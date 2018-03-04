import RPi.GPIO as GPIO
from WheelManager import WheelManager

class WheelSensorListener:
    # listens on gpio pin 7 for falling edge
    # on tick, calls wheelManager.newRawTick

    def __init__(self, wheelManager):
        self.wheelManager = wheelManager
        GPIO.setmode(GPIO.BOARD)
        # set board GPIO pin 7 to input with a pull up resistor
        GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        # set interupt on pin 7 falling value and call newRawTick
        # knh todo - tune bouncetime
        GPIO.add_event_detect(
            7, 
            GPIO.FALLING, 
            callback=self.wheelManager.newRawTick,
            bouncetime=300)