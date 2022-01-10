from common.connection import get_connection, liberar_conexion, get_cursor

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


    #def registrar_cobro(self, )