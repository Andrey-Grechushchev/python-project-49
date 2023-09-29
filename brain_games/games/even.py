import random
from brain_games.games.game import game
from brain_games.welcome_user import welcome_user


def even():
    how_to_answer = 'Answer "yes" if the number is even, otherwise answer "no".'
    number_of_question = 3
    name = welcome_user()
    print(how_to_answer)
    result = True
    for i in range(number_of_question):
        if result is False:
            break
        question = random.randint(1, 100)
        correct_answer = question % 2 == 0 and "yes" or "no"
        result = game(question, correct_answer, i, number_of_question, name)
