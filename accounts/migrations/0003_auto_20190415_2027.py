# Generated by Django 2.2 on 2019-04-15 14:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20190415_2016'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='gender1',
            new_name='gender',
        ),
    ]
