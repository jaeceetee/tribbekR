from django.contrib.auth.models import User
from .models import GameData, Host, LeagueData, PlayerData, Questions, ScoreData, Host
from django.contrib import admin

# Register your models here.
admin.site.register(GameData)
admin.site.register(LeagueData)
admin.site.register(Questions)
admin.site.register(PlayerData)
admin.site.register(ScoreData)
admin.site.register(Host)