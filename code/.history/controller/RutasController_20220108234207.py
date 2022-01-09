from flask import Blueprint
from service.RutasService import RutasService
rutas_blueprint = Blueprint('rutas_blueprint', __name__)

@rutas_blueprint.route('/')
def index():
    n = RutasService()
    return n.hi()