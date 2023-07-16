# Generated by Django 4.1.7 on 2023-03-19 11:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_alter_gradeeducationtranslation_amount_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gradeeducationtranslation',
            name='coins',
        ),
        migrations.AlterField(
            model_name='gradeeducationtranslation',
            name='amount',
            field=models.IntegerField(default=1, max_length=90, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)]),
        ),
    ]
