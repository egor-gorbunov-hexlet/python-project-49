from brain_games.cli import welcome_user
from brain_games.games.engine import (
    a,
    answer,
    b,
    congratulations,
    correct,
    wrong,
)
from brain_games.scripts.brain_games import greet


def brain_gcd():
    name = welcome_user('name')
    print('Find the greatest common divisor of given numbers.')
    
    for i in range(0, 3):
        x = a()
        y = b()
        if abs(x) <= abs(y):
            z = x
        if abs(y) < abs(x):
            z = y

        for j in range(z, 0, -1):
            if x % j == 0 and y % j == 0:
                # print(j)
                result = j
                break
            j = j - 1
            
        print(f'Question: {x} {y}')
        
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
    brain_gcd()


if __name__ == "__main__":
    main()
