# Generated by Django 3.0.7 on 2020-06-28 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Myapp', '0007_remove_questions_result'),
    ]

    operations = [
        migrations.AddField(
            model_name='questions',
            name='result',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
