import time
import sys

class TimeService:
    def __init__(self, scaleFactor):
        self.scaleFactor = scaleFactor
        # initlize the clock, each subsquent call will return the seconds
        # scense this call
        time.clock()

    def CurrentTime(self):
        # get seconds from start
        # multiply seconds by scale factor
        # add scaled seconds to start to get scalled time
        # return it
        actualSeconds = time.clock()
        return actualSeconds * self.scaleFactor

