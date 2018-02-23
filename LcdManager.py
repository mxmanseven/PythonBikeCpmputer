
#  download the repository and run python setup.py install to install it into your Python package directory.
#  https://gist.github.com/DenisFromHR/cc863375a6e19dce359d
from RPLCD.i2c import CharLCD

class LcdManager:

    def __init__(self):
	    self.lcd = CharLCD('PCF8574', 0x27)

    def setEnduroScreen(self, distance, paceSeconds, routeSpeed, averageSpeed,time, milesToNextPossable, currentSpeed):
		# knh todo convert paceSeconds to minutes and seconds
		line1 = ("D{:5.2f}   P+{:5.2f}  {:2.0f}\r\n".format(distance, paceSeconds, routeSpeed))
		line2 = "{:18.0f}".format(averageSpeed)
		line3 = "{:18.0f}".format(averageSpeed)
		line4 = "{:18.0f}".format(averageSpeed)

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