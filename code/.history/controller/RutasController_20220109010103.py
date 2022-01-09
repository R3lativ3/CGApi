from flask import Blueprint
from service.RutasService import RutasService
rutas_blueprint = Blueprint('rutas_blueprint', __name__)

@rutas_blueprint.route('/cambio')
def index():
    n = RutasService()
    return n.hi()

@rutas_blueprint.route('/')
def hi():
    return "nueva ruta"