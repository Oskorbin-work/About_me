# Generated by Django 4.1.7 on 2023-07-19 05:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project_1_sending_emails', '0002_emailend_emailrecipient_emailtemplate_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='EmailEnd',
        ),
    ]
