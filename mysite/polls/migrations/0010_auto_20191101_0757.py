# Generated by Django 2.2.6 on 2019-11-01 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0009_auto_20191031_1151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='status',
            field=models.TextField(),
        ),
    ]
