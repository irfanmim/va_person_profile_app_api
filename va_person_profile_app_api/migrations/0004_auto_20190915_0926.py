# Generated by Django 2.1.7 on 2019-09-15 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('va_person_profile_app_api', '0003_auto_20190915_0105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
