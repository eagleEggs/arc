import RPi.GPIO as GPIO
import time
import os
import datetime
import MySQLdb
import sys
import string
from picamera import PiCamera
import asyncio
import smtplib

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(4,GPIO.OUT)

SOUND_PIN = 17
GPIO.setup(SOUND_PIN, GPIO.IN)

sourceEmail = ""
emailName = ""
destinationEmail = ""
sendChecks = 1

mailServer = smtplib.SMTP('',)
mailServer.starttls()
mailServer.login("", "")

host = ""
un = ""
pw = ""
DB = ""

count = 0


def activeSound(SOUND_PIN):
    
    nowtime = datetime.datetime.now()
    #count=count+1
    print ("Sound detected " + str(nowtime))
    logTime = ("Alert " + str(nowtime))
    print(logTime)
    
    try:
        db = MySQLdb.connect(host="", user="", passwd="", db="")
        qdb = db.cursor()
        query = "INSERT INTO arcDB(alerts) VALUES(1)"
        qdb.execute(query)
        print ("Submitted query to database")
        db.commit()
        db.close()
        
    except:
        print ("Issue submitting DB query")
        
    try:
        BODY = "Detected Sound"
        mailServer.sendmail("+sourceEmail+", "+destinationEmail+", BODY)
	#add send img in BODY
        print ("Sent email alert")
        
    except:    
        print ("Issue submitting email alert")
        
    try:
        #camera.start_preview()
        sleep(2)
        currentVideo = ('/home/pi/home/scripts/%s.h264' % logTime)
        #camera.start_recording(currentVideo)
        
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


async def waitForSound(start):
            
    GPIO.add_event_detect(SOUND_PIN, GPIO.RISING, callback=activeSound)
    
    end_time = start.time() + 60.0
    while True:
        if (start.time()) >= end_time:
            #detect whether reboot, storage, reconn, or other action is needed
            if sendChecks == 1:
                print ("Checking Database")
                print ("Checking Email")
                print ("Checking Mic Sensor")
                print ("Checking Camera Module")
                print ("Checking Resources")
                end_time = start.time() + 60.0
    

start = asyncio.get_event_loop()
start.run_until_complete(waitForSound(start))


try:
    print ("Starting Up...")
    #camera = PiCamera()
    start.run_forever()
finally:
    print ("Closing Down...")
    start.close()


