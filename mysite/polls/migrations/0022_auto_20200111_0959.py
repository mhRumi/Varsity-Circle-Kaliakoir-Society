# Generated by Django 2.2.6 on 2020-01-11 09:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0021_comments'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comments',
            old_name='comments',
            new_name='user',
        ),
    ]
