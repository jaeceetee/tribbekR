# Generated by Django 3.1.7 on 2021-03-26 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trivia', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamedata',
            name='category',
            field=models.IntegerField(),
        ),
    ]
