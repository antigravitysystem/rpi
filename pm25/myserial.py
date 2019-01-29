import serial
import time

#port = "/dev/ttyAMA0"  # Raspberry Pi 2
port = "/dev/ttyS0"    # Raspberry Pi 3

ser = serial.Serial(
        port=port,
        baudrate=2400,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout = 1
)

#ser = serial.Serial(port, baudrate = 2400)

def debug():
    byteData = ser.read(7) # read one, blocking
    byteData += ser.read(ser.inWaiting()).encode('hex')
    print byteData.encode('hex')

print "starting"
def show():
    byteData = ser.read(7)                          # read one, blocking
    byteData += ser.read(ser.inWaiting()).encode('hex')
    line = byteData.encode('hex')

    A = 550
    Vout = get_vout(line)
    #Vout = ((Vout_h * 256) + Vout_l) / 1024 * 5
    Dustdensity = int(A * Vout)
    #print "====================="
    #print "Vout:" + str(Vout) + "V"
    #DustDensity = "DustDensity:" + str(Dustdensity) + "ug/m3"
    sys.stdout.write("[  Vout: %s V     |    DustDensity: %s ug/m3 ] \r" % (Vout, Dustdensity))
    sys.stdout.flush()
    time.sleep(1)


try:
    while 1:
#        show()
        debug()
except KeyboardInterrupt:
    ser.close()