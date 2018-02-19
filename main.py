from WheelTick import WheelTick
from Computer import Computer
import datetime
import time
import pdb
from TimeService import TimeService
from Route import Route
import sys
from WheelManager import WheelManager

def testRoute():
	r = Route()

	r.AddSpeed(0, 6)
	r.AddSpeed(1, 12)
	r.AddSpeed(2, 18)

	r.CalculatePossibles()

	r.printPossables()

	pace = r.getPaceSecondsFromPossableAndMile(0.1, 0)
	sys.stdout.write(str(pace) + "\r\n")
	pace = r.getPaceSecondsFromPossableAndMile(0.1, 0.5)
	sys.stdout.write(str(pace) + "\r\n")
	pace = r.getPaceSecondsFromPossableAndMile(0.1, 1)
	sys.stdout.write(str(pace) + "\r\n")
	pace = r.getPaceSecondsFromPossableAndMile(0.1, 2)
	sys.stdout.write(str(pace) + "\r\n\r\n")

	pace = r.getPaceSecondsFromPossableAndMile(0.15, 0)
	sys.stdout.write(str(pace) + "\r\n")
	pace = r.getPaceSecondsFromPossableAndMile(0.15, 0.5)
	sys.stdout.write(str(pace) + "\r\n")
	pace = r.getPaceSecondsFromPossableAndMile(0.15, 1)
	sys.stdout.write(str(pace) + "\r\n")
	pace = r.getPaceSecondsFromPossableAndMile(0.15, 2)
	sys.stdout.write(str(pace) + "\r\n")

def main():
	# sys.stdout.write(r.getPaceSecondsFromPossableAndMile(0.1, 0.5))
	# sys.stdout.write(r.getPaceSecondsFromPossableAndMile(0.1, 1.5))
	wm = WheelManager(2)

	time.sleep(1)
	wm.newRawTick()

	distance = wm.getTotalDistance()
	sys.stdout.write('Distance: ' + str(distance) + '\r\n')

	time.sleep(1)
	wm.newRawTick()

	distance = wm.getTotalDistance()
	sys.stdout.write('Distance: ' + str(distance) + '\r\n')
	

if __name__ == '__main__':
	main()