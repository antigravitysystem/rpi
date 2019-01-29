#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time,sys,serial


# configure the serial connections (the parameters differs on the device you are connecting to)
# if uses Rpi serial port, the serial port login must be disable/stop first
# sudo systemctl stop serial-getty@ttyS0.service
ser = serial.Serial(
    port = '/dev/serial0',
    baudrate = 2400,
    parity = serial.PARITY_NONE,
    stopbits = serial.STOPBITS_ONE,
    bytesize = serial.EIGHTBITS,
    timeout = 1
)
#ser.open()
#ser.write("testing")

def debug():
    byteData = ser.read(7) # read one, blocking
    byteData += ser.read(ser.inWaiting()).encode('hex')
    print byteData.encode('hex')
    time.sleep(1)

def num_format(num_hex):
    num_int = int(num_hex, 16)
    return float(format(num_int, '.10f'))

def get_vout(hex_str):
    #0005004d52ffaa
    #找到数据开始位aa
    index = hex_str.find('aa')
    #获取Vout_h索引位置
    if index==12:
        Vout_h_index = 0
    else:
        Vout_h_index = index + 2
    #获取Vout_l索引位置
    if Vout_h_index==12:
        Vout_l_index = 0
    else:
        Vout_l_index = Vout_h_index + 2

    #开始计算
    Vout_h = num_format(hex_str [Vout_h_index:Vout_h_index+2])
    Vout_l = num_format(hex_str [Vout_l_index:Vout_l_index+2])

    Vout = ((Vout_h * 256) + Vout_l) / 1024 * 5     #输入电压
    Vout = round(Vout, 3)
    return Vout

def get_serial_data():
    # read one, blocking
    bytes = 7
    byteData = ser.read(bytes)
    byteData += ser.read(ser.inWaiting()).encode('hex')
    line = byteData.encode('hex')
    return line

def get_density(Vout):
    A = 550
    Dustdensity = int(A * Vout)                     #灰尘密度,单位 ug/m3
    return Dustdensity

def show():
    
    line = get_serial_data()
    #比例系数,由用户自定义

    #输入电压

    Vout = get_vout(line)
    #Vout = ((Vout_h * 256) + Vout_l) / 1024 * 5    #输入电压
    DustDensity = get_density(Vout)
    #print "====================="
    #print "Vout:" + str(Vout) + "V"
    #DustDensity = "DustDensity:" + str(Dustdensity) + "ug/m3"

    sys.stdout.write("[  Vout: %s V     |    DustDensity: %s ug/m3 ] \r" % (Vout, DustDensity))
    sys.stdout.flush()
    time.sleep(1)

try:
    while 1:
        show()
        # debug()
        # print get_serial_data()
        # time.sleep(1)

except KeyboardInterrupt:
    ser.close()
