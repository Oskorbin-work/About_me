# Generated by Django 4.1.7 on 2023-03-25 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0031_alter_education_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gradeeducation',
            name='type',
        ),
        migrations.AddField(
            model_name='gradeeducationtranslation',
            name='comment',
            field=models.CharField(blank=True, max_length=90),
        ),
    ]
