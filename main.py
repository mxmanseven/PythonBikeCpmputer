from WheelTick import WheelTick
from Computer import Computer
import datetime
import time
import pdb
from TimeService import TimeService
from Route import Route


def main():
	r = Route()

	r.AddSpeed(0, 6)
	r.AddSpeed(1, 12)
	r.AddSpeed(2, 18)

	r.CalculatePossibles()

	print("printPossiables")
	r.printPossables()
	
	

if __name__ == '__main__':
	main()