# Generated by Django 2.1.5 on 2019-03-13 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_auto_20190312_2139'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fillup',
            options={'ordering': ['-date']},
        ),
        migrations.RemoveField(
            model_name='car',
            name='driver',
        ),
        migrations.AlterField(
            model_name='fillup',
            name='date',
            field=models.DateField(verbose_name='fillup date'),
        ),
    ]
