# Generated by Django 3.1.7 on 2021-04-14 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trivia', '0006_gamedata_playing_yn'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gamedata',
            name='playing_yn',
        ),
        migrations.AddField(
            model_name='gamedata',
            name='status',
            field=models.CharField(default='wait', max_length=5),
        ),
    ]
