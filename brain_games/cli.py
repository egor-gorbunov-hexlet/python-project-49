import prompt


def welcome_user(name):
    name = prompt.string("May I have your name? ")
    print("Hello, " + name + "!")
    return name
