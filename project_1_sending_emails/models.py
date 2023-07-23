from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from parler.models import TranslatableModel, TranslatedFields


class EmailRecipient(models.Model):
    email = models.EmailField(null=True)
    name = models.CharField(max_length=200)
    user_owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.email + " (" + self.name+")"


class EmailTemplate(models.Model):
    # Message
    body_message = models.TextField()
    name = models.CharField(max_length=200)
    user_owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class MessageEmail(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=400, blank=True,),
    )

    def __str__(self):
        return self.name





