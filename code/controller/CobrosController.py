from flask import Blueprint, jsonify, request
from service.CobrosService import CobrosService

cobros_bp = Blueprint('cobros_bp', __name__)
cobros_service = CobrosService()

#   Enpoint o ruta para mostrar todos los cobros
@cobros_bp.route('/')
def index():
    cobros = cobros_service.get_cobros()
    print(cobros)
    return jsonify({'Rutas:': cobros})
