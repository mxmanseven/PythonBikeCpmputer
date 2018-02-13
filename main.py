from WheelTick import WheelTick
from Computer import Computer
import datetime
import time
import pdb
from TimeService import TimeService
from Route import Route
import sys

def main():
	r = Route()

	r.AddSpeed(0, 6)
	r.AddSpeed(1, 12)
	r.AddSpeed(2, 18)

	r.CalculatePossibles()

	r.printPossables()

	pace = r.getPaceSecondsFromPossableAndMile(0.1, 1)
	# sys.stdout.write(r.getPaceSecondsFromPossableAndMile(0.1, 0.5))
	# sys.stdout.write(r.getPaceSecondsFromPossableAndMile(0.1, 1.5))
	
	

if __name__ == '__main__':
	main()