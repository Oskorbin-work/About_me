# Generated by Django 4.1.7 on 2023-03-19 12:59

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0013_remove_gradeeducation_foo_field_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='gradeeducation',
            name='amount',
            field=models.IntegerField(blank=True, default=1, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AddField(
            model_name='gradeeducation',
            name='type',
            field=models.CharField(blank=True, choices=[('B', 'Base'), ('PT', 'Practical training'), ('C', 'Certification')], max_length=90),
        ),
    ]