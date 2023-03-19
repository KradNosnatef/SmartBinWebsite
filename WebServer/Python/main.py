from flask import Flask
from flask import request
from flask_cors import *
from BinLogDAO import *
import json

message={"data":"No Data"}
app=Flask(__name__)

@app.route('/home')
def helloWorld():
    return(message["data"])

@app.route('/Tapi',methods=['POST'])
@cross_origin()
def Tapi():
    print(request.data.decode)
    return("helloWorld")

@app.route('/Xapi/postReport',methods=['POST'])
def postReport():
    message["data"]+=request.form["data"]
    
    dataObject=json.loads(request.form["data"])

    if dataObject["BID"]==-1:
        dataObject["BID"]=BinLogDAO.BinRigister(dataObject["latitude"],dataObject["longitude"])

    BinLogDAO.insertRawInfo(dataObject["BID"],dataObject["weight"],dataObject["distance"],dataObject["pitch"],dataObject["roll"])
    #if dataObject["alert0"]==1:BinLogDAO.insertAlert(dataObject["BID"],"SwitchDoor Detected")
    #if dataObject["alert1"]==1:BinLogDAO.insertAlert(dataObject["BID"],"Vibration Detected")
    #if dataObject["alert2"]==1:BinLogDAO.insertAlert(dataObject["BID"],"Abnormal Attitude Detected")

    return str(dataObject["BID"])

@app.route('/Xapi/postAlert',methods=['POST'])
def postAlert():
    message["data"]+=request.form["data"]
    dataObject=json.loads(request.form["data"])
    if dataObject["alert0"]==1:BinLogDAO.insertAlert(dataObject["BID"],"SwitchDoor Detected")
    if dataObject["alert1"]==1:BinLogDAO.insertAlert(dataObject["BID"],"Vibration Detected")
    if dataObject["alert2"]==1:BinLogDAO.insertAlert(dataObject["BID"],"Abnormal Attitude Detected")
    return 'success'


@app.route('/Wapi/getBinBriefing')
@cross_origin()
def getBinBriefing():
    return(json.dumps(BinLogDAO.getBinBriefing()))

@app.route('/Wapi/getAlertsByBID',methods=['POST'])
@cross_origin()
def getAlertsByBID():
    print(request.data.decode())
    dataObject=json.loads(request.data.decode())


    
    result=json.dumps(BinLogDAO.getAlertsByBID(int(dataObject['BID'])))
    return result

@app.route('/Wapi/getRawInfoByBID',methods=['POST'])
@cross_origin()
def getRawInfoByBID():
    print(request.data.decode())
    dataObject=json.loads(request.data.decode())

    result=json.dumps(BinLogDAO.getRawInfoByBID(int(dataObject['BID'])))
    return result


#if __name__ == '__main__':
   #app.run(host='0.0.0.0')