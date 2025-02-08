from brain_games.cli import welcome_user
from brain_games.scripts.brain_games import greet
from brain_games.scripts.games.engine import (
    a,
    answer,
    congratulations,
    correct,
    wrong,
)


def brain_prime():
    name = welcome_user('name')
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    
    for i in range(0, 3):
        a1 = a()
        if (a1 % 2 == 0 or a1 % 3 == 0 or a1 == 1) and a1 != 2 and a1 != 3:
            print("Not a prime number")
            result = "no"
        else:
            print("Prime number")
            result = "yes"

        print(f'Question: {a1}')
        
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
    brain_prime()


if __name__ == "__main__":
    main()
