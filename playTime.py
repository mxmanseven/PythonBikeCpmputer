import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)


GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def hit(a):
    print 'hi'


GPIO.add_event_detect(7, GPIO.FALLING, callback=hit, bouncetime=300)

while (True):
    pass