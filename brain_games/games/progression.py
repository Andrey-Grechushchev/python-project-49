import random
from brain_games.games.game import game
from brain_games.welcome_user import welcome_user


def progression():
    how_to_answer = "What number is missing in the progression?"
    number_of_question = 3
    name = welcome_user()
    print(how_to_answer)
    result = True
    for i in range(number_of_question):
        if result is False:
            break
        progression_len = random.randint(5, 10)
        iter_value = random.randint(2, 7)
        first_value = random.randint(1, 20)
        empty_space_position = random.randint(0, progression_len - 1)
        list_of_num = [(first_value + iter_value * i) for i in range(progression_len)]
        correct_answer = f"{list_of_num[empty_space_position]}"
        question = ""
        for j in list_of_num:
            if list_of_num.index(j) == empty_space_position:
                j = ".."
            question += f"{str(j)} "
        result = game(question, correct_answer, i, number_of_question, name)
