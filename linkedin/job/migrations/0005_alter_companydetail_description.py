# Generated by Django 4.1.3 on 2022-11-18 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0004_alter_companydetail_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companydetail',
            name='description',
            field=models.CharField(max_length=1500),
        ),
    ]
