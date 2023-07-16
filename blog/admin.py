from django.contrib import admin

from .models import Post, TagsPost

# For body page. One basedata to page "Blog"
admin.site.register(Post)
admin.site.register(TagsPost)

# Register your models here.
