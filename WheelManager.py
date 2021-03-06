

from TimeService import TimeService


class WheelManager:
    # Manages wheel ticks and distance
    # keeps all valid wheel ticks
    # keeps running average of speed over last minute
    # keeps current speed
    # listens on gpio pin 7 for falling edge
    # knh todo - maybe main should be configuring gpio instead.

    def __init__(self, wheelCircumferenceInches, timeService):
        self.wheelCircumferenceInches = wheelCircumferenceInches
        self.timeService = timeService
        self.validTickCount = 0
        # validTicks is an array with the arrival time as the value
        # added in order of arrival.
        # arrival time is based off of the timeService time
        self.validTicks = []
        
    def getSpeed(self, durrationSeconds=2, average=False):
        # Need at least two points of distance and time (ticks) to find speed
        # Need max time window to consider for determining speed
        # Lets look back at the last two seconds for any ticks
        # If there are no ticks in the last two second then speed is zero
        # if theire is one tick in the last two seconds then speed 
        #  is 1 rotation per 2 seconds extended to mph by wheel size
        # if mpre than one tick in last tow seconds, the find speed = d / t
        # durrationSeconds is needed because we get one tick per wheel rev 
        # and for a 21" wheel, one rev each two seconds is about 5 mph
        # when average is trur, will reutrn the average across durrationSeconds
        maxSecondsBack = durrationSeconds
        lastArrivals = self.getLastTicksByTime(maxSecondsBack)
        lastArrivalCount = len(lastArrivals)
        if (lastArrivalCount == 0):
            return 0
        elif (lastArrivalCount == 1):
            #knh todo - do math to find speed at 1 rev per maxSecondsBack
            #  17.6 inch  per second (constant) => 1 mph
            return (float(self.wheelCircumferenceInches) / float(maxSecondsBack)) / 17.6
        elif (lastArrivalCount > 1):
            #knh todo - handle average case
            # get last two arrivals, find time span, find speed
            length = len(lastArrivals)
            last = lastArrivals[length - 1]
            nextLast = lastArrivals[length - 2]
            timeSpanSeconds = abs(last - nextLast)
            return (float(self.wheelCircumferenceInches) / float(timeSpanSeconds)) / 17.6
        return -1
    
    def getLastTicksByTime(self, secondsBack):
        # get the last ticks that are newer than seconds back
        recientTicks = []
        now = self.timeService.CurrentTime()
        minArrivalTime = now - float(secondsBack)
        # start at the end then work back
        i = self.validTickCount - 1
        keepLooking = True
        if i < 0:
            keepLooking = False

        while (keepLooking):
            arrival = self.validTicks[i]
            if (arrival > minArrivalTime):
                recientTicks.append(arrival)
            else:
                keepLooking = False
            if (i == 0): keepLooking = False
            i -= 1
        return recientTicks

    def getTotalDistance(self):
        # knh todo - keep track of both ground miles and route miles 
        #63,360 inchs per Mile
        return  (float(self.validTickCount) * float(self.wheelCircumferenceInches)) / 63360

    def newRawTick(self, chan):
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
