# holds a collection of route objects
import sys
from RouteTypes import RouteType
from RouteEntry import RouteEntry
from SpeedInterval import SpeedInterval

class Route:
    Routes = []
    Possibles = []
    SpeedIntervals = []
    
    def __init__(self):
        self.Routes = []
        self.Possibles = []
        self.SpeedIntervals = []
        self.MaxSpeed = 100
        self.buildIntervalTable(self.MaxSpeed)

    def AddSpeed(self, startMile, speed):
        # Add Speed route with start mile and new speed
        endMile = None
        self.Routes.append(RouteEntry(startMile, endMile, speed, RouteType.SpeedChange))
        
    def AddReset(self, startMile, endMile):
        # add a reset to the route with start mile and end mile
        speed = None
        self.Routes.append(RouteEntry(startMile, endMile, speed, RouteType.MiliageReset))

    def CalculatePossibles(self):
        # Builds a set of all possiables for all speeds and resets
        # reset Possibles
        # for each speed, look up distance and minute interval 
        # add possibles while mile is less than next rout start mile
        #knh todo - how should resets be hanled? Mybe they already are?
        self.Possibles = []
        i = 0
        while i < len(self.Routes):
            re = self.Routes[i]
            if i + 1 < len(self.Routes):
                next = self.Routes[i+1]
            else:                
                # knh tood check if last route is a 
                # knownControl or EndBy.
                # for now, just add 10 miles to last route
                next = RouteEntry(re.startMile + 10, None, None, None)
            # Add Possibles
            # for speed entries, get interval
            # to add possiables
            if(re.routeType == RouteType.SpeedChange):
                endMile = next.startMile
                startMile = re.startMile
                interval = self.getIntervalBySpeed(re.speed)
                minute = 0
                mile = startMile
                while mile < endMile:
                    mile = round(mile + interval.miles, 1)
                    #how do we deal with start mile?
                    minute += interval.minutes
                    p = SpeedInterval(re.speed, mile, minute)
                    self.Possibles.append(p)
            if re.routeType == RouteType.MiliageReset:
                # knh todo - what is the time we shold arrive at the end mile at?
                # I think it is the same as the start time
                r = SpeedInterval(None, re.startMile, re.endMile)
                self.Possibles.append(r)
            i += 1

    def getPaceSecondsFromPossableAndMile(self, mile, minute):
        # When you are behind or slow, pace is negative.
        # When you are early / fase, pace is positive.
        # given the current mile, get the next possable
        # for the speed find determine what the ontime minute is
        # return the dirrerence of the ontime minute and the actual minute
        i = 0
        nextPossible = None
        for p in self.Possibles:
            i += 1
            nextPossible = p
            if p.miles >= mile:
                break
        lastPossable = self.Possibles[i-1]
        milesPastLastPossable = mile - lastPossable.miles
        expectedMinute = (((milesPastLastPossable / lastPossable.speed) * 60) 
            + lastPossable.minutes)
        minutesFromPace = minute - expectedMinute
        return minutesFromPace * 60

    def printPossables(self):
        for p in self.Possibles:
            p.printMe()

    def  getIntervalBySpeed(self, speed):
        # Given a speed, finds the possable interval:
        # Distance must be evenaly divisable by 0.1
        # Minute must be whole
        # looks the mile and minute interval by current speed
        if isinstance(speed, (long, int)):
            return self.SpeedIntervals[speed - 1]
        if speed > self.MaxSpeed:
            return "getInterValBySpeed() failed: speed >" + str(speed) + "< cannot be greater than MaxSpeed."
        return None

    def buildIntervalTable(self, maxSpeed):
        # build a list of intervals from 1 to maxSpeed, speed is the index 
        # A valid interval has milage with a whole tenth and a whole minute
        sys.stdout.write('Route::buildIntervalTable()')
        self.SpeedIntervals = []
        for speed in range(1, maxSpeed):
            si = self.getInterval(speed)
            if(si != None):
                self.SpeedIntervals.append(si)                
    
    def getInterval(self, speed):
        try:
            sys.stdout.write('Route::getInterval()\r\n')
            for i in range(1, 100):
                distance = i / 10.0
                timeHours = distance / speed
                timeMinutes = timeHours * 60
                if timeMinutes % 1 < 0.000001:
                    si = SpeedInterval(speed, distance, int(round(timeMinutes)))
                    si.printMe()
                    return si
        except:
            return None
    



    