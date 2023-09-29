import prompt


def game(question, correct_answer, i, number_of_questions, name):
    print(f"Question: {question}")
    answer = prompt.string("You answer: ")
    if answer == correct_answer:
        print("Correct!")
        if i == number_of_questions - 1:
            print(f"Congratulations, {name}!")
    else:
        print(f"""'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.
Let's try again, {name}!""")
        return False
