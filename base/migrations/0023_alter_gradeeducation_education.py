# Generated by Django 4.1.7 on 2023-03-19 13:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0022_alter_education_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gradeeducation',
            name='education',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.education'),
        ),
    ]