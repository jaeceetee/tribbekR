# Generated by Django 3.1.7 on 2021-04-12 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trivia', '0005_host'),
    ]

    operations = [
        migrations.AddField(
            model_name='gamedata',
            name='playing_yn',
            field=models.BooleanField(default=True),
        ),
    ]
