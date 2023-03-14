from flask import Flask
from flask import request
from flask_cors import *
from BinLogDAO import *
import json
import requests

message={"data":"No Data"}
app=Flask(__name__)

@app.route('/home')
def helloWorld():
    return(message["data"])

@app.route('/Xapi',methods=['POST'])
def Xapi():
    message["data"]+=request.form["data"]
    
    dataObject=json.loads(request.form["data"])

    if dataObject["BID"]==-1:
        dataObject["BID"]=BinLogDAO.BinRigister(0,0)

    BinLogDAO.insertRawInfo(dataObject["BID"],dataObject["weight"],dataObject["distance"],dataObject["pitch"],dataObject["roll"])
    if dataObject["alert0"]==1:BinLogDAO.insertAlert(dataObject["BID"],"SwitchDoor Detected")
    if dataObject["alert1"]==1:BinLogDAO.insertAlert(dataObject["BID"],"Vibration Detected")

    return str(dataObject["BID"])

if __name__ == '__main__':
   app.run(host='0.0.0.0')