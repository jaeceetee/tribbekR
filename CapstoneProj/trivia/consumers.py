# from channels import Group
import json
from random import shuffle
from typing import NoReturn
from trivia.views import play_game
from channels.db import database_sync_to_async
from asgiref.sync import sync_to_async
from .models import GameData, PlayerData, ScoreData, Questions
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
        
            player = await self.get_player_data()

            game = await self.get_game_data()

            await self.create_score_data(player=player, game=game)

            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'new_player',
                    'user': self.user.username,
                }
            )

    async def new_player(self, event):
        print("new player")
        player = event['user']

        await self.send(text_data=json.dumps({
            'player' : player,
        }))

    @database_sync_to_async
    async def create_score_data(self, player, game):
        score = ScoreData(game_id=game.game_id, player_id=player.player_id)
        score.save()
        NoReturn

    @database_sync_to_async
    async def delete_score_data(self, player, game):
        score = ScoreData.objects.filter(game_id=game.game_id, player_id=player.player_id)
        score.delete()

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
        player = self.get_player_data()
        game = await self.get_game_data()
        await self.delete_score_data(player=player, game=game)
        remove_player = event['user']

        await self.send(text_data=json.dumps({
            'remove_player': remove_player
        }))

    async def receive(self, text_data):
        print(text_data)
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        print(message)

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type':'question',
                'message':message
            }
        )



        # if message == 'start':
        #     print("started")
        #     # question = await Questions.objects.get(game_id=self.room_name, question_num=1)
        #     question = self.get_first_question_data()
        #     print(question)


        #     self.channel_layer.group_send(
        #     self.room_group_name,
        #     {
        #         'type': 'question',
        #         'question_num': 1
        #     }
        # )
    async def question(self, event):
        print("questions!!")
        print(event)
        what = await self.get_first_question_data()
        print(what)
        self.channel_layer.send(
            "update-question",{
                "type": "next_question",
                "question_num": 1
            }
        )

        await self.send(text_data=json.dumps({
            "first_question": "question"
        }))

    @database_sync_to_async
    async def get_first_question_data(self):
        print("question database!")
        questions = (Questions.objects.filter(game_id=self.room_name, question_num=1))
        for question in questions:
            print(question)
        return questions

        #    message = await self.start_game()
            
        #     # self.send(text_data=json.dumps({
        #     #     'type': 'start_game'
        #     # }))
        #     return super().receive(text_data=text_data)
        # else:
        #

        

    async def start_game(self):
        print('got to start_game')
        # num = 1
        question = await self.get_question_data(1)
        print(question)

        choices = [
            question.answer,
            question.wrong1,
            question.wrong2,
            question.wrong3,
        ]
        
        shuffle(choices)

        
        
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'question',
                'question_number:': 1,
                'question:': question.question,
                'answer': question.answer,
                'choices': choices,
                'truefalse': question.truefalse,

            })
        return "success"




    # def connect(self):
    #     self.accept()