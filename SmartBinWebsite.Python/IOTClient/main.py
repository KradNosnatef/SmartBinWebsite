import requests
import serial
import json

serial = serial.Serial()
serial.baudrate = 115200
serial.port = '/dev/cu.usbmodem11302'
serial.open()
while True:
    value = serial.readline()
    print(value.decode())

    data={'data':value.decode()}
    jsonData=json.dumps(data)
    requests.post("http://fuqianshan.asuscomm.com/Xapi",data=data)
