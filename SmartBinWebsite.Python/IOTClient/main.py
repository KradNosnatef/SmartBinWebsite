import requests
import serial
import json
import re

serial = serial.Serial()
serial.baudrate = 115200
serial.port = '/dev/cu.usbmodem11302'
serial.open()
while True:
    try:
        value = serial.readline()
        print(value.decode())
        jsonString=value.decode().rstrip("\r\n")
    except:
        pass
    #requests.post("http://fuqianshan.asuscomm.com:22000/Xapi",data=data)
