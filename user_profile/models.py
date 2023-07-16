from django.db import models
from parler.models import TranslatableModel, TranslatedFields
# Create your models here.


class MessageUser(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=400, blank=True,),
    )

    def __str__(self):
        return self.name

