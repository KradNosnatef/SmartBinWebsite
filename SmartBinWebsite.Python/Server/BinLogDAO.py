import mysql.connector
import datetime
  
mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'fuqianshan',
    password = 'KRPCGroup',
    database = 'smartbin'
)

class BinLogDAO:
    

    #register the bin into the database and return BID
    def BinRigister(latitude,longitude):
        cursor=mydb.cursor()
        statement = 'INSERT INTO bin (latitude, longitude) VALUES (%s, %s)'
        value = (latitude, longitude)

        cursor.execute(statement, value)
        mydb.commit()
        result=cursor.lastrowid
        cursor.close()

        return result
    

    def insertRawInfo(BID, weight, distance, pitch, roll):
        cursor=mydb.cursor()
        now = datetime.datetime.now()
        timestamp = now.strftime('%Y-%m-%d %H:%M:%S')
        statement = 'INSERT INTO rawInfo (BID, weight, distance, pitch, roll, timestamp) VALUES (%s, %s, %s, %s, %s, %s)'
        value = (BID, weight, distance, pitch, roll, timestamp)
        
        cursor.execute(statement, value)
        mydb.commit()

        cursor.close()
        return 0

    def insertAlert(BID, text):
        cursor=mydb.cursor()
        now = datetime.datetime.now()
        timestamp = now.strftime('%Y-%m-%d %H:%M:%S')
        statement = 'INSERT INTO alert (BID, text, timestamp) VALUES (%s, %s, %s)'
        value = (BID, text, timestamp)
        
        cursor.execute(statement, value)
        mydb.commit()

        cursor.close()
        return 0
    
    def getBinBriefing():
        mydb.commit()

        cursor=mydb.cursor()
        sql="SELECT bin.BID,bin.Latitude,bin.Longitude,TB.nearestAlert from bin left join (select BID, substring_index(group_concat(text order by Timestamp desc),',',1) as nearestAlert from alert group by BID) as TB on bin.BID=TB.BID;"
        cursor.execute(sql)
        result=cursor.fetchall()
        

        result2=[{"BID":row[0],"latitude":row[1],"longitude":row[2],"text":row[3] if row[3]!=None else "No alert yet"} for row in result]

        cursor.close()
        return result2
    
    def getBinAlertListByBID(BID):
        mydb.commit()

        cursor=mydb.cursor()
        sql="SELECT * from alert where BID=%s order by Timestamp desc;"
        val=(BID,)
        cursor.execute(sql,val)

        result=cursor.fetchall()
        cursor.close()
        return result
    
    def getBinRawInfoByBID(BID):
        mydb.commit()
        
        cursor=mydb.cursor()
        sql="SELECT * from rawInfo where BID=%s order by Timestamp desc;"
        val=(BID,)
        cursor.execute(sql,)

        result=cursor.fetchall()
        cursor.close()
        return result
