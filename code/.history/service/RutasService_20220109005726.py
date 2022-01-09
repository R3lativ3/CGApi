from os import getcwd
from common.connection import getConnection

class RutasService():

    def hi(self):
        return "hi"

    def agregar_ruta(self, nombreRuta, idSede, idMunicipio):
        try:
            connection = getConnection()
            cursor = connection.getcursor()
            add_ruta =   """ 
                    INSERT INTO rutas (nombreRuta, idSede, idMunicipio) 
                                VALUES ('{0}', {1}, {2})
                    """.format(nombreRuta, idSede, idMunicipio)

            cursor.execute(add_ruta)
            id = cursor.lastrowid
            self.liberar_conexion(connection, cursor)
            return id
        except Exception as e:
            return e

    def liberar_conexion(self, connection, cursor):
        connection.commit()
        cursor.close()
        connection.close()