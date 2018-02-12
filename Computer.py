import sys
from WheelTick import WheelTick
import datetime

class Computer:

	def __init__(self):
		self.LastTicks = []
		self.MaxTicks = 3
		
	def AddTick(self, tick):
		sys.stdout.write('computer.addTick() lastticks len: ' + str(len(self.LastTicks)) + '\r\n')
		sys.stdout.write('computer.addTick() time: ' + str(datetime.datetime.now()) + '\r\n')
		if len(self.LastTicks) > self.MaxTicks:
			self.LastTicks.pop(0)
		self.LastTicks.append(tick)
		
	def Print(self):
		for tick in self.LastTicks:
			sys.stdout.write(str(tick.ArrivalTime) + '\r\n')