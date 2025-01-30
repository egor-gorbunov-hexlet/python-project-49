from brain_games.cli import welcome_user
from brain_games.games.engine import (
    a,
    answer,
    congratulations,
    correct,
    wrong,
)
from brain_games.scripts.brain_games import greet


def brain_gcd():
    name = welcome_user('name')
    print('What number is missing in the progression?')
    
    for i in range(0, 3):
        a1 = a()  # Первый член прогрессии
        d = a()  # Шаг прогрессии
        n = 10  # Длина прогрессии
        progression = [a1]  # Создаём список с первым членом прогрессии
        for j in range(1, n):
            member = a1 + j * d  # Вычисляем j-ый член прогрессии
            progression.append(member)  # Добавляем его в список
        
        x = a()
        progression[x] = '..'
        result = a1 + x * d
        
        line = ''
        for k in range(len(progression) - 1):
            line += str(progression[k]) + ' ' 

        print(f'Question: {line}')
        
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
