# ---------------------------------------------
# import base django

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.translation import get_language
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError
# ---------------------------------------------
# import models

from base.models import Base, ContentBody
# ---------------------------------------------
# import forms
from .forms import EmailForm, NewEmailRecipientForm, NewEmailTemplateForm
# ---------------------------------------------

# import base python
import xml.etree.ElementTree as ET
# ---------------------------------------------


def index(request):
    base_entry = Base.objects.all()[0]
    content_body = ContentBody.objects.filter(translations__title="Main Page")[0]
    if request.method == 'POST':
        form = EmailForm(request.POST, user=request.user)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            for recipient in form.cleaned_data['emails_to']:
                message = form.cleaned_data['template'].body_message.replace("||Name||", recipient.name)
                try:
                    send_mail(subject, message, settings.EMAIL_HOST_USER, [recipient.email])
                except BadHeaderError:
                    return HttpResponse('Invalid header found.')
            return redirect("/"+get_language()+'/main_page/')
    form = EmailForm(user=request.user)
    context = {
        'Base': base_entry,
        "Content_body": content_body,
        'content_data': parse(f'project_1_sending_emails/static/project_1_sending_emails/xml/{request.path[1:3]}_content.xml'),
        'get_last_url': request.path[4:-1],
        'base_data': f'base/js/data/{request.path[1:3]}.js',
        'form': form
    }
    return render(request, 'projects/sending_emails/index.html', context=context)


def new_email_recipient(request):
    base_entry = Base.objects.first()
    content_body = ContentBody.objects.filter(translations__title="New Email Reception")[0]
    if request.method == "POST":
        form = NewEmailRecipientForm(request.POST,user=request.user)
        if form.is_valid():
            email_recipient = form.save()
            messages.success(request, "Good")
            return redirect("/"+get_language()+'/projects/sending_emails/')
        messages.error(request, "Bad")
    form = NewEmailRecipientForm( user=request.user)
    context = {
        "form": form,
        'Base': base_entry,
        "Content_body": content_body,
        'content_data': parse(
            f'project_1_sending_emails/static/project_1_sending_emails/xml/new_email_recipient/{request.path[1:3]}_form_new.xml'),
        'get_last_url': request.path[4:-1],
        'base_data': f'base/js/data/{request.path[1:3]}.js'

    }
    return render(request=request, template_name="projects/sending_emails/create_email_reception.html", context=context)


def new_email_template(request):
    base_entry = Base.objects.first()
    content_body = ContentBody.objects.filter(translations__title="New Email Template")[0]

    if request.method == "POST":

        form = NewEmailTemplateForm(request.POST, user=request.user)
        if form.is_valid():
            email_template = form.save()
            messages.success(request, "Good")
            return redirect("/"+get_language()+'/projects/sending_emails/')
        messages.error(request, "Bad")
    form = NewEmailTemplateForm( user=request.user)
    context = {
        "form": form,
        'Base': base_entry,
        "Content_body": content_body,
        'content_data': parse(
            f'project_1_sending_emails/static/project_1_sending_emails/xml/new_email_template/{request.path[1:3]}_form_new.xml'),

        'get_last_url': request.path[4:-1],
        'base_data': f'base/js/data/{request.path[1:3]}.js',
    }
    return render(request=request, template_name="projects/sending_emails/create_email_template.html", context=context)

def redirect_to_url_main_page(request):
    return redirect("/"+get_language()+'/main_page/')

def parse(address):
    xmldoc = ET.parse(address)
    root = xmldoc.getroot()
    xml_dict = {child.tag: child.text for child in root}
    return xml_dict