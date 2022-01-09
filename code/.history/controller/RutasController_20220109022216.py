from flask import Blueprint, jsonify, request
from service.RutasService import RutasService

rutas_blueprint = Blueprint('rutas_blueprint', __name__)
rutas_service = RutasService()

@rutas_blueprint.route('/cambio')
def index():
    return rutas_service.hi()

@rutas_blueprint.route('/agregar_ruta', methods=['post'])
def add_ruta():

    ruta = rutas_service.es_ruta(request)
    if ruta is None :  return jsonify({'error': "invalid request"}), 400
    id = rutas_service.agregar_ruta(ruta)
    return jsonify({'Id': id}), 201