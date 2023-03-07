import json
import random

ball_1 = 0
ball_2 = 0
lifes = 0
lifes_1 = 1
lifes_2 = 1

def say_hi():
    print('Добро пожаловать в викторину!')

def import_questions_base():
    global questions_base
    with open('questions.json', encoding='UTF=8') as file:
        questions_base = json.load(file)


def set_lifes():
    global lifes
    global lifes_1
    global lifes_2
    try:
        lifes = int(input('Введите количество жизней больше нуля '))
        lifes_1 = lifes
        lifes_2 = lifes
    except:
        print('аяяй! введите число!!')

def add_players():
    global player_1
    global player_2
    player_1 = input('Введите имя первого игрока ')
    player_2 = input('Введите имя второго игрока ')

  
def choose_random_question():
    """выдает случайный вопрос из базы"""
    global lifes
    global lifes_1
    global lifes_2
    global ball_1
    global ball_2
    question = random.choice(questions_base)
    questions_base.remove(question)
    for key in question.keys():
        print(key)
        break
    print(f'Ходит {player_1.title()}')
    if input('\t').lower() == question[key]:
        ball_1 += 1
        print(f'ты угадал. У тебя {ball_1} баллов')
    else:
        lifes_1 -= 1
        print(f'Ты не угадал. Теряешь жизнь! Теперь у тебя {lifes_1} жизней. У тебя {ball_1} баллов\n')
    print(f'Ходит {player_2.title()}')
    if input('\t').lower() == question[key]:
        ball_2 += 1
        print(f'ты угадал. У тебя {ball_2} баллов')
    else:
        lifes_2 -= 1
        print(f'Ты не угадал. Теряешь жизнь! Теперь у тебя {lifes_2} жизней. У тебя {ball_2} баллов\n')

set_lifes()
add_players()
while lifes_1 > 0 or lifes_2 > 0: 
    import_questions_base()
    choose_random_question()

