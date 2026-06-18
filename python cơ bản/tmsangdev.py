import random

pi = 3.14
big_six_teams = ["Manchester City", "Manchester United","Liverpool", "Arsenal", "Chelsea"]



def roll_dice(number):
    return random.randint(1, number)

phone_book = open("index.html", "w", encoding="utf-8")
phone_book.write("<p>Hello, world <p>")
