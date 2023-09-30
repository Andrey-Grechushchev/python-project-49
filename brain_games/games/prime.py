import random
from brain_games.games.game import game
from brain_games.welcome_user import welcome_user


def prime():
    how_to_answer = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    number_of_question = 3
    name = welcome_user()
    print(how_to_answer)
    result = True
    for i in range(number_of_question):
        if result is False:
            break
        question = random.randint(1, 100)
        prime = True
        for j in range(2, question // 2 + 1):
            prime *= question % j != 0
            if not prime:
                break
        correct_answer = prime and "yes" or "no"
        result = game(question, correct_answer, i, number_of_question, name)
