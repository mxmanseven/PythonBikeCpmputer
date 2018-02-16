

from TimeService import TimeService


class WheelManager:
    # Manages wheel ticks and distance
    # keeps all valid wheel ticks
    # keeps running average of speed over last minute
    # keeps current speed

    def __init__(self, wheelCircumference, timeScaleFactor=1):
        self.wheelCircumference = wheelCircumference
        self.timeService = TimeService(timeScaleFactor)
        self.validTickCount = 0
        self.validTicks = []

    def getCurrentSpeed(self):
        pass
    
    def getAverageSpeed(self):
        pass

    def getTotalDistance(self):
        return  self.validTickCount * self.wheelCircumference  

    def newRawTick(self):
        # knh todo - check for tick bounce
        # if this time is too close to the previous then reject it
        # at a 6 ft circumfrance @ 15 hz => 68mph =>0.066 seconds between ticks
        currentTime = self.timeService.CurrentTime()
        lastTickTime = 0
        if(self.validTickCount > 0):
            lastTickTime = self.validTicks[self.validTickCount - 1]
        timeFromLastTick = currentTime - lastTickTime
        if(timeFromLastTick > 0.050):
            self.validTicks.append(currentTime)
            self.validTickCount += 1