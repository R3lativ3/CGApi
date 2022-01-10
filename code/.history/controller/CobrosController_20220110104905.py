from flask import Blueprint, json, jsonify, request
from service.CobrosService import CobrosService
from datetime import datetime

from common.connection import get_connection, liberar_conexion, liberar_conexion_commit, get_cursor

cobros_bp = Blueprint('cobros_bp', __name__)
cobros_service = CobrosService()

#   Enpoint o ruta para mostrar todos los cobros
@cobros_bp.route('/')
def index():
    cobros = cobros_service.get_cobros()
    print(cobros)
    return jsonify({'Rutas:': cobros})

#   Enpoint o ruta para agregar un cobro
@cobros_bp.route('agregar-cobro', methods=['post'])
def add_cobro():
    cobro = cobros_service.es_cobro(request)
    print(cobro)
    if cobro is None :  return jsonify({'error': "invalid request"}), 400 
    id = cobros_service.add_cobro(cobro)
    return jsonify({'Cobro': id})


#   Ejemplo de insercion
#   El primer parametro es el nombre con el que se expondra la ruta,
#   El segundo parametro es con el tipo de metodo que se expondra la ruta.
@cobros_bp.route('agregar-cobro-sin-refactor', methods=['post'])
def add_cobro2():
    #   Paso 1: Obtener los valores que nos envia el cliente (una pagina, una app, otro sistema, etc...)
    peticion_cobro = request.json['cobro']
    peticion_latitud = request.json['latitud']
    peticion_longitud = request.json['longitud']
    peticion_id_prestamo = request.json['prestamo']

    #   Paso 2: Validar si viene almenos el monto a abonar y el credito al cual se abonar'a
    if(bool(peticion_id_prestamo) == False and bool(peticion_cobro) == False):
        #   Si no viene, devolver un BadRequest
        return jsonify({'error': "invalid request"}), 400 

    #   Crear un diccionario con la informacion que nos envio el cliente
    cobro = {
        "cobro": peticion_cobro,
        "lat": peticion_latitud,
        "lon": peticion_longitud,
        "fecha": datetime.now(), #strftime("%d/%m/%Y %H:%M:%S")
        "idPrestamo": peticion_id_prestamo
    }

    #   Paso 3 (acceso a la base de datos): Crear una conexion a la base de datos
    connection = get_connection()
    #   Crear un cursor, el cual nos servira para manejar o escribir en la base de datos
    cursor = connection.cursor()
    #   Definir el query o instruccion que queremos realizar en base de datos
    #   Notese que los valores a insertar deben coincidir con los del diccionario previamente creado
    add_cobro = ("INSERT INTO CobrosPrestamos "
                "(cobro, lat, lon, fecha, idPrestamo)  "
                "VALUES (%(cobro)s, %(lat)s, %(lon)s, %(fecha)s, %(idPrestamo)s)")
    #   Ejecutar el query, pasandole la instruccion y como segundo parametro la informacion a insertar
    cursor.execute(add_cobro, cobro)
    #   Obtener id insertado
    id = cursor.lastrowid
    #   Realizar un commit para indicar que si queremos registrar los cambios en bd, si no se realiza esta instruccion los cambios
    #   No se veran reflejados en base de datos
    connection.commit()
    #   Cerrar el cursor y la conexion
    cursor.close()
    connection.close()
    
    return jsonify({'Cobro': id})


#   Ejemplo de consulta
#   Si no se especifica el tipo de acceso, se sobreentiende que serà del tipo GET
@cobros_bp.route('/cobro-ejemplo')
def index2():
    #   Paso 1 (acceso a la base de datos): Crear una conexion a la base de datos
    connection = get_connection()
    #   Crear un cursor, el cual nos servira para manejar o escribir en la base de datos, 
    #   dictionary = True para que nos muestre los encabezados de la tabla
    cursor = connection.cursor(buffered=True , dictionary=True)
    #   Definir el query o instruccion que queremos realizar en base de datos
    select_cobros = "SELECT * FROM CobrosPrestamos"
    #   Ejecutar la consulta
    cursor.execute(select_cobros)
    #   Almacenar en una variable la consulta realizada
    data = cursor.fetchall()
    #   Cerrar el cursor y la conexion
    cursor.close()
    connection.close()

    #   Retornar como JSON el diccionario con la informacion
    return jsonify({'Cobros:': data})