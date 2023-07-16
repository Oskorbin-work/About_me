# ---------------------------------------------
# import base django
from django.shortcuts import render, redirect
from django.utils.translation import get_language
from django.views.generic.detail import DetailView
from django.db.models import Avg
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
# ---------------------------------------------
# import models
from .models import Base
from .models import ContentBody
from .models import Education, GradeEducation
from .models import Skill, TypeSkills
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
        'content_data': parse(f'base/static/education/xml/{request.path[1:3]}_content.xml'),
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
            'content_data': parse(f'base/static/education/xml/grades/{self.request.path[1:3]}_grades.xml'),
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
            subject = "Website Inquiry"
            body = {
                'first_name': form.cleaned_data['first_name'],
                'last_name': form.cleaned_data['last_name'],
                'email': form.cleaned_data['email_address'],
                'message': form.cleaned_data['message'],
            }
            message = "\n".join('{} : {}'.format(key, value) for key, value in body.items())
            try:
                send_mail(subject, message, 'polozyuk.ser.work@gmail.com', ['polozyuk.ser.work@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect("/"+get_language()+'/main_page/')
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
