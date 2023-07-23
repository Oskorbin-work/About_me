from django.contrib import admin
from parler.admin import TranslatableAdmin

from .models import EmailRecipient, EmailTemplate, MessageEmail


admin.site.register(EmailRecipient)
admin.site.register(EmailTemplate)
admin.site.register(MessageEmail, TranslatableAdmin)

# Register your models here.
