import random

import prompt


def a():
    expr1 = random.randint(1, 10)
    return expr1


def b():
    expr2 = random.randint(1, 10)
    return expr2


def congratulations(name):
    congratulations = print(f'Congratulations, {name}!')
    return congratulations


def wrong(otvet, result, name):
    print(
        f'{otvet} is wrong answer ;(. Correct answer was {result}.\n'
        f'Let\'s try again, {name}!'
        )
        

def correct():
    print('Correct!')
    

def answer():
    otvet = prompt.string("Your answer: ")
    return otvet
