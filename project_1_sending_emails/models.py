from django.db import models


class Destination(models.Model):
    email = models.CharField(max_length=256)
    name = models.CharField(max_length=256)
    tag = models.CharField(max_length=256)


class TemplateEmail(models.Model):
    # structure email get from https://erinwrightwriting.com/wp-content/uploads/2015/06/Basic-Email-Format.jpg
    from_email = models.EmailField(null=True)
    # Subject line
    subject_line = models.CharField(max_length=256)
    # Salutation
    opening_message = models.CharField(max_length=256)
    # Message
    body_message = models.TextField()
    # Closing
    closing_message = models.CharField(max_length=256)
    # Signature Block
    signature_block = models.CharField(max_length=256)

