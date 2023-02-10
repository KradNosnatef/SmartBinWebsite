from flask import Flask
from flask import request
from flask_cors import *
import json
import requests

message={"data":"No Data"}
app=Flask(__name__)

@app.route('/home')
def helloWorld():
    return(message["data"])

@app.route('/Xapi',methods=['POST'])
def Xapi():
    message["data"]=request.form["data"]
    print(message["data"])
    return "Success"

if __name__ == '__main__':
   app.run(debug = True)