# Generated by Django 2.1.5 on 2019-03-12 21:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_fillups'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Fillups',
            new_name='Fillup',
        ),
    ]
