# Generated by Django 3.0.7 on 2020-06-28 06:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Myapp', '0004_auto_20200628_1140'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questions',
            name='result',
        ),
    ]
