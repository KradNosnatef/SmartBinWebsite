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
        obj=json.loads(value.decode().rstrip("\r\n"))
        print(obj["fuck"])
        """data1=re.search("[a-z]+:([0-9]|[a-z]|[A-Z]|.)*",value.decode()).group()

        data2=data1.split(":",1)
        data3={}

        data3[data2[0]]=float(data2[1])

        jsonData=json.dumps(data3)
        print("jsonData is : "+jsonData)"""
    except:
        pass
    #jsonData=json.dumps(data)
    #requests.post("http://fuqianshan.asuscomm.com:22000/Xapi",data=data)
