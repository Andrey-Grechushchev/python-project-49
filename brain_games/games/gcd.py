import random
import math
from brain_games import constants
from brain_games.game import run_game
from brain_games.welcome_user import welcome_user


def gcd():
    name = welcome_user()
    print(constants.INTRO_GCD)
    result = True
    for i in range(constants.NUMBER_OF_QUESTIONS):
        if not result:
            break
        a = random.randint(constants.MIN_NUM_GCD_1, constants.MAX_NUM_GCD_1)
        b = random.randint(constants.MIN_NUM_GCD_2, constants.MAX_NUM_GCD_2)
        question = f"{a} {b}"
        correct_answer = f"{math.gcd(a, b)}"
        result = run_game(question, correct_answer, i,
                          constants.NUMBER_OF_QUESTIONS, name)
