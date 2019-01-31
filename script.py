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

    while 1:
        ir.run()
        if ir.get_status() == True:
            sensor.set_playable(False)
        else:
            # print "get status"
            sensor.set_playable(True)
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
    print " Quit"
