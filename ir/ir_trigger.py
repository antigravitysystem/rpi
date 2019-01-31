import RPi.GPIO as GPIO
import time

class IR_TRIGGER():
    def __init__(self, IR_PIN, RELAYER_PIN):
        self.RELAYER_PIN = RELAYER_PIN
        self.IR_PIN = IR_PIN
        self.wait_sec = 1
        self.wait_milli_sec = self.wait_sec * 1000
        self.trigger_limit = 3
        self.trigger_count = 0
        self.is_triggerable = True
        self.status = False

        #GPIO 23 -> Low level trigger relayer
        GPIO.setup(RELAYER_PIN, GPIO.OUT)
        GPIO.output(RELAYER_PIN, GPIO.HIGH)

        #GPIO 24 -> Infrared Sensor
        GPIO.setup(IR_PIN, GPIO.IN)

        # GPIO.add_event_detect(IR_PIN, GPIO.RISING, callback=self.ir_detected, bouncetime=2000)

    def ir_detected(self, IR_PIN):
        if GPIO.input(self.IR_PIN) == GPIO.HIGH:
            time.sleep(self.wait_sec)
            if GPIO.input(self.IR_PIN) == GPIO.HIGH:
                self.set_status(True)
                if self.get_triggerable() == True:
                    # if GPIO.input(IR_PIN) == GPIO.HIGH :
                    self.trigger()

                else:
                    GPIO.output(self.RELAYER_PIN, GPIO.HIGH)
        else:
            self.set_status(False)
    def trigger(self):
        # print "Trigger"
        # time.sleep(self.wait_sec)
        self.trigger_on_off(.5)


        # print "Wait for " + str(self.wait_sec)  + " seconds"
        # if GPIO.input(self.IR_PIN) == GPIO.HIGH :
        #     GPIO.output(self.RELAYER_PIN, GPIO.LOW)
        #     print "Low level relayer triggerd" + " RELAYER", GPIO.input(self.RELAYER_PIN)
        # else:
        #     GPIO.output(self.RELAYER_PIN, GPIO.HIGH)

    # def rising():

    def trigger_on_off(self, time_length):

        # print "Trigger count " + str(self.trigger_count)
        GPIO.output(self.RELAYER_PIN, GPIO.LOW)
        time.sleep(time_length)
        GPIO.output(self.RELAYER_PIN, GPIO.HIGH)

    def get_status(self):
        return self.status

    def set_status(self, status):
        self.status = status

    def set_triggerable(self, triggerable):
        try:
            self.is_triggerable = triggerable
            if not isinstance(triggerable, bool):
                raise Exception('set_triggerable must be boolean value')
        except Exception as error:
            print('Oppse! ' + repr(error))

    def get_triggerable(self):
        return self.is_triggerable
        # except Exception as e:
            # raise

    def run(self):
        print "IR SENSOR", GPIO.input(self.IR_PIN)
        print "is_triggerable: " + str(self.is_triggerable)

                # if self.trigger_count < self.trigger_limit :
                    # self.trigger_count += 1

        self.ir_detected(self.IR_PIN)
                    # self.trigger_on_off(.5)
                # else:
                    # self.set_triggerable(False)
                    # print "Trigger Stopped"
