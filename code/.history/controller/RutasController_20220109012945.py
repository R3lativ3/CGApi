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
    ruta = rutas_service.es_ruta(request.get_json())
    print("esta es la ruta: "+str(ruta))
    #    id = rutas_service.agregar_ruta(ruta, id_departamento, id_municipio)

    return jsonify({'id_ruta_added': 2}), 201