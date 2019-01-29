#!/usr/bin/python

#Monitors GPIO pin 40 for input. A sound module is set up on physical pin 40.
#https://pinout.xyz/pinout/wiringpi#
import RPi.GPIO as GPIO
import time
import datetime
import os

from pydub import AudioSegment
from pydub.playback import play

tweet = AudioSegment.from_file("./playfile/tweet.wav", format="wav")

GPIO.setmode(GPIO.BCM)
SOUND_PIN = 25
GPIO.setup(SOUND_PIN, GPIO.IN)

count = 0

def DETECTED(SOUND_PIN):
   global count
   nowtime = datetime.datetime.now()
   count += 1

   print "Sound Detected! " + str(nowtime) + " " + str(count)
   #os.system("./playfile.py")
#   playfile()
   play(tweet)

   return nowtime

print "Sound Module Test (CTRL+C to exit)"
time.sleep(2)
print "Ready"

try:
   GPIO.add_event_detect(SOUND_PIN, GPIO.RISING, callback=DETECTED, bouncetime=2000)
   while 1:
      time.sleep(100)
except KeyboardInterrupt:
   print " Quit"
   GPIO.cleanup()
