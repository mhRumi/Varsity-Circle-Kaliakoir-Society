# Generated by Django 2.2.6 on 2019-10-26 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20191025_0548'),
    ]

    operations = [
        migrations.AddField(
            model_name='userlogin',
            name='img',
            field=models.ImageField(default='user.png', upload_to=''),
        ),
    ]
