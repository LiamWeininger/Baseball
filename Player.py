from random import random, randint
class Player:
    def __init__(self, name):
        self.name = name
        self.numHits = 0
        self.currentBase = 0  # Add base number
        self.hitRecord = []
        self.pitchingFatigue = 100
    
    def __str__(self):
        return f"Hello, my name is {self.name}. I have {self.numHits} hit(s). My fatigue is at {self.pitchingFatigue}/100.\n"
    
    def addHitRecord(self, nameOfHit):
        self.hitRecord.append(str(nameOfHit))

    def getHitRecord(self):
        return self.hitRecord

    def addHitToPlayerTotal(self, numHits):
        self.numHits += 1
    
    def getName(self):
        return self.name
    
    def getCurrentBase(self):
        return self.currentBase

    def setTeam(self, team):
        self.team = team

