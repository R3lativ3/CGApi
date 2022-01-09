import mysql.connector

def getConnection():
    try:
        cnx = mysql.connector.connect(user='root', password='Perromon12',
                                    host='localhost', database='DBGold')
        return cnx
    except Exception as e:
        return e