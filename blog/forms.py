from django import forms
from .models import Post
# Create your forms here.
import datetime

from django.contrib.auth.models import User


class NewPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(NewPostForm, self).__init__(*args, **kwargs)
        self.fields['author'] = forms.ModelChoiceField(queryset=User.objects.all(), initial=self.user, disabled=True)

    title = forms.CharField(required=True)
    img_main = forms.ImageField(required=True)
    data_published = forms.DateField(required=True, disabled=True, initial=datetime.date.today)
    slug = forms.SlugField(required=True)

    class Meta:
        model = Post
        fields = ("title", "slug", "img_main", "body", "tags", "data_published", "author")
