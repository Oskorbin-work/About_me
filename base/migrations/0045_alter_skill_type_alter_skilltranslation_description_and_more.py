# Generated by Django 4.1.7 on 2023-04-30 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0044_alter_skill_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='type',
            field=models.CharField(blank=True, choices=[('Base', 'Base'), ('Framework and libs', 'Framework and libs'), ('Tools', 'Tools'), ('Other', 'Other')], max_length=50, verbose_name='type_50'),
        ),
        migrations.AlterField(
            model_name='skilltranslation',
            name='description',
            field=models.CharField(blank=True, max_length=100, verbose_name='description_100'),
        ),
        migrations.AlterField(
            model_name='skilltranslation',
            name='name',
            field=models.CharField(blank=True, max_length=90, verbose_name='name_90'),
        ),
    ]
