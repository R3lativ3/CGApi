from flask import Blueprint, jsonify, request
from service.RutasService import RutasService

rutas_blueprint = Blueprint('rutas_blueprint', __name__)
rutas_service = RutasService()

@rutas_blueprint.route('/cambio')
def index():
    rutas = rutas_service.obtener_rutas()
    return jsonify({'Rutas:': rutas})

#   Endpoint o ruta para agregar una ruta
@rutas_blueprint.route('/agregar_ruta', methods=['post'])
def add_ruta():
    #   obtener diccionario de ruta en base al request enviado desde el cliente
    ruta = rutas_service.es_ruta(request)
    #   retornar invalid request si lo enviado por el cliente no es una ruta valida
    if ruta is None :  return jsonify({'error': "invalid request"}), 400
    #   almacenar id retornado de la insercion de la ruta
    id = rutas_service.agregar_ruta(ruta)
    return jsonify({'Id': id}), 201