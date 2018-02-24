from WheelTick import WheelTick
from Computer import Computer
import datetime
import time
import pdb
from TimeService import TimeService
from Route import Route
import sys
from WheelManager import WheelManager
from LcdManager import LcdManager

#  download the repository and run python setup.py install to install it into your Python package directory.
#  https://gist.github.com/DenisFromHR/cc863375a6e19dce359d
#from RPLCD.i2c import CharLCD

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

# def lcdTest1():
# 	lcd = CharLCD('PCF8574', 0x27)
# 	#                 12345678911234567892    
# 	lcd.write_string('D12.34   P+15:35  RS')
# 	lcd.write_string('                  AS')
# 	lcd.write_string('T 09:00   NP 1.5  CS')
# 	lcd.write_string('BBBBBBBBB  AAAAAAAAA')
# 	sys.stdout.write('wrote hello world to lcd\r\n')
# 	time.sleep(5)
	
# #def lcdTest2():
# 	#                 12345678911234567892    
# 	lcd.write_string('D12.34   P-00:35  12')
# 	lcd.write_string('                  10')
# 	lcd.write_string('T 55:23   NP 0.5  11')
# 	lcd.write_string('BB                  ')
# 	sys.stdout.write('wrote hello world to lcd\r\n')
# 	time.sleep(5)	

# #def lcdTest3():
# 	#                 12345678911234567892    
# 	lcd.write_string('D12.35  P-04:21  12')
# 	lcd.write_string('                  8')
# 	lcd.write_string('T 56:41  NP 0.1   7')
# 	lcd.write_string('BBBBBBBBB          ')
# 	sys.stdout.write('wrote hello world to lcd\r\n')
# 	time.sleep(5)

def main():
	# sys.stdout.write(r.getPaceSecondsFromPossableAndMile(0.1, 0.5))
	# sys.stdout.write(r.getPaceSecondsFromPossableAndMile(0.1, 1.5))
	# line1 = "D{:5.2f}   P+{:5.2f}  {:2.0f}\r\n".format(2.3, 3.4, 12.67)
	# sys.stdout.write(line1)
	# line = "{:5.2f}\r\n".format(12.34)
	# sys.stdout.write(line)
	# line = "{:5.2f}\r\n".format(0.01)
	# sys.stdout.write(line)

	lcdM = LcdManager()
	lcdM.setEnduroScreen(1.35, 90, 12, 11, 6, 55.11, 12)
	time.sleep(5)
	lcdM.setEnduroScreen(12.35, -5, 12, 11.5, 6.5, 55.11, 12)
	time.sleep(5)
	lcdM.setEnduroScreen(12.35, -20, 12, 11.5, 540.1, 55.11, 12)
	time.sleep(5)
	lcdM.setEnduroScreen(12.35, -40, 12, 11.5, 606.5, 55.11, 12)
	time.sleep(5)
	lcdM.setEnduroScreen(12.35, -66, 12, 11.5, 1200.5, 55.11, 12)
	time.sleep(5)
	lcdM.setEnduroScreen(12.35, -666, 12, 11.5, 3000, 55.11, 12)
	time.sleep(5)
	lcdM.setEnduroScreen(12.35, -666, 12, 11.5, 3660, 55.11, 12)

	#lcdTest1()

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