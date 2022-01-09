from flask import Blueprint, jsonify, request
from service.RutasService import RutasService

rutas_blueprint = Blueprint('rutas_blueprint', __name__)
rutas_service = RutasService()

#   Enpoint o ruta para mostrar todas las rutas
@rutas_blueprint.route('/')
def index():
    rutas = rutas_service.obtener_rutas()
    return jsonify({'Rutas:': rutas})


#   Endpoint o ruta para agregar una ruta
@rutas_blueprint.route('/agregar-ruta', methods=['post'])
def add_ruta():
    ruta = rutas_service.es_ruta(request)                                           #   Obtener diccionario de ruta en base al request enviado desde el cliente
    if ruta is None :  return jsonify({'error': "invalid request"}), 400            #   Retornar invalid request si lo enviado por el cliente no es una ruta valida
    id = rutas_service.agregar_ruta(ruta)                                           #   Almacenar id retornado de la insercion de la ruta
    return jsonify({'Id': id}), 201


#   Enpoint que crea una ruta sin validar los parametros de entrada, 
#   la version refactorizada es la de arriba, fn: add_ruta()
@rutas_blueprint.route('/agregar-ruta-sin-validar', methods=['post'])
def add_ruta_sin_validar():
    rutas_service = RutasService()                                                  #   Instancia de clase que contiene la logica

    print(request.get_json())                                                       #   Mostrar el request enviado por el cliente
    ruta = request.json["ruta"]                                                     #   Almacenar en variables los campos esperados (ruta, idSede, idMunicipio)
    id_departamento = request.json["idSede"]
    id_municipio = request.json["idMunicipio"]

    id = rutas_service.agregar_ruta(ruta, id_departamento, id_municipio)

    return jsonify({'id_ruta_added': id})