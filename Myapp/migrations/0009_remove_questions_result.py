# Generated by Django 3.0.7 on 2020-06-28 06:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Myapp', '0008_questions_result'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questions',
            name='result',
        ),
    ]
