from requests.models import Response
from .models import GameData, LeagueData, Questions
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse
from .serializer import QuestionSerializer
import requests, json, random

# Create Game
def create_game(request):
    if request.method == "POST":
        form = request.POST 

        game_data = GameData()
        game_data.game_name = form['GameLeagueName']
        game_data.player_num = 1
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
        
        questions_to_send={}
        for items in json_data['results']:
            num += 1
            question = Questions()
            
            question.game_id = game_data
            question.question_num = num
            question.question = items['question']
            question.answer = items['correct_answer']
            questions_to_send[num] ={
                "question_num": num,
                "question": items['question'],
                "answer": items['correct_answer']
            }
            if items['type'] == 'multiple':
                question.wrong1 = items['incorrect_answers'][0]
                question.wrong2 = items['incorrect_answers'][1]
                question.wrong3 = items['incorrect_answers'][2]
                
                question.truefalse = False
                questions_to_send[num]["truefalse"] = False
                questions_to_send[num]["wrong1"] = items['incorrect_answers'][0]
                questions_to_send[num]["wrong2"] = items['incorrect_answers'][1]
                questions_to_send[num]["wrong3"] = items['incorrect_answers'][2]

            else:
                question.truefalse = True
                questions_to_send[num]["truefalse"] = True
            
            question.save()

        print(game_data.host.username)
        request.session['game_id'] = game_data.pk
        request.session['host'] = True
        request.session['total_questions'] = game_data.question_num

  
        return redirect('/trivia/' + str(game_data.game_id) + '/host_screen')
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
        open_games = GameData.objects.filter(status="wait")
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
    total_questions = request.session['total_questions']
    questions = Questions.objects.filter(game_id=game_num)
    questions_to_send = []
    for q in questions:
        if q.truefalse == True:
            questions_to_send.append({
                "question_num": q.question_num,
                "question": q.question,
                "truefalse": q.truefalse,
                "answer": q.answer
            })
        else:
            questions_to_send.append({
                "question_num": q.question_num,
                "question": q.question,
                "truefalse": q.truefalse,
                "answer": q.answer,
                "choices": [
                    q.wrong1,
                    q.wrong2,
                    q.wrong3,
                    q.answer
                ]
            })
        
        question_to_serialize = Questions.objects.filter(game_id=game_num)


    print(questions)
    context = {
        "game_num":game_num,
        "total_questions": total_questions,
        "questions": questions_to_send,
        "serializedQ": QuestionSerializer(question_to_serialize, many=True).data,

    }
    return render(request, 'trivia/host_screen.html', context)