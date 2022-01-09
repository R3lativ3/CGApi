from flask import Blueprint, jsonify
from service.RutasService import RutasService
rutas_blueprint = Blueprint('rutas_blueprint', __name__)

@rutas_blueprint.route('/cambio')
def index():
    n = RutasService()
    return n.hi()

@rutas_blueprint.route('/agregar_ruta', methods=['post'])
def add_ruta():
    rutas_service = RutasService()
    id = rutas_service.agregar_ruta("jose",1,1)
    return jsonify({'id_ruta_added': id})