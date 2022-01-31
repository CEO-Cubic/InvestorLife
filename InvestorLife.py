

import os
from os import name
from pickle import NONE
from datetime import timedelta, date
import random
def clear(): os.system('cls')


class Game:
    def __init__(self):
        self.date = date.today()
        life = random.choice(range(365, 465))
        self.endDate = self.date + timedelta(days=life)
        self.err = ""

    def addDay(self, days):
        self.date += timedelta(days=days)
        for x in range(days):
            person.recalcInvest()

    def printGame(self):
        print("Date: {}".format(self.date.strftime("%B %d, %Y")))
        print("Cash: {} | Invested: {}".format(
            format(person.cash, '.2f'), format(person.investedCash, '.2f')))

    def printErr(self):
        print("\n{}".format(game.err))
        game.err = ""


class Person:
    def __init__(self, name):
        self.name = name
        self.job = NONE
        self.cash = 0
        self.investedCash = 0

    def recalcInvest(self):
        self.investedCash *= random.uniform(0.97, 1.035)

    def printActivities(self):
        print("\nGo to:")
        print(" W - go to work(7 days, {} USD)".format(format(job.salary, '.2f')))
        print(" S - school(31 days, cost: 200USD, new salary {} USD)".format(format(job.salary*1.2, '.2f')))
        print(" I - invest money")
        print(" T - transfer invested money to bank")

class Job:
    def __init__(self):
        self.name = name
        self.salary = 100


game = Game()
person = Person(input("Enter your nickname: "))
job = Job()
while game.date < game.endDate:
    clear()
    game.printGame()
    person.printActivities()
    game.printErr()
    choice = input("Your choice? ")
    choice = choice.upper()
    if choice == "W":
        person.cash += job.salary
        game.addDay(7)

    if choice == "S":
        if person.cash < 200:
            game.err = "Not enough funds!"
            continue
        else:
            person.cash -= 200
            job.salary *= 1.2
            game.addDay(31)

    if choice == "I":
        invest = input("How much do you want to invest?['a' = all] ")
        if invest == "a":
            invest = person.cash
        else:
            try:
                invest = float(invest)
            except:
                game.err = "Wrong input!"
                continue
        if invest > person.cash:
            game.err = "Not enough funds!"
            continue
        else:
            person.investedCash += invest
            person.cash -= invest

    if choice == "T":
        invest = input("How much do you want to transfer?['a' = all] ")
        if invest == "a":
            invest = person.investedCash
        else:
            try:
                invest = float(invest)
            except:
                game.err = "Wrong input!"
                continue
        if invest > person.investedCash:
            game.err = "Not enough funds!"
            continue
        else:
            person.cash += invest
            person.investedCash -= invest

clear()
game.printGame()
print("\nGame over!")
print("Net worth: {}".format(person.cash+person.investedCash))
input("Press enter to exit")
