# Generated by Django 2.2.6 on 2019-11-04 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0013_profile_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='postOffice',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='profile',
            name='village',
            field=models.CharField(default='', max_length=50),
        ),
    ]
