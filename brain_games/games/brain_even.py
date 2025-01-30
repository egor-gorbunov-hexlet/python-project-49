
from brain_games.cli import welcome_user
from brain_games.games.engine import a, answer, congratulations, correct, wrong
from brain_games.scripts.brain_games import greet


def brain_even():
    print('Answer "yes" if the number is even, otherwise answer "no".')
    name = welcome_user('name')
    for i in range(0, 3):
        x = a()
        print(f'Question: {x}')
        otvet = answer()
        result = "yes"
        if x % 2 == 0 and otvet == result:
            correct()
        elif x % 2 == 0 and otvet != result:
            wrong(otvet, result, name)
            break 
        result = "no"
        if x % 2 != 0 and otvet == result:
            correct()
        elif x % 2 != 0 and otvet != result:
            wrong(otvet, result, name)
            break
        if i == 2:
            congratulations(name)


def main():
    greet()
    brain_even()


if __name__ == "__main__":
    main()
