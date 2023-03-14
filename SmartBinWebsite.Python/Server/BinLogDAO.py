import mysql.connector
import datetime
  
mydb = mysql.connector.connect(
    host = 'fuqianshan.asuscomm.com',
    user = 'fuqianshan',
    password = 'KRPCGroup',
    database = 'smartbin'
)
  
cursor = mydb.cursor()

class BinLogDAO:

    #register the bin into the database and return BID
    def BinRigister(latitude,longitude):
        statement = 'INSERT INTO bin (latitude, longitude) VALUES (%s, %s)'
        value = (latitude, longitude)

        cursor.execute(statement, value)
        mydb.commit()

        return cursor.lastrowid
    

    def insertRawInfo(BID, weight, distance, pitch, roll):
        now = datetime.datetime.now()
        timestamp = now.strftime('%Y-%m-%d %H:%M:%S')
        statement = 'INSERT INTO rawInfo (BID, weight, distance, pitch, roll, timestamp) VALUES (%s, %s, %s, %s, %s, %s)'
        value = (BID, weight, distance, pitch, roll, timestamp)
        
        cursor.execute(statement, value)
        mydb.commit()

        return 0

    def insertAlert(BID, text):
        now = datetime.datetime.now()
        timestamp = now.strftime('%Y-%m-%d %H:%M:%S')
        statement = 'INSERT INTO alert (BID, text, timestamp) VALUES (%s, %s, %s)'
        value = (BID, text, timestamp)
        
        cursor.execute(statement, value)
        mydb.commit()

        return 0
