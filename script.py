from sound import detect
from ir import ir_trigger
import RPi.GPIO as GPIO
import time

SOUND_SENSOR_PIN = 25
IR_PIN = 24
RELAYER_PIN =23

GPIO.setmode(GPIO.BCM)
GPIO.setup(SOUND_SENSOR_PIN, GPIO.IN)
print "Sound Module Test (CTRL+C to exit)"
time.sleep(1)
print "Ready"


try:
    sensor = detect.Detect(SOUND_SENSOR_PIN)
    ir = ir_trigger.IR_TRIGGER(IR_PIN, RELAYER_PIN)
    # sensor.set_playfile("tweet.mp3", "mp3")
    # print "Playable :" + str(sensor.get_playable())
    # print "Set not playable to False"
    # sensor.set_playable(False)
    # print "Playable :" + str(sensor.get_playable())
    # sensor.add_event_detect()
    while 1:
        ir.run()
        if ir.ir_stat == False:
            sensor.set_playable(False)
        else:
            sensor.set_playable(True)
        # ir.trigger_on_off(.5)
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()

    print " Quit"

    # else:
    #     GPIO.output(RELAYER_PIN, GPIO.HIGH)
