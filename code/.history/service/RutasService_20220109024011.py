from common.connection import get_connection, liberar_conexion

class RutasService():

    def obtener_rutas(self):
        try:
            connection = get_connection()
            cursor = connection.cursor()

            select_ruta = ("""  SELECT a.nombreRuta, b.sede, c.municipio 
                                FROM rutas a, sedesGold b, municipios c 
                                WHERE a.idSede = b.id and a.idMunicipio = c.id """)
            cursor.execute(select_ruta)
            data = cursor.fetchall()
            return data
        except Exception as e:
            return e

    #Funcion para registrar una ruta
    def agregar_ruta(self, ruta):
        try:
            connection = get_connection()
            cursor = connection.cursor()
            add_ruta = ("INSERT INTO rutas "
                        "(nombreRuta, idSede, idMunicipio) "
                        "VALUES (%(ruta)s, %(idSede)s, %(idMunicipio)s)")

            cursor.execute(add_ruta, ruta)
            #obtener id insertado
            id = cursor.lastrowid   
            print(id)
            #Ejecutar commit, liberar conexion y cursor
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
                #retornar diccionario que servira para pasar como parametro en funcion 'agregar_ruta'
                return {
                    "ruta": rutax,
                    "idSede": id_departamento,
                    "idMunicipio": id_municipio
                }

            return None
        except Exception as e:
            print(e)
            return None