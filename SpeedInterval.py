import sys

class SpeedInterval:
    def __init__(self, speed, miles, minutes):
        self.speed = speed
        self.miles = miles
        self.minutes = minutes
    
    def IsValid(self):
        # knh todo check that minutes are whole
        # check that miles are even thenths
        pass

    def printMe(self):
        try:
            sys.stdout.write(str(self.speed) + " " + str(self.miles) + " " + str(self.minutes) + "\r\n")
        except:
            pass