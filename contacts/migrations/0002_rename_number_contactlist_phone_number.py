# Generated by Django 4.0.6 on 2022-07-27 16:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactlist',
            old_name='number',
            new_name='Phone_number',
        ),
    ]
