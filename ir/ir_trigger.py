import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

RELAYER_PIN = 23
IR_SENSOR_PIN = 24
WAIT_SEC = 3
WAIT_MILLI_SEC = WAIT_SEC * 1000
TRIGGER_THRESHOLD = 3

trigger_count = 0
is_triggerable = True

#GPIO 23 -> Low level trigger relayer
GPIO.setup(RELAYER_PIN, GPIO.OUT)
GPIO.output(RELAYER_PIN, GPIO.HIGH)

#GPIO 24 -> Infrared Sensor
GPIO.setup(IR_SENSOR_PIN, GPIO.IN)

def ir_detected(IR_SENSOR_PIN):
    print "Wait for " + str(WAIT_SEC)  + " seconds"
    if GPIO.input(IR_SENSOR_PIN) == GPIO.HIGH :
        GPIO.output(RELAYER_PIN, GPIO.LOW)
        print "Low level relayer triggerd" + " RELAYER", GPIO.input(RELAYER_PIN)
    else:
        GPIO.output(RELAYER_PIN, GPIO.HIGH)

def rising():
    GPIO.add_event_detect(IR_SENSOR_PIN, GPIO.RISING, callback=ir_detected, bouncetime=WAIT_SEC)

def trigger_on_off(time_length):

    global trigger_count

    if trigger_count < TRIGGER_THRESHOLD :
        trigger_count += 1
        print "Trigger count " + str(trigger_count)
        GPIO.output(RELAYER_PIN, GPIO.LOW)
        time.sleep(time_length)
        GPIO.output(RELAYER_PIN, GPIO.HIGH)
    else:
        is_triggerable = False
        print "Trigger Stopped"

def if_and_if(IR_SENSOR_PIN):
    if GPIO.input(IR_SENSOR_PIN) == GPIO.HIGH and is_triggerable == True:

        time.sleep(WAIT_SEC)
        if GPIO.input(IR_SENSOR_PIN) == GPIO.HIGH:
            trigger_on_off(.5)
    # else:
    #     GPIO.output(RELAYER_PIN, GPIO.HIGH)


try:
    # rising()
    while 1:
        print "IR SENSOR", GPIO.input(IR_SENSOR_PIN)
        time.sleep(1)
        if_and_if(IR_SENSOR_PIN)
        # GPIO.output(RELAYER_PIN, GPIO.HIGH)

except KeyboardInterrupt:
    GPIO.cleanup()
    print "Quit!"
# if object is near

