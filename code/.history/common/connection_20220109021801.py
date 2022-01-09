import mysql.connector

def get_connection():
    try:
        cnx = mysql.connector.connect(user='ueksr5gb2ucn0psn', password='P7me8wfy5lb5FaUYcXW2',
                                    host='bapakqf1x9lue5zajbt6-mysql.services.clever-cloud.com', database='bapakqf1x9lue5zajbt6')
        return cnx
    except Exception as e:
        return e


def liberar_conexion(connection, cursor):
    connection.commit()
    cursor.close()
    connection.close()