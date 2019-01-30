from sound import detect
import RPi.GPIO as GPIO
import time

SOUND_SENSOR_PIN = 25
GPIO.setmode(GPIO.BCM)
GPIO.setup(SOUND_SENSOR_PIN, GPIO.IN)
print "Sound Module Test (CTRL+C to exit)"
time.sleep(1)
print "Ready"


try:
    sensor = detect.Detect(SOUND_SENSOR_PIN)
    # sensor.set_playfile("tweet.mp3", "mp3")
    print "Playable :" + str(sensor.get_playable())
    print "Set not playable to False"
    sensor.set_playable(False)
    print "Playable :" + str(sensor.get_playable())
    # sensor.add_event_detect()
    while 1:
        time.sleep(100)
except KeyboardInterrupt:
    print " Quit"
    GPIO.cleanup()
