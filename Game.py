from random import random, randint
from Team import Team

class Game:
    def __init__(self, awayTeam, homeTeam):
        self.inningNumber = 1
        self.awayTeam = awayTeam
        self.homeTeam = homeTeam
        self.strikes = 0
        self.balls = 0
        self.outs = 0
        self.scores = {self.awayTeam: 0, self.homeTeam: 0}
        self.bases = [None, None, None]  # Represent the bases: [first base, second base, third base]

    def __repr__(self):
        return f"The game is currently in inning #{self.inningNumber} and the score is {self.homeTeam} {self.scores[self.homeTeam]}, and the {self.awayTeam} {self.scores[self.awayTeam]}"

    def hitting(self, teamHitting, teamPitching):
        print(f"Now batting, the {teamHitting.getTeamName()}.")
        self.strikes = 0
        self.balls = 0

        while self.outs < 3:
            print(f"{teamHitting.players[teamHitting.currentBatter].getName()} at the plate.")
            stillHitting = True
            while stillHitting:
                player = teamHitting.players[teamHitting.currentBatter]
                result = self.at_bat(player, teamHitting)
                if result == 'strike':
                    self.strikes += 1
                    print(f"Strike {self.strikes}!")
                    if self.strikes >= 3:
                        self.outs += 1
                        self.strikes = 0
                        self.balls = 0
                        print(f"{player.getName()} is out!")
                        stillHitting = False
                elif result == 'ball':
                    self.balls += 1
                    print(f"Ball {self.balls}.")
                    if self.balls >= 4:
                        print(f"{player.getName()} walked!")
                        self.advanceRunners(1, teamHitting)
                        self.balls = 0
                        self.strikes = 0
                else:
                    self.strikes = 0
                    self.balls = 0
                    if result == 'single':
                        print(f"{player.getName()} hit a single!")
                        self.advanceRunners(1, teamHitting)
                    elif result == 'double':
                        print(f"{player.getName()} hit a double!")
                        self.advanceRunners(2, teamHitting)
                    elif result == 'triple':
                        print(f"{player.getName()} hit a triple!")
                        self.advanceRunners(3, teamHitting)
                    elif result == 'home run':
                        print(f"{player.getName()} hit a home run!")
                        self.advanceRunners(4, teamHitting)
                    stillHitting = False
            teamHitting.currentBatter = (teamHitting.currentBatter + 1) % len(teamHitting.players)
            if self.outs >= 3:
                break

    def at_bat(self, player, teamHitting):
        cpu_number = randint(1, 100)
        player_guess = teamHitting.getUserGuess()
        difference = abs(cpu_number - player_guess)
        if difference <= 3:
            return 'home run'
        elif difference <= 8:
            return 'triple'
        elif difference <= 13:
            return 'double'
        elif difference <= 18:
            return 'single'
        else:
            if random() < 0.2:
                print("Ball!")
                return 'ball'
            else:
                return 'strike'

    def pitching(self, teamPitching, teamHitting):
        print(f"Now pitching, the {teamPitching.getTeamName()}.")
        self.strikes = 0
        while self.outs < 3:
            pitcher = teamPitching.getNewUserPitcher()
            cpu_guess = randint(1, 100)
            player_number = teamHitting.getUserGuess()
            difference = abs(cpu_guess - player_number)
            pitcher.pitchingFatigue -= 1
            if difference <= 3:
                print(f"The CPU hit a home run off {pitcher.getName()}!")
                self.advanceRunners(4, teamHitting, isCPU=True)
            elif difference <= 8:
                print(f"The CPU hit a triple off {pitcher.getName()}!")
                self.advanceRunners(3, teamHitting, isCPU=True)
            elif difference <= 13:
                print(f"The CPU hit a double off {pitcher.getName()}!")
                self.advanceRunners(2, teamHitting, isCPU=True)
            elif difference <= 18:
                print(f"The CPU hit a single off {pitcher.getName()}!")
                self.advanceRunners(1, teamHitting, isCPU=True)
            else:
                self.strikes += 1
                if self.strikes >= 3:
                    self.outs += 1
                    self.strikes = 0
                    print(f"{pitcher.getName()} struck out the batter!")
            if self.outs >= 3:
                break

    def updateScore(self, team, runs):
        self.scores[team] += runs
        print(f"The score is now {team.teamName} {self.scores[team]}.")

    def advanceRunners(self, basesToAdvance, teamHitting=None, isCPU=False):
        # Move runners according to the number of bases advanced
        for i in range(2, -1, -1):  # Iterate from third base to first base
            if self.bases[i] is not None:
                newBase = i + basesToAdvance
                if newBase >= 3:
                    self.updateScore(self.bases[i].team, 1)  # Score a run if the player crosses home plate
                    self.bases[i].currentBase = 0
                    self.bases[i] = None  # The player has scored, so remove them from the base
                else:
                    self.bases[newBase] = self.bases[i]  # Move the player to the new base
                    self.bases[i].currentBase = newBase + 1
                    self.bases[i] = None

        if not isCPU:
            # Place the current batter on the appropriate base
            if basesToAdvance <= 3:
                self.bases[basesToAdvance - 1] = teamHitting.players[teamHitting.currentBatter]
                teamHitting.players[teamHitting.currentBatter].currentBase = basesToAdvance

    def endInning(self):
        self.outs = 0
        self.inningNumber += 1
        print(f"Inning #{self.inningNumber} begins")