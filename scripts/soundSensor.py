import RPi.GPIO as GPIO
import time
import os
import datetime
import MySQLdb
import sys
import string

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(4,GPIO.OUT)

SOUND_PIN = 17
GPIO.setup(SOUND_PIN, GPIO.IN)

count = 0


def activeSound(SOUND_PIN):
    
    try:
        db = MySQLdb.connect(host="HOST", user="USER", passwd="PASSWORD", db="DBNAME")
        qdb = db.cursor()
        query = "INSERT INTO arcDB(alerts) VALUES(1)"
        qdb.execute(query)
        db.commit()
        db.close()
        print ("Submitted query to database")
    except:    
        print ("Issue submitting DB query")
    global count
    nowtime = datetime.datetime.now()
    count+=1
    print ("Sound detected " + str(nowtime) + " " + str(count))
    GPIO.output(27,GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(27,GPIO.LOW)

print ("Starting Up...")


try:
	GPIO.add_event_detect(SOUND_PIN, GPIO.RISING, callback=activeSound)
	while 1:
		time.sleep(1)

except KeyboardInterrupt:
	print ("Quitting")
	GPIO.cleanup()

