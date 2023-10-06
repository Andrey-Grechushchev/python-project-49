import random
from brain_games import constants
from brain_games.game import run_game
from brain_games.welcome_user import welcome_user


def even():
    name = welcome_user()
    print(constants.INTRO_EVEN)
    result = True
    for i in range(constants.NUMBER_OF_QUESTIONS):
        if not result:
            break
        question = random.randint(constants.MIN_NUM_EVEN,
                                  constants.MAX_NUM_EVEN)
        correct_answer = question % 2 == 0 and "yes" or "no"
        result = run_game(question, correct_answer, i,
                          constants.NUMBER_OF_QUESTIONS, name)
