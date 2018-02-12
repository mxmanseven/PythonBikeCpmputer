# holds a collection of route objects

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
        self.buildIntervalTable(100)

    def AddSpeed(self, startMile, speed):
        endMile = None
        self.Routes.append(RouteEntry(startMile, endMile, speed, RouteType.SpeedChange))
        
    def AddReset(self, startMile, endMile):
        speed = None
        self.Routes.append(RouteEntry(startMile, endMile, speed, RouteType.MiliageReset))

    def CalculatePossibles(self):
        # reset Possibles
        # for each speed, look up distance and minute interval 
        # add possibles while mile is less than next rout start mile
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
                next = self.Routes[i]
                next.endMile += 10
            # Add Possibles
            # for speed entries, get interval
            # to add possiables
            if(re.routeType == RouteType.SpeedChange):
                pass

    def  getIntervalBySpeed(self, speed):
        pass

    def buildIntervalTable(self, maxSpeed):
        self.SpeedIntervals = []
        for speed in range(1, maxSpeed):
            si = self.getInterval(speed)
            if(si != None):
                self.SpeedIntervals.append(si)

                
    
    def getInterval(self, speed):
        for i in range(1, 100):
            distance = i / 10.0
            timeHours = distance / speed
            timeMinutes = timeHours * 60
            if timeMinutes % 1 < 0.000001:
                # knh todo - round to whole minute
                si = SpeedInterval(speed, distance, timeMinutes)
                si.printMe()
                return si
        return None
    



    