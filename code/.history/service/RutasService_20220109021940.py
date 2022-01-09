from common.connection import get_connection, liberar_conexion

class RutasService():

    def hi(self):
        return "hi"

    def agregar_ruta(self, ruta):
        try:
            connection = get_connection()
            cursor = connection.cursor()
            add_ruta = ("INSERT INTO rutas "
                        "(nombreRuta, idSede, idMunicipio) "
                        "VALUES (%(ruta)s, %(departamento)s, %(municipio)s)")

            cursor.execute(add_ruta, ruta)
            id = cursor.lastrowid
            print(id)
            liberar_conexion(connection, cursor)
            return id
        except Exception as e:
            return e

    #Funcion para validar si los parametros enviados son los esperados en el backend
    def es_ruta(self, request):                                                 
        try:
            rutax = request.json['ruta']
            id_departamento = request.json['departamento']
            id_municipio = request.json['municipio']

            #si todos los campos contienen algo:
            if(bool(rutax) and bool(id_departamento) and bool(id_municipio)):
                return {
                    "ruta": rutax,
                    "departamento": id_departamento,
                    "municipio": id_municipio
                }

            return None
        except Exception as e:
            print(e)
            return None