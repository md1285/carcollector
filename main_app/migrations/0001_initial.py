# Generated by Django 2.1.5 on 2019-03-11 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=100)),
                ('engine', models.CharField(max_length=100)),
                ('make', models.CharField(max_length=100)),
                ('style', models.CharField(max_length=100)),
                ('driver', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
            ],
        ),
    ]
