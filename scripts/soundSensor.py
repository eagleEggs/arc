
import RPi.GPIO as GPIO
import time
import os
import datetime

GPIO.setmode(GPIO.BCM)
SOUND_PIN = 17
GPIO.setup(SOUND_PIN, GPIO.IN)

count = 0

def DETECTED(SOUND_PIN):
        global count
        nowtime = datetime.datetime.now()
        count==1

        print "Sound detected " + str(nowtime) + " " + str(count)

time.sleep(2)
print "ready"

try:
        GPIO.add_event_detect(SOUND_PIN, GPIO.RISING, callback=DETECTED)
        while 1:
                time.sleep(1)

except KeyboardInterrupt:
        print "Quit"
        GPIO.cleanup()

