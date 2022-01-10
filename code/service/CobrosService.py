from common.connection import get_connection, liberar_conexion, liberar_conexion_commit, get_cursor
from datetime import datetime

class CobrosService():

    def get_cobros(self):
        connection = get_connection()
        cursor = get_cursor(connection)
        sql = """
                SELECT 
                    a.cobro,
                    a.lat,
                    a.lon,
                    a.fecha,
                    f.nombres,
                    e.nombreRuta,
                    c.nombres
                FROM 
                    CobrosPrestamos a, 
                    prestamos b, 
                    clientes c,
                    rutasCobradores d,
                    rutas e, 
                    cobradores f
                WHERE 
                    a.idPrestamo = b.id
                    and b.idCliente = c.id
                    and b.idRutaCobrador = d.id
                    and d.idRuta = e.id
                    and d.idCobrador  = f.id
                ORDER BY
                    a.fecha DESC
            """
        cursor.execute(sql)
        data = cursor.fetchall()
        liberar_conexion(connection, cursor)
        return data
        

    def add_cobro(self, cobro):
        connection = get_connection()
        cursor = get_cursor(connection)
        add_ruta = ("INSERT INTO CobrosPrestamos "
            "(cobro, lat, lon, fecha, idPrestamo)  "
            "VALUES (%(cobro)s, %(lat)s, %(lon)s, %(fecha)s, %(idPrestamo)s)")
        cursor.execute(add_ruta, cobro)
        id = cursor.lastrowid
        liberar_conexion_commit(connection, cursor)
        return id


    def es_cobro(self, request):
        try:
            peticion_cobro = request.json['cobro']
            peticion_latitud = request.json['latitud']
            peticion_longitud = request.json['longitud']
            peticion_id_prestamo = request.json['prestamo']

            #   si todos los campos contienen algo:
            if(bool(peticion_cobro) and bool(peticion_id_prestamo)):
                #   retornar diccionario que servira para pasar insertar en funcion 'add_cobro'
                return {
                    "cobro": peticion_cobro,
                    "lat": peticion_latitud,
                    "lon": peticion_longitud,
                    "fecha": datetime.now(), #strftime("%d/%m/%Y %H:%M:%S")
                    "idPrestamo": peticion_id_prestamo
                }

            return None
        except Exception as e:
            print(e)
            return None