import random
from brain_games import constants
from brain_games.game import run_game
from brain_games.welcome_user import welcome_user


def progression():
    name = welcome_user()
    print(constants.INTRO_PROGRESSION)
    result = True
    for i in range(constants.NUMBER_OF_QUESTIONS):
        if not result:
            break
        progression_len = random.randint(constants.MIN_PROGRESSION_LEN,
                                         constants.MAX_PROGRESSION_LEN)
        iter_value = random.randint(constants.MIN_ITER_VALUE,
                                    constants.MAX_ITER_VALUE)
        first_value = random.randint(constants.MIN_FIRST_VALUE,
                                     constants.MAX_FIRST_VALUE)
        empty_space_position = random.randint(constants.MIN_EMPTY_POSITION,
                                              progression_len - 1)
        list_of_num = [(first_value + iter_value * i)
                       for i in range(progression_len)]
        correct_answer = f"{list_of_num[empty_space_position]}"
        question = ""
        for j in list_of_num:
            if list_of_num.index(j) == empty_space_position:
                j = ".."
            question += f"{str(j)} "
        result = run_game(question, correct_answer, i,
                          constants.NUMBER_OF_QUESTIONS, name)
