from django.db import models
from parler.models import TranslatableModel, TranslatedFields
import datetime
from django.urls import reverse
from django.contrib.auth.models import User
from django.conf import settings


class TagsPost(models.Model):
    name = models.CharField(verbose_name="name_30", max_length=30, blank=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField( max_length=80, blank=True, )
    img_main = models.ImageField(upload_to='posts/', blank=True, max_length=500)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL,)
    body = models.TextField(blank=True,)
    data_published = models.DateField(default=datetime.date.today)
    tags = models.ManyToManyField(TagsPost, blank=True)
    slug = models.SlugField(null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"slug": self.slug})