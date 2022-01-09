from flask import Blueprint, jsonify, request
from service.RutasService import RutasService
rutas_blueprint = Blueprint('rutas_blueprint', __name__)

@rutas_blueprint.route('/cambio')
def index():
    n = RutasService()
    return n.hi()

@rutas_blueprint.route('/agregar_ruta', methods=['post'])
def add_ruta():
    rutas_service = RutasService()
    print(request.get_json)
    ruta = request.json['ruta']
    id_departamento = request.json['departamento']
    id_municipio = request.json['municipio']

    id = rutas_service.agregar_ruta(ruta, id_departamento, id_municipio)

    return jsonify({'id_ruta_added': id})