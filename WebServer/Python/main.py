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

@app.route('/Xapi',methods=['POST'])
def Xapi():
    message["data"]+=request.form["data"]
    
    dataObject=json.loads(request.form["data"])

    if dataObject["BID"]==-1:
        dataObject["BID"]=BinLogDAO.BinRigister(dataObject["latitude"],["longitude"])

    BinLogDAO.insertRawInfo(dataObject["BID"],dataObject["weight"],dataObject["distance"],dataObject["pitch"],dataObject["roll"])
    if dataObject["alert0"]==1:BinLogDAO.insertAlert(dataObject["BID"],"SwitchDoor Detected")
    if dataObject["alert1"]==1:BinLogDAO.insertAlert(dataObject["BID"],"Vibration Detected")

    return str(dataObject["BID"])

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

if __name__ == '__main__':
   app.run(host='0.0.0.0')