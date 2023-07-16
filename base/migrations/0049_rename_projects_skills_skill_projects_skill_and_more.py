# Generated by Django 4.1.7 on 2023-05-02 12:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0048_typeskills_typeskillstranslation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='skill',
            old_name='projects_skills',
            new_name='projects_skill',
        ),
        migrations.AddField(
            model_name='skill',
            name='type_skill',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.typeskills'),
        ),
    ]
