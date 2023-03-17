from flask import Flask
from flask import request
from flask_cors import *
import requests
import serial
import json
import threading
import time

BID=-1
serial = serial.Serial()
serial.baudrate = 115200
serial.port = '/dev/cu.usbmodem11302'
serial.open()
num=0

class SerialReadHandler(threading.Thread): 
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name

    def run(self):
        while True:
            try:
                value = serial.readline()

                dataObject=json.loads(value.decode().rstrip("\r\n"))
                dataObject["BID"]=BID


                data={}
                data["data"]=json.dumps(dataObject)
                print(data)
            except:
                pass
            #result=requests.post("http://fuqianshan.asuscomm.com:22000/Xapi",data=data)
            #if BID==-1:BID=int(result.text)

serialReadHandler=SerialReadHandler(1,"mainHandler")
serialReadHandler.start()

app=Flask(__name__)
@app.route("/cmd/startup")
def startup():
    text="ST:0;"
    serial.write(text.encode())
    return('success')

if __name__ == '__main__':
   app.run(host='0.0.0.0',port=25565)
