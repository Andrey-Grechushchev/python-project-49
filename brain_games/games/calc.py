import random
from brain_games import constants
from brain_games.game import run_game
from brain_games.welcome_user import welcome_user


def calc():
    name = welcome_user()
    print(constants.INTRO_CALC)
    result = True
    for i in range(constants.NUMBER_OF_QUESTIONS):
        if not result:
            break
        a = random.randint(constants.MIN_NUM_CALC_1, constants.MAX_NUM_CALC_1)
        b = random.randint(constants.MIN_NUM_CALC_2, constants.MAX_NUM_CALC_2)
        j = random.randint(0, len(constants.MATH_OPERATORS) - 1)
        question = f"{a} {constants.MATH_OPERATORS[j]} {b}"
        correct_answer = f"""\
{eval(str(a) + constants.MATH_OPERATORS[j] + str(b))}"""
        result = run_game(question, correct_answer, i,
                          constants.NUMBER_OF_QUESTIONS, name)
