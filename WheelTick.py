import datetime

class WheelTick:
	ArrivalTime = datetime.datetime.now()
	TimeFromLastArrival = datetime.datetime.now()
	
	def __init__(self, lastArrivalTime):
		self.TimeFromLastArrival = lastArrivalTime
		self.ArrivalTime = datetime.datetime.now()