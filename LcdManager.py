
#  download the repository and run python setup.py install to install it into your Python package directory.
#  https://gist.github.com/DenisFromHR/cc863375a6e19dce359d
from RPLCD.i2c import CharLCD

import sys
from math import ceil, floor

class LcdManager:

    def __init__(self):
		self.lcd = CharLCD('PCF8574', 0x27)

    def setEnduroScreen(self, distance, paceTotalSeconds, 
		routeSpeed, averageSpeed,timeTotalSeconds, 
		milesToNextPossable, currentSpeed):
		
		paceMinutes = int(abs(paceTotalSeconds / 60.0))
		paceSeconds = int(abs(paceTotalSeconds % 60))
		if paceTotalSeconds < 0:
			paceMinutes = floor(abs(paceTotalSeconds / 60.0))
			paceSeconds = int(abs(paceTotalSeconds) % 60)
		
		if paceMinutes > 10:
			paceMinutes = 9
			paceSeconds = 59

		paceSign = "+"
		if paceTotalSeconds < 0:
			paceSign = "-"

		sys.stdout.write('paceTotalSeconds ' + str(paceTotalSeconds) + '\r\n')
		sys.stdout.write('paceMinutes ' + str(paceMinutes) + '\r\n')
		sys.stdout.write('paceSeconds ' + str(paceSeconds) + '\r\n')
		sys.stdout.write('\r\n')

		line1 = ("D{:5.2f}   P{}{:01.0f}:{:02d}   {:2.0f}\r\n"
		.format(distance, paceSign, paceMinutes, paceSeconds, routeSpeed))

		line2 = "{:20.0f}\r\n".format(averageSpeed)

		timeMinutes = int(round(timeTotalSeconds / 60.0)) % 60
		timeSeconds = int(round(timeTotalSeconds % 60))
		
		milesToNextPossableAdjusted = milesToNextPossable
		if milesToNextPossable > 10:
			milesToNextPossableAdjusted = 9.9

		line3 = ("T {:02.0f}:{:02d}  NP{:4.1f} {:4.0f}\r\n"
		.format(timeMinutes, timeSeconds, milesToNextPossableAdjusted, currentSpeed))

		# knh todo - get rounding correct 

		# always round away from zero
		paceMarkerCount = int(ceil(abs(paceTotalSeconds / 15)))
			
		# We will display at most 9 pace chars
		if paceMarkerCount > 9:
			paceMarkerCount = 9
		# we have 20 chars, those that are not pace markers are spaces
		paddCharCount = 20 - paceMarkerCount

		# if we are ahead with positive paceTotalSeconds, use A
		# if we are behaind with negative paceTotalSeconds, use B
		if paceTotalSeconds > 0: 
			paceMarkerChar = "A"
		else:
			paceMarkerChar = "B"

		paceString = ""

		# build correct length pace String
		for i in range(1, paceMarkerCount):
			paceString += paceMarkerChar

		# build correct length padd string and place it on the correct side
		#if paceTotalSeconds > 0:
		if paceTotalSeconds > 0:
			paddString = ""
			for i in range(1, paddCharCount):
				paddString += " "
			paceString = paddString + paceString

		line4 = paceString +  "\r\n"

		# sys.stdout.write(line1)
		# sys.stdout.write(line2)
		# sys.stdout.write(line3)
		# sys.stdout.write(line4)
		self.lcd.clear()
		self.lcd.write_string(line1)
		self.lcd.write_string(line2)
		self.lcd.write_string(line3)
		self.lcd.write_string(line4)
	# def lcdTest1(self):
	# 	#                 12345678911234567892
	# 	self.lcd.write_string('D12.34   P+15:35  RS')
	# 	self.lcd.write_string('                  AS')
	# 	self.lcd.write_string('T 09:00   NP 1.5  CS')
	# 	self.lcd.write_string('BBBBBBBBB  AAAAAAAAA')