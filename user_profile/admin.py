from django.contrib import admin
from parler.admin import TranslatableAdmin
# Register your models here.

from .models import MessageUser

admin.site.register(MessageUser, TranslatableAdmin)
