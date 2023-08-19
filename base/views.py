# ---------------------------------------------
# import base django
from django.shortcuts import render, redirect
from django.utils.translation import get_language
from django.utils import translation
from django.views.generic.detail import DetailView
from django.db.models import Avg
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from django.contrib import messages
from django.http import HttpResponse
# ---------------------------------------------
# import models
from .models import Base
from .models import ContentBody
from .models import Education, GradeEducation
from .models import Skill, TypeSkills
from .models import MessageContact
# ---------------------------------------------
# import forms
from .forms import ContactForm
# ---------------------------------------------
# import base python
import xml.etree.ElementTree as ET
# ---------------------------------------------


def main_page(request):
    base_entry = Base.objects.first()
    content_body = ContentBody.objects.filter(translations__title="Main Page")[0]
    context = {
        'Base': base_entry,
        "Content_body": content_body,
        'get_last_url': request.path[4:-1],
        'base_data': f'base/js/data/{request.path[1:3]}.js',
    }
    return render(request, 'base/main_page.html', context=context)


def about_me_education(request):
    base_entry = Base.objects.all()[0]
    content_body = ContentBody.objects.filter(translations__title="Education")[0]
    education_base = Education.objects.all()
    context = {
        'Base': base_entry,
        "Content_body": content_body,
        "educations": education_base,
        # request.path[1:3] this is current language. Give from url.
        'content_data': parse(settings.STATIC_ROOT + f'/education/xml/{request.path[1:3]}_content.xml'),
        'get_last_url': request.path[4:-1],
        'base_data': f'base/js/data/{request.path[1:3]}.js',
    }
    return render(request, 'base/about_me/education/education.html', context=context)


class EducationDetail(DetailView):
    model = Education
    context_object_name = "education"
    template_name = 'base/about_me/education/education_detail.html'

    def get_context_data(self, **kwargs):
        detail_education = super(EducationDetail, self).get_context_data(**kwargs)
        base_entry = Base.objects.all()[0]
        content_body = ContentBody.objects.filter(translations__title="Education")[0]
        # detail_education["object"].id is id current Education
        grades = GradeEducation.objects.filter(education__id=detail_education["object"].id).translated('en').order_by("translations__commentary")
        grades_average = round(grades.aggregate(Avg('amount'))["amount__avg"],2)
        context = {
            "Education": detail_education,
            "Base": base_entry,
            "Content_body": content_body,
            "grades": grades,
            "grades_average": grades_average,
            'content_data': parse(settings.STATIC_ROOT + f'/education/xml/grades/{self.request.path[1:3]}_grades.xml'),
            "get_last_url": self.request.path[4:-1],
            'base_data': f'base/js/data/{self.request.path[1:3]}.js',
        }

        return context


def about_me_skills(request):
    base_entry = Base.objects.all()[0]
    content_body = ContentBody.objects.filter(translations__title="Skills")[0]
    skills_base = Skill.objects.translated('en').order_by("id").all()
    skills_type = TypeSkills.objects.all()
    context = {
        'Base': base_entry,
        "Content_body": content_body,
        # request.path[1:3] this is current language. Give from url.
        'content_data': f'skills/js/data/{request.path[1:3]}.js',
        'skills': skills_base,
        'skills_type': skills_type,
        'get_last_url': request.path[4:-1],
        'base_data': f'base/js/data/{request.path[1:3]}.js',
    }
    return render(request, 'base/about_me/skills.html', context=context)


def contacts(request):
    base_entry = Base.objects.all()[0]
    content_body = ContentBody.objects.filter(translations__title="Contacts")[0]
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "[Website 'About me'] [Contact]"
            body = {
                'first_name': form.cleaned_data['first_name'],
                'last_name': form.cleaned_data['last_name'],
                'email': form.cleaned_data['email_address'],
                'message': form.cleaned_data['message'],
            }
            message = "\n".join('{} : {}'.format(key, value) for key, value in body.items())
            messages.info(request,
                          MessageContact.objects.filter(translations__name="Send message!")[0].name)

            try:
                send_mail(subject, message, settings.EMAIL_HOST_USER, ['polozyuk.ser.work@gmail.com'])
            except BadHeaderError:
                return HttpResponse(MessageContact.objects.filter(translations__name=
                                                                "Invalid header found."))
            return redirect("/"+get_language()+'/main_page/')
        else:
            messages.error(request, MessageContact.objects.filter(translations__name=
                                                            "Doesn't send message!"))
    form = ContactForm()
    context = {
        'Base': base_entry,
        "Content_body": content_body,
        'get_last_url': request.path[4:-1],
        'base_data': f'base/js/data/{request.path[1:3]}.js',
        'form': form,
        }

    return render(request, 'base/contacts.html', context=context)


def parse(address):
    xmldoc = ET.parse(address)
    root = xmldoc.getroot()
    xml_dict = {child.tag: child.text for child in root}
    return xml_dict


def redirect_to_url_main_page(request):
    return redirect("/"+get_language()+'/main_page/')


# custom 400 view
def custom_400(request, exception):
    return render(request, 'base/HTTP_status/400.html', status=400)


# custom 401 view
def custom_401(request, exception):
    return render(request, 'base/HTTP_status/401.html', status=401)


# custom 403 view
def custom_403(request, exception):
    return render(request, 'base/HTTP_status/403.html', status=403)


# custom 404 view
def custom_404(request, exception):

    return render(request, 'base/HTTP_status/404.html', status=404)


# custom 500 view
def custom_500(request):
    return render(request, 'base/HTTP_status/500.html', status=500)


# custom 501 view
def custom_501(request):
    return render(request, 'base/HTTP_status/501.html', status=501)


# custom 503 view
def custom_503(request):
    return render(request, 'base/HTTP_status/503.html', status=503)


# custom 504 view
def custom_504(request):
    return render(request, 'base/HTTP_status/504.html', status=504)
