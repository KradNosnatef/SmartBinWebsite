import requests
import serial
import json

BID=-1
serial = serial.Serial()
serial.baudrate = 115200
serial.port = '/dev/cu.usbmodem11302'
serial.open()
while True:
    try:
        value = serial.readline()
        print(value.decode())

        dataObject=json.loads(value.decode().rstrip("\r\n"))
        dataObject["BID"]=BID


        data={}
        data["data"]=json.dumps(dataObject)
    except:
        pass
    #result=requests.post("http://fuqianshan.asuscomm.com:22000/Xapi",data=data)
    #if BID==-1:BID=int(result.text)
