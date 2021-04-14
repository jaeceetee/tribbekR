# Generated by Django 3.1.7 on 2021-03-30 18:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trivia', '0002_auto_20210325_2116'),
    ]

    operations = [
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_num', models.IntegerField()),
                ('question', models.TextField()),
                ('answer', models.CharField(max_length=200)),
                ('wrong1', models.CharField(blank=True, max_length=200, null=True)),
                ('wrong2', models.CharField(blank=True, max_length=200, null=True)),
                ('wrong3', models.CharField(blank=True, max_length=200, null=True)),
                ('truefalse', models.BooleanField()),
                ('game_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trivia.gamedata')),
            ],
        ),
    ]