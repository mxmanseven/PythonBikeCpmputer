
import sys

class EnduroScreenModel:
    
    def __init__(self, 
        distanceMiles, 
        milesToNextPossable,
        routeSpeed,
        averageSpeed,
        currentSpeed,
        timeTotalSeconds,
        paceTotalSeconds):
        
        self.distanceMiles = distanceMiles
        self.milesToNextPossable = milesToNextPossable
        self.routeSpeed = routeSpeed
        self.averageSpeed = averageSpeed
        self.currentSpeed = currentSpeed
        self.timeTotalSeconds = timeTotalSeconds
        self.paceTotalSeconds = paceTotalSeconds

    def printMe(self):        
        sys.stdout.write("dist: " + str(self.distanceMiles))
        sys.stdout.write(" mtnp: " + str(self.milesToNextPossable))
        sys.stdout.write(" rs  : " + str(self.routeSpeed))
        sys.stdout.write(" as  : " + str(self.averageSpeed))
        sys.stdout.write(" cs  : " + str(self.currentSpeed))
        sys.stdout.write(" tots: " + str(self.timeTotalSeconds)) 
        sys.stdout.write(" pacs: " + str(self.paceTotalSeconds))
        sys.stdout.write("\r\n")