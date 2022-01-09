from flask import Flask, jsonify, request
from config import config
from common.connection import get_connection
from controller.RutasController import rutas_blueprint 

app = Flask(__name__)
app.register_blueprint(rutas_blueprint, url_prefix='/rutas')

@app.route("/")
def index():
    cnx = get_connection()
    cursor = cnx.cursor()

    query = ("select * from rutas")
    cursor.execute(query)
    data = cursor.fetchall()
    return jsonify({'rutas': data})


@app.route("/post", methods=['POST'])
def post():
    departamento = request.json['departamento']
    add =   """ 
            INSERT INTO departamentos (departamento) VALUES ('{0}')
            """.format(departamento)
    cnx = getConnection()                           #obtengo conexion
    cursor = cnx.cursor()                           #cursor
    cursor.execute(add)                             #ejecuto el insert, seguido de lo que insertare
    id = cursor.lastrowid                           #obtener id insertado                    
    print(id)         
    cnx.commit()                                          #guardar cambios
    cursor.close()                                        #cerrar conexion y cursor
    cnx.close()
    return jsonify({'id': id})


if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.run()