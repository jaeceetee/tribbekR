from django.core.exceptions import DisallowedHost
from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.related import ForeignKey
from django.contrib.auth.models import Group, Permission
from django.conf import settings
# Create your models here.

class GameData(models.Model):
    game_id = models.AutoField(primary_key=True)
    game_name = models.CharField(max_length=500, default="Game!")
    player_num = models.IntegerField()
    question_num = models.IntegerField()
    category = models.IntegerField()
    league_id = models.ForeignKey("LeagueData", on_delete=models.CASCADE, blank=True, null=True)
    host = models.ForeignKey(User, on_delete=models.CASCADE)
    playing_yn = models.BooleanField(default=True)
    play_DT = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.game_name + " By " + str(self.host)


class ScoreData(models.Model):
    player_id = models.ForeignKey("PlayerData", on_delete=models.CASCADE)
    game_id = models.ForeignKey("GameData", on_delete=models.CASCADE)
    score = models.IntegerField()

    def __str__(self) -> str:
        return str(self.game_id) + " " + str(self.player_id) + " " + str(self.score)
    

class PlayerData(models.Model):
    player_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=1000) 

    def __str__(self) -> str:
        return self.name

class LeagueData(models.Model):
    league_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=500)
    end_game_num = models.IntegerField(null=True, blank=True)
    last_game_num = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.name

class Questions(models.Model):
    game_id = models.ForeignKey("GameData", on_delete=models.CASCADE)
    question_num = models.IntegerField()
    question = models.TextField()
    answer = models.CharField(max_length=200)
    wrong1 = models.CharField(max_length=200, blank=True, null=True)
    wrong2 = models.CharField(max_length=200, blank=True, null=True)
    wrong3 = models.CharField(max_length=200, blank=True, null=True)
    truefalse = models.BooleanField()

    def __str__(self) -> str:
        return str(self.game_id) + str(self.question_num)

class Host(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        permissions = [
            ("host_game", "Host a game")
        ]

# host_group, created = Group.objects.get_or_create(name='Host')
# host_group.permissions.set("HOST")