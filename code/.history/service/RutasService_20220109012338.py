from os import getcwd
from common.connection import getConnection

class RutasService():

    def hi(self):
        return "hi"

    def agregar_ruta(self, nombreRuta, idSede, idMunicipio):
        try:
            connection = getConnection()
            cursor = connection.cursor()
            add_ruta =   """ 
                    INSERT INTO rutas (nombreRuta, idSede, idMunicipio) 
                                VALUES ('{0}', {1}, {2})
                    """.format(nombreRuta, idSede, idMunicipio)

            cursor.execute(add_ruta)
            id = cursor.lastrowid
            print(id)
            self.liberar_conexion(connection, cursor)
            return id
        except Exception as e:
            return e

    def liberar_conexion(self, connection, cursor):
        connection.commit()
        cursor.close()
        connection.close()

    def es_ruta(request):
        try:
            ruta = request.json["ruta"]
            id_departamento = request.json["departamento"]
            id_municipio = request.json["municipio"]

            if(ruta and id_departamento and id_municipio):
                return {
                    "ruta": ruta,
                    "id_departamento": id_departamento,
                    "id_municipio": id_municipio
                }
            
            return None
        except Exception as e:
            return e