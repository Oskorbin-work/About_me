# ---------------------------------------------
# import base django
from django.shortcuts import  redirect
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.utils.translation import get_language
# ---------------------------------------------
# import models
from .models import Post
from base.models import Base
from base.models import ContentBody
# ---------------------------------------------
# import forms
from .forms import NewPostForm
# ---------------------------------------------
# import base python
import xml.etree.ElementTree as ET
# ---------------------------------------------


class PostListView(ListView):
    model = Post
    paginate_by = 5  # if pagination is desired
    ordering = ['-data_published']

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        base_entry = Base.objects.all()[0]
        content_body = ContentBody.objects.filter(translations__title="Posts")[0]
        ctx['Base'] = base_entry
        ctx['Content_body'] = content_body
        ctx['get_last_url'] = self.request.path[4:-1]
        ctx['blog_data'] = parse(f'blog/static/posts/xml/{self.request.path[1:3]}_content.xml')
        ctx['base_data'] = f'base/js/data/{self.request.path[1:3]}.js'
        return ctx


class PostDetailView(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        base_entry = Base.objects.all()[0]
        content_body = ContentBody.objects.filter(translations__title="Posts")[0]
        ctx['Base'] = base_entry
        ctx['Content_body'] = content_body
        ctx['get_last_url'] = self.request.path[4:-1]
        ctx['post_data'] = parse(f'blog/static/posts/xml/post/{self.request.path[1:3]}_post.xml')
        ctx['blog_data'] = parse(f'blog/static/posts/xml/{self.request.path[1:3]}_content.xml')
        ctx['base_data'] = f'base/js/data/{self.request.path[1:3]}.js'
        return ctx


class PostCreate(CreateView):
    template_name = "blog/post_create.html"
    form_class = NewPostForm

    def get_success_url(self):
        return "/" + get_language() + '/blog/post_list/'

    def get_form_kwargs(self):
        ctx = super(PostCreate, self).get_form_kwargs()
        ctx['user'] = self.request.user
        return ctx

    def get_context_data(self, **kwargs):
        ctx = super(PostCreate, self).get_context_data(**kwargs)
        base_entry = Base.objects.all()[0]
        content_body = ContentBody.objects.filter(translations__title="Create a post")[0]
        ctx['Base'] = base_entry
        ctx['Content_body'] = content_body
        ctx['get_last_url'] = self.request.path[4:-1]
        ctx['base_data'] = f'base/js/data/{self.request.path[1:3]}.js'
        return ctx


def parse(address):
    xmldoc = ET.parse(address)
    root = xmldoc.getroot()
    xml_dict = {child.tag: child.text for child in root}
    return xml_dict


def redirect_to_url_blog(request):
    return redirect("/"+get_language()+'/blog/post_list/')

