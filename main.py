from WheelTick import WheelTick
from Computer import Computer
import datetime
import time
import pdb
from TimeService import TimeService
from Route import Route
import sys
from WheelManager import WheelManager
# comment out when testing on pc
#from WheelSensorListener import WheelSensorListener
from LcdManager import LcdManager
from EnduroScreenModel import EnduroScreenModel

def main():
	
	# comment out WheelSensorListener when testing on pc
	#wheelSensor = WheelSensorListener(wheelMan)
	# init lcd and wheelmanager
	lcdMan = LcdManager()
	timeScaleFactor = 1
	timeService = TimeService(timeScaleFactor)
        timeService.ResetTime()
	wheelCircumferenceInches = 84.5
	wheelMan = WheelManager(wheelCircumferenceInches, timeService)

	enduroScreenModel = EnduroScreenModel(0, 0, 0, 0, 0, 0, 0)
	lcdMan.setEnduroScreenByModel(enduroScreenModel)

        count = 0
	while (True):
		time.sleep(1)
                sys.stdout.write("c: " + str(count) + "\r\n")
                count += 1
		wheelMan.newRawTick(1)

		enduroScreenModel.currentSpeed = wheelMan.getSpeed()
		enduroScreenModel.averageSpeed = wheelMan.getSpeed(60, True)
		enduroScreenModel.distanceMiles = wheelMan.getTotalDistance()
		enduroScreenModel.timeTotalSeconds = timeService.CurrentTime()
                sys.stdout.write("t: " + str(timeService.CurrentTime()) + "\n")

		enduroScreenModel.printMe()
		lcdMan.setEnduroScreenByModel(enduroScreenModel)

if __name__ == '__main__':
	main()
