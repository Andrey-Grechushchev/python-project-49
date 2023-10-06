import random
from brain_games import constants
from brain_games.game import run_game
from brain_games.welcome_user import welcome_user


def prime():
    name = welcome_user()
    print(constants.INTRO_PRIME)
    result = True
    for i in range(constants.NUMBER_OF_QUESTIONS):
        if not result:
            break
        question = random.randint(constants.MIN_NUM_PRIME,
                                  constants.MAX_NUM_PRIME)
        is_prime = True
        for j in range(2, question // 2 + 1):
            is_prime *= question % j != 0
            if not is_prime:
                break
        correct_answer = is_prime and "yes" or "no"
        result = run_game(question, correct_answer, i,
                          constants.NUMBER_OF_QUESTIONS, name)
