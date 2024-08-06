"""

Each team has 4 players

a player at bat has to coose a number 1-50
a random number gets selected
if within 18, its a hit, 13 double, 8, triple, 3 home run
set player to corresponding base obj and add to record

CLASS 1: PLAYER:
  hit
  occupy bases
  RBIs
  hit record for game
  pitching fatigue

CLASS 2: GAME:
  change inning / keep track of outs
  keep track of team scores
  keep track of a pitching fatigue and higher chances of hitting by lowering 1-50??  Pitcher will change after -15 chance

on inning change player can pitch
have them pick a number 1-50 and have CPU gen number with same hitting logic
can change pitcher

ask player to pick either mariners or guardians
ask if they want to pick different teams
display the player of the team they chose
ask for home or away

(picks away and Mariners)

GAMEPLAY LOOP
"Top of the first inning! No outs. The score is Mariners 0, Guardians 0."
tell player which player is currently hitting

ask for a number 1-50 and analyze the number against a random number and assign hit value to a player

set up team obj with players and save user input to team name somehow
addplayer method and removeplayer method


"""

from random import random, randint
from Game import Game
from Player import Player
from Team import Team

    #write game methods that handle pitching and hitting
    #such as:
    #guessing a number for hitting and comparing it to a generated number

      

#
#
#       GAME                                GAME                                 GAME
#      STARTS                              STARTS                               STARTS
#
#
#


welcomeStatement = """
\n\nHello and welcome to Python Baseball 0.1!\n
In this game you will choose two teams (or use the game standard) and select your own players for said teams.\n
From there the game will start. \n\n

For ease of tutorial, say you picked away.  \n
You will be prompted to pick a number 1-100 and the CPU will also generate a number 1-50.\n
If your number is within 18 of the CPU number, its a single, within 13 a double, within 8 a triple, if you manage to get it within 3 that will be a home run.\n
Anything outside of that range will be a strike but there will be a small chance it could be ball.  3 strikes you're out and 3 outs inning changes.\n\n

Now, you are pitching.\n
To pitch is very similar to hitting, however, this time the roles reverse.  You will be providing a number and the CPU is trying to get close to your number.\n
Same rules apply to the CPU for hitting as did for you.  (The CPU might adjust its guess ranges if you give numbers too close together back-to-back)
"""
print(welcomeStatement)

#team name generation and user input

#if the user picked their own team names, ask them to choose their own player names as well
#if the user did not pick their own team names, give them the standard Mariners v Guardians

done = False
while not done:
    try:
        choice = input("Do you want to pick team names? Y/N: ")
        if choice == 'Y':
            #set team names and rosters to user input
            homeTeamName = input("Pick a name for the home team: ")
            homeTeam = Team(str(homeTeamName))
            inputName1 = ""
            for i in range(4):
                inputName1 = input(f"Team 1, Player {i+1} name: ")
                homeTeam.addPlayer(Player(inputName1))

            inputName2 = ""
            awayTeamName = input("Pick a name for the away team: ")
            awayTeam = Team(str(awayTeamName))
            for n in range(4):
                inputName2 = input(f"Team 2, Player {n+1} name: ")
                awayTeam.addPlayer(Player(inputName2))

            done = True

        elif choice == 'N':
            #set team names and roster to standard
            homeTeamName = "Seattle Mariners"
            homeTeam = Team(str(homeTeamName))
            #print(homeTeam.getTeamName())  --- PRINTS TEAM NAME
            homeTeam.addPlayer(Player("Ty France"))
            homeTeam.addPlayer(Player("Julio Rodriguez"))
            homeTeam.addPlayer(Player("JP Crawford"))
            homeTeam.addPlayer(Player("Cal Raleigh"))

            awayTeamName = "Cleveland Guardians"
            awayTeam = Team(str(awayTeamName))
            #print(awayTeam.getTeamName())  --- PRINTS TEAM NAME
            awayTeam.addPlayer(Player("Bo Naylor"))
            awayTeam.addPlayer(Player("Jose Ramirez"))
            awayTeam.addPlayer(Player("Steven Kwan"))
            awayTeam.addPlayer(Player("Tyler Freeman"))
            done = True

        else:
            print("Invalid choice. Try again.\n")
    except EOFError:
        print("Error reading input. Please try again.\n")
    


awayTeam.printRoster()
homeTeam.printRoster()

print("\nGame is ready to start.\n")

game = Game(awayTeam, homeTeam)
#how do we want to store inning data and score.  do we want to be able to track inning by inning score?
#if so we could use a dictionary per team and use the inning number as the key that points to the value, score, of said inning.
#this would make custom inning length easy too.  we could store this dictionary in the teamScore we have in the Team obj alr.
#
#
#
"""
while done != True:
    userChoice = input("Do you want to be Home, or Away? H/A: ")

    if userChoice == 'H':
        isHome = True
        done = True

    elif userChoice == 'A':
        isHome = False
        done = True

    else:
        print("User choice invalid. Try again.")
        
        
#code for handling home vs away selection
#scrapped for now
done = False
while not done:
    try:
        choice = input("Do you want to be Home or Away? H/A: ")
        if choice == 'H':
            isHome = True
            done = True

        elif choice == 'A':
            isHome = False
            done = True

        else:
            print("User choice invalid. Try again.")
        
    except EOFError:
        print("Error reading input. Please try again.")
"""

#start game with asking who to have pitch first since user is home
print("Since you are home, you are now pitching. Who would you like to pitch? \n")

currentUserPitcher = homeTeam.getNewUserPitcher()  #<-- this method to returns the object(player)that the user selects
print(currentUserPitcher)

while game.inningNumber <= 9:
        print(f"\n--- Inning {game.inningNumber} ---")
        game.hitting(awayTeam, homeTeam)
        if game.outs < 3:
            game.pitching(homeTeam, awayTeam)
        game.inningNumber += 1
        game.outs = 0  # Reset outs for the next inning




