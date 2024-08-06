
from random import random, randint
class Team:
    def __init__(self, teamName):
        self.players = []
        self.teamName = teamName
        self.currentBatter = 0
        self.teamScore = 0

    def getTeamName(self):
        return self.teamName

    def addPlayer(self, player):
        player.setTeam(self)
        self.players.append(player)

    def printRoster(self):
        number = 1
        print(f"This is your {self.teamName}:\n")
        for player in self.players:
            print(f"Player #{number}, " + str(player))
            number += 1

    def returnTeamScore(self):
        return self.teamScore

    def getUserGuess(self):
        while True:
            try:
                userHittingGuess = int(input("Pick a number 1-100: "))
                if 1 <= userHittingGuess <= 100:
                    return userHittingGuess
                else:
                    print("Invalid input, please pick a number between 1 and 100.")
            except ValueError:
                print("Invalid input, please enter a valid number.")

    def getNewUserPitcher(self):
        self.printRoster()
        while True:
            try:
                userSelection = int(input(f"Please enter your selection by typing a number between 1 and {len(self.players)}: "))
                if 1 <= userSelection <= len(self.players):
                    selectedPitcher = self.players[userSelection - 1]
                    return selectedPitcher
                else:
                    print(f"Invalid selection, please pick a number between 1 and {len(self.players)}.")
            except ValueError:
                print("Invalid input, please enter a valid number.")
            except IndexError:
                print("Invalid selection, please try again.")
