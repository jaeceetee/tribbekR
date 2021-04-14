from requests.models import Response
from .models import GameData, LeagueData, Questions
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse
import requests, json, random

# Create Game
def create_game(request):
    if request.method == "POST":
        form = request.POST 

        game_data = GameData()
        game_data.game_name = form['GameLeagueName']
        game_data.player_num = form['PlayerNum']
        game_data.question_num = form['questionNum']
        game_data.category = form['category']
        game_data.host = User.objects.get(id=request.user.id)

        # if form['LeagueYN'].checked == True:
        #     league = LeagueData()
        #     league.name = game_data.game_name
        #     league.end_game_num = 10 # Will add this function
        #     league.save()

        #     game_data.league_id = league.league_id
        
        game_data.save()
        #game_data_saved = GameData.objects.last()
        #print(game_data_saved)
     
        url = f'https://opentdb.com/api.php?amount={form["questionNum"]}&category={form["category"]}'

        response = requests.get(url)
        response.encoding = 'utf-8'
        json_data = json.loads(response.text)

        num = 0
        
        for items in json_data['results']:
            num += 1
            question = Questions()
            question.game_id = game_data
            question.question_num = num
            question.question = items['question']
            question.answer = items['correct_answer']
            if items['type'] == 'multiple':
                question.wrong1 = items['incorrect_answers'][0]
                question.wrong2 = items['incorrect_answers'][1]
                question.wrong3 = items['incorrect_answers'][2]
                
                question.truefalse = False
            else:
                question.truefalse = True
            question.save()

        # Get first question to send to the question page
        # question = Questions.objects.get(game_id = game_data, question_num = 1)

        # multichoice = []    
        # if question.truefalse == False:
        #     multichoice.append(question.answer)
        #     multichoice.append(question.wrong1)
        #     multichoice.append(question.wrong2)
        #     multichoice.append(question.wrong3)

        # random.shuffle(multichoice)
        
        print(game_data.host.username)
        request.session['game_id'] = game_data.pk
        request.session['host'] = True

        return redirect('/trivia/' + str(game_data.game_id) + '/host_screen', game_name=game_data.game_name)
        # ('trivia/'+ str(game_data.game_id) + '/host_screen.html')
    elif request.method == "GET":
        url = 'https://opentdb.com/api_category.php'
        
        response = requests.get(url)
        response.encoding = 'utf-8'
        json_data = json.loads(response.text)
        
        categories = [items for items in json_data['trivia_categories']]

        context = {
            "categories": categories
        }

        return render(request, 'trivia/create_game.html', context)

    else:
        return render(request, 'Users/register.html')

def nextQuestion(request, question_num):

    game_data = GameData.objects.get(game_id=request.session['game_id'])
    question_num += 1

    if game_data['question_num'] < question_num:

        question = Questions.objects.get(game_id=request.session['game_id'], question_num=question_num)

        multichoice = []    
        if question.truefalse == False:
            multichoice.append(question.answer)
            multichoice.append(question.wrong1)
            multichoice.append(question.wrong2)
            multichoice.append(question.wrong3)

        random.shuffle(multichoice)

        context = {
            "question": question,
            "choices": multichoice
            }

        return render(request, 'trivia/question.html', context)
    else:
        return render(request, 'trivia/completed.html')

def user_list(request):
    return render(request, 'trivia/user_list.html')

def play_game(request):
    #Check for playable rooms
    
    try:
        open_games = GameData.objects.filter(playing_yn=True)
    except:
        return render(request, 'trivia/play_game.html')

    
    context = {
        "open_games":open_games
    }

    return render(request, 'trivia/play_game.html', context)

def player(request, game_num):
    request.session['host'] = False
    return render(request, 'trivia/player_screen.html', {
        'game_num': game_num
    })

def question(request, room_name, question_num):
    return render(request, 'trivia/player_screen.html', {
        'room_name': room_name,
        'question_num': question_num
    })

def host_screen(request, game_num):
    context = {
        "game_num":game_num
    }
    return render(request, 'trivia/host_screen.html', context)