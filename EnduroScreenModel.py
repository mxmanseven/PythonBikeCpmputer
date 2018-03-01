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