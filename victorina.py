import json
import random

def import_questions_base():
    with open('questions.json', encoding='UTF=8') as file:
        questions_base = json.load(file)
    return questions_base

def set_lifes():
    try:
        lifes = int(input('Введите количество жизней '))
    except:
        print('аяяй! введите число!!')

def add_players():
    player_1 = input('Введите имя первого игрока')
    player_2 = input('Введите имя второго игрока')
    return player_1, player_2
  
def choose_random_question():
    pass

 
while True:
    set_lifes()
    add_players()

