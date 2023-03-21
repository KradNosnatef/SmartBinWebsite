from flask import Flask
from flask import request
from flask_cors import *
import requests
import serial
import json
import threading
import time

BID=-1
mySerial=None
num=0
position={
    'latitude':0,
    'longitude':0
}
abnormalAttitudeCounter=0

def serialReconnect():
    try:
        print('trying to reconnect serial')
        global mySerial

        mySerial = serial.Serial()
        mySerial.baudrate = 115200
        mySerial.port = '/dev/cu.usbmodem11302'
        mySerial.open()
        print('connected')
        if BID!=-1:
            text="ST:0"
            mySerial.write(text.encode())
    except:
        print('connecting failed,will retry anothertime')

serialReconnect()


class SerialReadHandler(threading.Thread): 
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name

    def run(self):
        global BID
        global position
        global abnormalAttitudeCounter
        data={}
        while True:
            try:
                value = mySerial.readline()

                dataObject=json.loads(value.decode().rstrip("\r\n"))
                dataObject["BID"]=BID

                #you should get a BID to do anything else
                if BID==-1:
                    dataObject["longitude"]=position['longitude']
                    dataObject["latitude"]=position['latitude']

                    data["data"]=json.dumps(dataObject)
                    print(data)

                    result=requests.post("http://fuqianshan.asuscomm.com:22000/Xapi/postReport",data=data)
                    if BID==-1:BID=int(result.text)

                else:
                    if dataObject["pitch"]<-70 and  dataObject["pitch"]>-110:abnormalAttitudeCounter=0
                    else: abnormalAttitudeCounter+=1
                    
                    if abnormalAttitudeCounter>=3: dataObject["alert2"]=1
                    else :dataObject["alert2"]=0

                    needToSendReport=False
                    if dataObject["pitch"]<-70 and  dataObject["pitch"]>-110 and dataObject["accel"]<1200 and dataObject["accel"]>800 and dataObject["distance"]<420 and dataObject["distance"]>70:
                        needToSendReport=True
                    else: print("regular report will not be sent")
                    data["data"]=json.dumps(dataObject)
                    print(data)
                    #if BID!=-1 anyway you must post the alert
                    requests.post("http://fuqianshan.asuscomm.com:22000/Xapi/postAlert",data=data)
                    #when pitch or accel shows unstable situation do not send regular report
                    if needToSendReport:requests.post("http://fuqianshan.asuscomm.com:22000/Xapi/postReport",data=data)

                
            except:
                print("why?")
                serialReconnect()
                time.sleep(1)

serialReadHandler=SerialReadHandler(1,"mainHandler")
serialReadHandler.start()
reportPeriod=10

app=Flask(__name__)
@app.route("/cmd/startup")
def startup():
    text="ST:0;"
    try:
        mySerial.write(text.encode())
        print("should startup")
        return('success')
    except:
        serialReconnect()
        mySerial.write(text.encode())
        return('success??')

@app.route("/cmd/setReportSpeed",methods=['POST'])
@cross_origin()
def setReportSpeed():
    dataObject=json.loads(request.data.decode())
    text="SP:"+str(dataObject['period'])+";"
    print(text)
    try:
        mySerial.write(text.encode())
    except:
        serialReconnect()
        mySerial.write(text.encode())
    return('success')

@app.route("/cmd/setPosition",methods=['POST'])
@cross_origin()
def setPosition():
    dataObject=json.loads(request.data.decode())
    position['latitude']=dataObject['latitude']
    position['longitude']=dataObject['longitude']
    print(position)
    return('success')
    

if __name__ == '__main__':
   app.run(host='0.0.0.0',port=25565)
