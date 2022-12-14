# Generated by Django 4.1.3 on 2022-11-22 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobData', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorie',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='companydetail',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='jobdetail',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='state',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='subcategorie',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
