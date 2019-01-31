#!/usr/bin/python

from pydub import AudioSegment
from pydub.playback import play

tweet = AudioSegment.from_file("./playfile/tweet.wav", format="wav")
play(tweet)
