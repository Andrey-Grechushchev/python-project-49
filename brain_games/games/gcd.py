import random
import math
from brain_games.games.game import game
from brain_games.welcome_user import welcome_user


def gcd():
    how_to_answer = "Find the greatest common divisor of given numbers."
    number_of_question = 3
    name = welcome_user()
    print(how_to_answer)
    result = True
    for i in range(number_of_question):
        if result is False:
            break
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        question = f"{a} {b}"
        correct_answer = f"{math.gcd(a, b)}"
        result = game(question, correct_answer, i, number_of_question, name)
