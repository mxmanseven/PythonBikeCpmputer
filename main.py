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
from EnduroScreenModel import EnduroScreenModel

def main():
	# init lcd and wheelmanager
	lcdMan = LcdManager()
	wheelCircumferenceInches = 84.5
	wheelMan = WheelManager(wheelCircumferenceInches)
	timeScaleFactor = 1
	timeService = TimeService(timeScaleFactor)

	enduroScreenModel = EnduroScreenModel(0, 0, 0, 0, 0, 0, 0)
	lcdMan.setEnduroScreenByModel(enduroScreenModel)
	
	while (True):
		time.sleep(2)

		enduroScreenModel.currentSpeed = wheelMan.getSpeed()
		enduroScreenModel.averageSpeed = wheelMan.getSpeed(60, True)
		enduroScreenModel.distanceMiles = wheelMan.getTotalDistance()
		enduroScreenModel.timeTotalSeconds = timeService.CurrentTime()

		lcdMan.setEnduroScreenByModel(enduroScreenModel)

if __name__ == '__main__':
	main()