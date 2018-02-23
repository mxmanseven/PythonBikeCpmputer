from WheelTick import WheelTick
from Computer import Computer
import datetime
import time
import pdb
from TimeService import TimeService
from Route import Route
import sys
from WheelManager import WheelManager

#  download the repository and run python setup.py install to install it into your Python package directory.
#  https://gist.github.com/DenisFromHR/cc863375a6e19dce359d
from RPLCD.i2c import CharLCD

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

def lcdTest():
	lcd = CharLCD('PCF8574', 0x27)
	#                 12345678911234567892    
	lcd.write_string('mm.mm    MM:ss    rs')
	lcd.write_string('PaceSecon: +ss AS ')
	lcd.write_string('123456789112345678CS')
	lcd.write_string('123456789112345678AS')
	#lcd.write_string('BBBBBBBBAAAAAAAAAA')
	sys.stdout.write('wrote hello world to lcd\r\n')
	time.sleep(5)
	#lcd.clear()	

def main():
	# sys.stdout.write(r.getPaceSecondsFromPossableAndMile(0.1, 0.5))
	# sys.stdout.write(r.getPaceSecondsFromPossableAndMile(0.1, 1.5))

	lcdTest()

	# wm = WheelManager(2)

	# time.sleep(1)
	# wm.newRawTick()

	# distance = wm.getTotalDistance()
	# sys.stdout.write('Distance: ' + str(distance) + '\r\n')

	# time.sleep(1)
	# wm.newRawTick()

	# distance = wm.getTotalDistance()
	# sys.stdout.write('Distance: ' + str(distance) + '\r\n')
	

if __name__ == '__main__':
	main()