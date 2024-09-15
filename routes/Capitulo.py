from flask import Blueprint, jsonify, request
from models.CapituloModel import CapituloModel

mainCapi = Blueprint('obra_blueprint', __name__)

@mainCapi.route('/<obra_id>/<numero>')
def get_capi(obra_id, numero):
    try:
        capi = CapituloModel.get_capitulo_by_obra(obra_id, numero)
        return jsonify(capi)
    except Exception as ex:
        return jsonify({'message':str(ex)}),500