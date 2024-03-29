import mysql.connector
import datetime
  
mydb = mysql.connector.connect(
    host = 'fuqianshan.asuscomm.com',
    user = 'fuqianshan',
    password = 'KRPCGroup',
    database = 'smartbin'
)

class BinLogDAO:
    def reconnect():
        global mydb
        mydb = mysql.connector.connect(
            host = 'fuqianshan.asuscomm.com',
            user = 'fuqianshan',
            password = 'KRPCGroup',
            database = 'smartbin'
        )

    #register the bin into the database and return BID
    def BinRigister(latitude,longitude):
        try:
            cursor=mydb.cursor()
            statement = 'INSERT INTO bin (latitude, longitude) VALUES (%s, %s)'
            value = (latitude, longitude)

            cursor.execute(statement, value)
            mydb.commit()
            result=cursor.lastrowid
            cursor.close()

            return result
        except:
            BinLogDAO.reconnect()
            return BinLogDAO.BinRigister(latitude,longitude)
    

    def insertRawInfo(BID, weight, distance, pitch, roll):
        try:
            cursor=mydb.cursor()
            now = datetime.datetime.now()
            timestamp = now.strftime('%Y-%m-%d %H:%M:%S')
            statement = 'INSERT INTO rawInfo (BID, weight, distance, pitch, roll, timestamp) VALUES (%s, %s, %s, %s, %s, %s)'
            value = (BID, weight, distance, pitch, roll, timestamp)
            
            cursor.execute(statement, value)
            mydb.commit()

            cursor.close()
            return 0
        except:
            BinLogDAO.reconnect()
            return BinLogDAO.insertAlert(BID, weight, distance, pitch, roll)

    def insertAlert(BID, text):
        try:
            cursor=mydb.cursor()
            now = datetime.datetime.now()
            timestamp = now.strftime('%Y-%m-%d %H:%M:%S')
            statement = 'INSERT INTO alert (BID, text, timestamp) VALUES (%s, %s, %s)'
            value = (BID, text, timestamp)
            
            cursor.execute(statement, value)
            mydb.commit()

            cursor.close()
            return 0
        except:
            BinLogDAO.reconnect()
            return BinLogDAO.insertAlert(BID, text)

    def getBinBriefing():
        try:
            #print("?1")
            mydb.commit()
            #print("?2")

            cursor=mydb.cursor()
            sql="SELECT bin.BID,bin.Latitude,bin.Longitude,TB.nearestAlert from bin left join (select BID, substring_index(group_concat(text order by Timestamp desc),',',1) as nearestAlert from alert group by BID) as TB on bin.BID=TB.BID;"
            cursor.execute(sql)
            result=cursor.fetchall()
            
            result2=[{"BID":row[0],"latitude":row[1],"longitude":row[2],"text":row[3] if row[3]!=None else "No alert yet"} for row in result]

            sql="SELECT bin.BID,TB.nearestDistance from bin left join (select BID, substring_index(group_concat(distance order by Timestamp desc),',',1) as nearestDistance from rawInfo group by BID) as TB on bin.BID=TB.BID;"
            cursor.execute(sql)
            result=cursor.fetchall()
            nearestDistanceDictionary={}
            for row in result:
                nearestDistanceDictionary[str(row[0])]=row[1]

            for row in result2:
                if str(row["BID"]) in nearestDistanceDictionary:
                    row["nearestDistance"]=nearestDistanceDictionary[str(row["BID"])]

            cursor.close()

            result=BinLogDAO.getRecentReportTimeToNowBriefing()
            nearestReportTimeDictionary={}
            for row in result:
                nearestReportTimeDictionary[str(row[0])]=row[1]

            for row in result2:
                if str(row["BID"]) in nearestReportTimeDictionary:
                    row["nearestReportTime"]=nearestReportTimeDictionary[str(row["BID"])]
            return result2
        except:
            print("getBinBriefing failed")
            BinLogDAO.reconnect()
            return BinLogDAO.getBinBriefing()
    
    #return list[(Text,TimeText)] order by time desc 
    def getAlertsByBID(BID):
        try:
            mydb.commit()

            cursor=mydb.cursor()
            sql="SELECT Text,cast(Timestamp as char(20)) from alert where BID=%s order by Timestamp desc;"
            val=(BID,)
            cursor.execute(sql,val)

            result=cursor.fetchall()
            cursor.close()
            return result
        except:
            BinLogDAO.reconnect()
            return BinLogDAO.getAlertsByBID(BID)
    
    def getRawInfoByBID(BID):
        try:
            mydb.commit()

            cursor=mydb.cursor()
            sql="SELECT Weight,Distance,Pitch,Roll,cast(Timestamp as char(20)) from rawInfo where BID=%s order by Timestamp desc limit 0,1000;"
            val=(BID,)
            cursor.execute(sql,val)

            result=cursor.fetchall()
            cursor.close()
            return result
        except:
            print("getRawInfoByBID failed")
            BinLogDAO.reconnect()
            return BinLogDAO.getRawInfoByBID(BID)
        
    #input a DateTimeText and return seconds to Now
    def getSecondToNow(dateTimeText):
        try:
            mydb.commit()

            cursor=mydb.cursor()
            sql="SELECT TIMESTAMPDIFF(SECOND,%s,NOW());"
            val=(dateTimeText,)
            cursor.execute(sql,val)

            result=cursor.fetchall()
            cursor.close()
            return result
        except:
            BinLogDAO.reconnect()
            return BinLogDAO.getSecondToNow(dateTimeText)
        
    def getRecentReportTimeToNowBriefing():
        try:
            mydb.commit()

            cursor=mydb.cursor()
            sql="SELECT BID,TIMESTAMPDIFF(SECOND,CAST(MAX(Timestamp) as char(20)),NOW()) from rawInfo group by BID;"
            cursor.execute(sql)

            result=cursor.fetchall()
            cursor.close()
            return result
        except:
            BinLogDAO.reconnect()
            return BinLogDAO.getRecentReportTimeToNowBriefing()