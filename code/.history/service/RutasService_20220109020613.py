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

    def es_ruta(self, request):
        try:
            rutax = request.json['ruta']
            id_departamento = request.json['departamento']
            id_municipio = request.json['municipio']

            if(bool(rutax) and bool(id_departamento) and bool(id_municipio)):
                return {
                    "rutax": rutax,
                    "id_departamento": id_departamento,
                    "id_municipio": id_municipio
                }
            
            return 1
        except Exception as e:
            return 'error'