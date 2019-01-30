#!/usr/bin/python

import RPi.GPIO as GPIO
import time
import datetime
import os

from pydub import AudioSegment
from pydub.playback import play

class Detect():
    def __init__(self, PIN):

        self.sensor_pin = PIN
        self.count = 0
        self.is_playable = True

        # setup defaukt audio file to play
        playfile = "tweet.mp3"
        file_format = "mp3"
        self.set_playfile(playfile, file_format)

        # Raspberry pi event
        GPIO.add_event_detect(PIN, GPIO.RISING, self.detected, bouncetime=2000)

    def set_playfile(self, playfile, file_format):
        self.playfile = playfile

        # specify the file name which will be played. Put this file name under
        # playfile folder
        current_path = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_path, "playfile", playfile)
        audio_path = os.path.abspath(file_path)
        self.tweet = AudioSegment.from_file(audio_path, format=file_format)

    def detected(self, channel):
        nowtime = datetime.datetime.now()
        self.count += 1

        print "Sound Detected! " + str(nowtime) + " " + str(self.count)
       #os.system("./playfile.py")
    #   playfile()
        if self.is_playable == True:
            play(self.tweet)

    def get_playable(self):
        return self.is_playable

    def set_playable(self, true_or_false):
        self.is_playable = true_or_false
        # return nowtime
