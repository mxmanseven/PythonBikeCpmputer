import time
import sys

class TimeService:
    def __init__(self, scaleFactor):
        self.scaleFactor = scaleFactor
        # initlize the clock, each subsquent call will return the seconds
        # scense this call
        self.initialTime =  time.clock()
        sys.stdout.write("TimeService.Init: " + str(self.initialTime) + "\n")
        sys.stdout.write("TimeService.scaleFactor: " + str(self.scaleFactor) + "\n")

    def CurrentTime(self):
        # get seconds from start
        # multiply seconds by scale factor
        # add scaled seconds to start to get scalled time
        # return it
        actualSeconds = time.clock() - self.initialTime
        return (actualSeconds * self.scaleFactor) * 10
        
    def ResetTime(self):
        self.initialTime = time.clock()