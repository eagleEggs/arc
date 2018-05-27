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
import base64

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

mailServer = smtplib.SMTP('smtp.gmail.com',587)
mailServer.starttls()
mailServer.login("", "")

host = ""
un = ""
pw = ""
DB = ""

count = 0


async def setup():
    print ("Setting up System...")
    try:
        print ("Setting up Database...")
        global db
        global qdb
        db = MySQLdb.connect(host="", user="", passwd="", db="")
        qdb = db.cursor()
        query = "INSERT INTO arcDB(logon) VALUES(1)"
        qdb.execute(query)
        print ("Submitted logon to database")
        db.commit()
        db.close()

    except:
        print ("Issue setting up database")

def activeSound(SOUND_PIN):
    
    
    
    nowtime = datetime.datetime.now()
    print ("Sound detected " + str(nowtime))
    logTime = ("Alert " + str(nowtime))
    print(logTime)
    
        
    try:
        BODY = "Detected Sound"
        mailServer.sendmail("", "", BODY)
        print ("Sent email alert")
        
    except:    
        print ("Issue submitting email alert")
        
    try:
        camera = PiCamera()
        print ("Initiated Camera")
        camera.resolution = (640, 480)
        print ("Set Camera Resolution")
        camera.start_preview(fullscreen=False, window = (100, 20, 640, 480))
        print ("Started Camera Preview")
        camera.capture('/home/pi/Pictures/image.jpg')
        
        currentVideo = ('/home/pi/scripts/test.h264')
        camera.start_recording(currentVideo)
        print ("Started Recording...")
        camera.wait_recording(1)
        camera.stop_recording()
        print ("Stopped Recording")
        camera.stop_preview()
        print ("Stopped Preview")
        
        try:
            db2 = MySQLdb.connect(host="", user="", passwd="", db="")
            with open(currentVideo, 'rb') as x:
                video = x.read()
            x.close()
            print("Opened Video to prep for Database")
            encodeString = base64.b64encode(video)
            print("Encoded Video")
            qdb2 = db2.cursor()
            print("Set up qdb2 Cursor")
            vSQL2 = "INSERT INTO arcDB (video) VALUES (%s)"
            print("Created Insert String")
            qdb2.execute(vSQL2, (video,))
            db2.commit()
            print ("Inserted Query")
        except:
            print ("Could not upload video to database")
        
    except:
        print("Could not access camera module")
        
    GPIO.output(27,GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(27,GPIO.LOW)


async def waitForSound(start):
            
    GPIO.add_event_detect(SOUND_PIN, GPIO.RISING, callback=activeSound)
    

async def threadedIntegrity(db):
    end_time = start.time() + 3.0
    while True:
        if (start.time()) >= end_time:
            #detect whether reboot, storage, reconn, or other action is needed
            if sendChecks == 1:
                await asyncio.gather(
                        dbI(),
                        emI(),
                        miI(),
                        caI(),
                        reI()
                    )
                end_time = start.time() + 3.0
                
async def dbI():
    print ("Checking Database")
    if db.open:
        print("Database Connection is Open")
    else:
        print("Database is Closed")
        
async def emI():
    print ("Checking...")
async def miI():
    print ("Checking...")
async def caI():
    print ("Checking...")
async def reI():
    print ("Checking...")
    

#--
init = asyncio.get_event_loop()
init.run_until_complete(setup())
#---
start = asyncio.get_event_loop()
start.run_until_complete(waitForSound(start))
#---
checks = asyncio.get_event_loop()
checks.run_until_complete(threadedIntegrity(db))


try:
    print ("Starting Up...")
    init.run_forever()
    start.run_forever()
    threadedIntegrity.run_forever(db)
finally:
    print ("Closing Down...")
    db.close()
    print ("Database Closed")
    init.close()
    start.close()
    checks.close()


