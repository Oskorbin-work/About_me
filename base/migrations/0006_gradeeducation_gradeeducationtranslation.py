# Generated by Django 4.1.7 on 2023-03-18 14:20

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import parler.fields
import parler.models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_education_educationtranslation'),
    ]

    operations = [
        migrations.CreateModel(
            name='GradeEducation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'abstract': False,
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='GradeEducationTranslation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('name', models.CharField(max_length=90)),
                ('type', models.CharField(max_length=90)),
                ('coins', models.CharField(max_length=90)),
                ('amount', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)])),
                ('education', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.education')),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='base.gradeeducation')),
            ],
            options={
                'verbose_name': 'grade education Translation',
                'db_table': 'base_gradeeducation_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
    ]