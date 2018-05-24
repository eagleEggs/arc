import RPi.GPIO as GPIO
import time
import os
import datetime
import MySQLdb
import sys
import string
from picamera import PiCamera

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(4,GPIO.OUT)

SOUND_PIN = 17
GPIO.setup(SOUND_PIN, GPIO.IN)

count = 0
host = ""
un = ""
pw = ""
DB = ""


def activeSound(SOUND_PIN):
    
    nowtime = datetime.datetime.now()
    count+=1
    print ("Sound detected " + str(nowtime) + " " + str(count))
    logTime = ("Alert " + str(nowtime) + " " + str(count))
    print(logTime)
    
    try:
        db = MySQLdb.connect(host="", user="", passwd="", db="")
        qdb = db.cursor()
        query = "INSERT INTO arcDB(alerts) VALUES(1)"
        qdb.execute(query)
        db.commit()
        db.close()
        print ("Submitted query to database")
    except:    
        print ("Issue submitting DB query")
    try:
        camera.start_preview()
        sleep(2)
        currentVideo = ('/home/pi/home/scripts/%s.h264' % logTime)
        camera.start_recording(currentVideo)
        
        # add check for diminishing sounds before sleeping
        # to continue recording until it stops
        
        time.sleep(5)
        camera.stop_recording()
        camera.stop_preview()
        
        try:
            video = open(currentVideo, 'rb').read()
            vSQL = "INSERT INTO arcDB (video) VALUES (%s)"
            qdb.execute(vSQL, (video))
        except:
            print ("Could not upload video to database")
        
    except:
        print("Could not access camera module")
        
    GPIO.output(27,GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(27,GPIO.LOW)

print ("Starting Up...")
camera = PiCamera()


try:
	GPIO.add_event_detect(SOUND_PIN, GPIO.RISING, callback=activeSound)
	while 1:
		time.sleep(1)

except KeyboardInterrupt:
	print ("Quitting")
	GPIO.cleanup()

