import random
from brain_games.games.game import game
from brain_games.welcome_user import welcome_user


def calc():
    how_to_answer = "What is the result of the expression?"
    number_of_question = 3
    math_oper = ["+", "-", "*"]
    name = welcome_user()
    print(how_to_answer)
    result = True
    for i in range(number_of_question):
        if result is False:
            break
        a = random.randint(1, 30)
        b = random.randint(1, 15)
        j = random.randint(0, 2)
        question = f"{a} {math_oper[j]} {b}"
        correct_answer = f"{eval(str(a) + math_oper[j] + str(b))}"
        result = game(question, correct_answer, i, number_of_question, name)
