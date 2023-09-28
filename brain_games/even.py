import random
import prompt


def even():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print('Answer "yes" if the number is even, otherwise answer "no".')
    number_of_questions = 3
    for i in range(number_of_questions):
        num = random.randint(1, 100)
        print(f"Question: {num}")
        answer = prompt.string("You answer: ")
        correct_answer = (num % 2 == 0 and "yes" or "no")
        if answer == correct_answer:
            print("Correct!")
            if i == number_of_questions - 1:
                print(f"Congratulations, {name}!")
        else:
            print(f"""'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.
Let's try again, {name}!""")
            break
