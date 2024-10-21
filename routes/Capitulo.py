from flask import Blueprint, jsonify, request
from models.CapituloModel import CapituloModel
from models.entities.Capitulo import Capitulo

mainCapi = Blueprint('obra_blueprint', __name__)

@mainCapi.route('/<obra_id>/<numero>')
def get_capi(obra_id, numero):
    try:
        capi = CapituloModel.get_capitulo_by_obra(obra_id, numero)
        return jsonify(capi)
    except Exception as ex:
        return jsonify({'message':str(ex)}),500
    
@mainCapi.route('/add', methods=['POST'])
def add_capitulo():
    try:
        numero = request.json['numero']
        fecha = request.json['fecha']
        idioma = request.json['idioma']
        capi = Capitulo('', numero, fecha, idioma)
        affec_row = CapituloModel.add_capitulo(capi, request.json['obra'])
        if affec_row == 0:
            return jsonify({'message': "Error on insert"})
        return jsonify({'message':"Ok"})
    except Exception as ex:
        return jsonify({'message':str(ex)}),500