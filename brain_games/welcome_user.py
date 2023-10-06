import prompt
from brain_games.constants import WELCOME


def welcome_user():
    name = prompt.string(WELCOME)
    print(f'Hello, {name}!')
    return name
