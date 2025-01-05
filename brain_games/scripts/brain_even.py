import random
    
import prompt

from brain_games.cli import welcome_user
from brain_games.scripts.brain_games import greet


def brain_even():
    print('Answer "yes" if the number is even, otherwise answer "no".')
    name = welcome_user()
    for i in range(0, 3):
        a = random.randint(1, 9999)
        print("Question:" + str(a))
        otvet = prompt.string("Your answer: ")
        if a % 2 == 0 and otvet == "yes":
            print("Correct!")
        elif a % 2 == 0 and otvet != "yes":
            print(
                otvet + " is wrong answer ;(. Correct answer was 'yes' \n"
                "Let's try again, " + name + "!"
            )
            break
        elif a % 2 != 0 and otvet != "no":
            print(
                otvet + " is wrong answer ;(. Correct answer was 'no' \n"
                "Let's try again, " + name + "!"
            )
            break
        elif a % 2 != 0 and otvet == "no":
            print("Correct!")
        if i == 2:
            print("Congratulations, " + name + "!")


def main():
    greet()
    brain_even()


if __name__ == "__main__":
    main()
