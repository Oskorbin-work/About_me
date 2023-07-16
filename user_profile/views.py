# ---------------------------------------------
# import base django
from django.shortcuts import render, redirect
from .forms import NewUserForm, UserProfile
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User, Group
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import get_language
# import models from app "base"
from base.models import Base
from base.models import ContentBody
# ---------------------------------------------
# import models
from .models import MessageUser


def register_request(request):
    base_entry = Base.objects.first()
    content_body = ContentBody.objects.filter(translations__title="Register")[0]
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, MessageUser.objects.filter(translations__name="Registration successful")[0].name)
            return redirect("/"+get_language()+'/main_page/')
        messages.error(request, MessageUser.objects.filter(translations__name=
                                                           "Unsuccessful registration. Invalid information.")[0].name)
    form = NewUserForm()
    context = {
        "register_form": form,
        'Base': base_entry,
        "Content_body": content_body,
        'content_data': f'user_profile/register/data/{request.path[1:3]}.js',
        'get_last_url': request.path[4:-1],
        'base_data': f'base/js/data/{request.path[1:3]}.js',

    }
    return render(request=request, template_name="user_profile/register.html", context=context)


def login_request(request):
    base_entry = Base.objects.first()
    content_body = ContentBody.objects.filter(translations__title="Login")[0]
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("/"+get_language()+'/main_page/')
            else:
                messages.error(request, MessageUser.objects.filter(translations__name="Invalid username or password.")[0].name)
        else:
            messages.error(request, MessageUser.objects.filter(translations__name="Invalid username or password.")[0].name)
    form = AuthenticationForm()
    context = {
        "login_form": form,
        'Base': base_entry,
        "Content_body": content_body,
        'content_data': f'user_profile/login/data/{request.path[1:3]}.js',
        'get_last_url': request.path[4:-1],
        'base_data': f'base/js/data/{request.path[1:3]}.js',
    }
    return render(request=request, template_name="user_profile/login.html", context=context)


def logout_request(request):
    logout(request)
    messages.info(request, MessageUser.objects.filter(translations__name="You have successfully logged out.")[0].name)
    return redirect("/"+get_language()+'/main_page/')


def profile(request, username):
    base_entry = Base.objects.first()
    content_body = ContentBody.objects.filter(translations__title="Profile")[0]
    profile = User.objects.filter(username=username).first()
    all_groups = Group.objects.all()
    if request.method == "POST":
        form = UserProfile(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.info(request,
                          MessageUser.objects.filter(translations__name="Saved successfully!")[0].name)
            return redirect("/"+get_language()+'/user/profile/' + username + "/")

    if profile:
        form = UserProfile(instance=profile)
        context = {
            "profile_form": form,
            'Base': base_entry,
            "Content_body": content_body,
            "user_groups": all_groups,
            'content_data': f'user_profile/profile/data/{request.path[1:3]}.js',
            'get_last_url': request.path[4:-1],
            'base_data': f'base/js/data/{request.path[1:3]}.js',
        }
        return render(request, 'user_profile/profile.html', context=context)

    return redirect("/"+get_language()+'/main_page/')

