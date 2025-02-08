import random

from brain_games.cli import welcome_user
from brain_games.scripts.brain_games import greet
from brain_games.scripts.games.engine import (
    a,
    answer,
    b,
    congratulations,
    correct,
    wrong,
)


def brain_calc():
    name = welcome_user('name')
    print('What is the result of the expression?')
    for i in range(0, 3):
        rand_expression = random.choice(['+', '-', '*'])
        x = a()
        y = b()
        result = eval(f'{x} {rand_expression} {y}')
        print(f'Question: {x} {rand_expression} {y}')
        
        otvet = answer()
        if str(result) == otvet:
            correct()
        else:
            wrong(otvet, result, name)
            break
        if i == 2:
            congratulations(name)


def main():
    greet()
    brain_calc()


if __name__ == "__main__":
    main()
