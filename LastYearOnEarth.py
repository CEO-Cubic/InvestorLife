

from mimetypes import init
import os
from datetime import timedelta, date
import random
from tkinter import NONE
import time
import sys
import keyboard


class Game:
    moneyGoal = 15000

    def __init__(self):
        self.date = date.today()
        life = random.choice(range(385, 420))
        self.endDate = self.date + timedelta(days=life)
        self.announcedFlightDate = self.date + timedelta(days=280)
        self.err = ""

    def isActive(self):
        if self.date < self.endDate:
            return 1
        return 0

    def clear(self):
        os.system('cls')

    def printPreGame(self):
        text = "It is "+str(self.date.strftime("%B %d, %Y"))+" and scientists announced, that Earth is gonna be uninhabitable due the global warming approximately in 1 year. There is one solution... Mars. Elon Musk announced, SpaceX is ready to trasport whole civilization to Mars. Ticket costs " + \
            str(self.moneyGoal) + \
            " USD per person. You are young homeless boi living under the bridge. Can you survive?"
        self.printWithDelay(text)
        input("\n\npress enter")

    def addDay(self, days):
        self.date += timedelta(days=days)
        for x in range(days):
            person.recalcInvest()

    def printGameProgress(self):
        print("Date: {}".format(self.date.strftime("%B %d, %Y")))
        print("Cash: {} USD | Invested: {} USD".format(
            format(person.cash, '.2f'), format(person.investedCash, '.2f')))
        print()

    def printErr(self):
        print("\n{}".format(game.err))
        game.err = ""

    def printGameOver(self, cash):
        text = "\nGame over!\nNet worth: " + format(cash, '.2f')+" USD\n"
        game.printWithDelay(text)
        if cash >= self.moneyGoal:
            text = "You won! Enjoy your flight!\n"
        else:
            text = "You lost! You have been fried!\n"
        game.printWithDelay(text)
        input("Press enter to exit")

    def printWithDelay(self, text):
        for char in text:
            print(char, end="")
            time.sleep(0.06)
            sys.stdout.flush()
            if keyboard.is_pressed("Enter"):
                game.clear()
                print(text)
                return

    def announcedFlight(self):
        self.timesShowed = 0
        if self.timesShowed < 6 and self.announcedFlightDate < self.date:
            print("News: Last flight is going to be at {}".format(
                game.endDate.strftime("%B %d, %Y")))
            self.timesShowed += 1


class Person:
    def __init__(self, name):
        self.name = name
        self.job = NONE
        self.cash = 0
        self.investedCash = 0

    def recalcInvest(self):
        self.investedCash *= random.uniform(0.98, 1.026)

    def printActivities(self):
        print("\nGo to:")
        print(" W - go to work(7 days, {} USD)".format(format(job.salary, '.2f')))
        print(" S - school(31 days, cost: 200USD, new salary {} USD)".format(format(job.salary*1.3, '.2f')))
        print(" I - invest money")
        print(" T - transfer invested money to bank")

    def doActivity(self):
        choice = input("Your choice? ")
        choice = choice.upper()
        if choice == "W":
            person.cash += job.salary
            game.addDay(7)

        if choice == "S":
            if person.cash < 200:
                game.err = "Not enough funds!"
                return
            else:
                person.cash -= 200
                job.salary *= 1.3
                game.addDay(31)

        if choice == "I":
            invest = input(
                "How much do you want to invest?[empty line = all] ")
            if invest == "":
                invest = person.cash
            else:
                try:
                    invest = float(invest)
                except:
                    game.err = "Wrong input!"
                    return
            if invest > person.cash:
                game.err = "Not enough funds!"
                return
            else:
                person.investedCash += invest
                person.cash -= invest

        if choice == "T":
            invest = input(
                "How much do you want to transfer?[empty line = all] ")
            if invest == "":
                invest = person.investedCash
            else:
                try:
                    invest = float(invest)
                except:
                    game.err = "Wrong input!"
                    return
            if invest > person.investedCash:
                game.err = "Not enough funds!"
                return
            else:
                person.cash += invest
                person.investedCash -= invest


class Job:
    def __init__(self, name):
        self.name = name
        self.salary = 100


game = Game()
job = Job("job")
person = Person(input("Enter your nickname: "))
game.printPreGame()

while game.isActive():

    game.clear()
    game.printGameProgress()
    game.announcedFlight()
    person.printActivities()
    game.printErr()
    person.doActivity()

game.clear()
game.printGameProgress()
game.printGameOver(person.cash+person.investedCash)