# Generated by Django 3.1.4 on 2020-12-24 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_page', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(upload_to='profile_pics'),
        ),
    ]
