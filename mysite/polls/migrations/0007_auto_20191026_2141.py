# Generated by Django 2.2.6 on 2019-10-26 21:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_auto_20191026_2139'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userlogin',
            old_name='imgage',
            new_name='image',
        ),
    ]
