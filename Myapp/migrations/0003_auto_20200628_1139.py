# Generated by Django 3.0.7 on 2020-06-28 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Myapp', '0002_questions_result'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='result',
            field=models.BooleanField(),
        ),
    ]
