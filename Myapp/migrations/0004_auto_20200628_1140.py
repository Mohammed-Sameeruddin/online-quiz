# Generated by Django 3.0.7 on 2020-06-28 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Myapp', '0003_auto_20200628_1139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='result',
            field=models.BooleanField(default=False),
        ),
    ]
