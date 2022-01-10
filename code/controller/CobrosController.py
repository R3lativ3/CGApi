from flask import Blueprint, json, jsonify, request
from service.CobrosService import CobrosService

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