import mysql.connector
  
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
    

    def insertRawInfo(BID,weight,distance,pitch,roll):
        pass

    def insertAlert(BID,text):
        pass