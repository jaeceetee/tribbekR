# from channels import Group
import json
from typing import NoReturn
from trivia.views import play_game
from channels.db import database_sync_to_async
from asgiref.sync import sync_to_async
from .models import GameData, PlayerData, ScoreData
from channels.generic.websocket import AsyncWebsocketConsumer

class TriviaConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['game_num']
        self.room_group_name = 'chat_%s' % self.room_name
        self.user = self.scope["user"]
        self.host = self.scope["session"]["host"]

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

        if self.host == False:
        
            player = self.get_player_data()

            game = await self.get_game_data()

            await self.create_score_data(player=player, game=game)

            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'new_player',
                    'user': self.user.username,
                }
        )

    @database_sync_to_async
    async def create_score_data(self, player, game):
        score = ScoreData(game_id=game.game_id, player_id=player.player_id)
        score.save()
        NoReturn


    @database_sync_to_async
    async def get_game_data(self):
        game = GameData.objects.get(game_id = self.room_name)
        return game
    
    @database_sync_to_async
    async def get_player_data(self):
        if PlayerData.objects.get(name = self.user.username) is None:
            player = PlayerData(name = self.user.username)
            player.save()
        else:
            player = PlayerData.objects.get(name = self.user.username)

        return player

    @database_sync_to_async
    async def get_player_number(self):
        if ScoreData.objects.filter(game_id = self.room_name).count() > 0:
            return 0
        else:
            return ScoreData.objects.filter(game_id = self.room_name).count()

    async def new_player(self, event):
        player = event['user']

        await self.send(text_data=json.dumps({
            'player' : player,
        }))

    async def disconnect(self, close_code):

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'user_disconnect',
                'user': self.user.username,
            }
        )
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def user_disconnect(self, event):
        remove_player = event['user']

        await self.send(text_data=json.dumps({
            'remove_player': remove_player
        }))


    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        self.send(text_data=json.dumps({
            'message': message
        }))
        return super().receive(text_data=text_data)

    # def connect(self):
    #     self.accept()