from flask import Blueprint, jsonify, request
from models.ObraModel import ObraModel
from models.entities.Obra import Obra
from models.entities.Capitulo import Capitulo
import uuid

mainObra = Blueprint('obra_blueprint', __name__)

#retorna una obra por id
@mainObra.route('/<id>')
def get_obra_id(id):
    try:
        obra = ObraModel.get_obra(id)
        if obra == None:
            return jsonify({'message': None})
        return jsonify(obra)
    except Exception as ex:
        return jsonify({'message':str(ex)}),500
#retorna un conjunto de obras con el to_JSON_view recomendadas para un usuario que no esta logueado
@mainObra.route('/')
def get_obras():
    try:
        obras = ObraModel.get_obras()
        print(obras)
        if obras == []:
            return jsonify({'message': None})
        return jsonify(obras)
    except Exception as ex:
        return jsonify({'message':str(ex)}),500

#retorna un conjunto de obras con el to_JSON_view recomendasas por basada en sus tags mas buscados y en las vistas de otros usuarios con su mismas o parecidos gustos , para usuarios logeados
@mainObra.route('/user/<id>')
def get_obras_for_user(id):
    try:
        return jsonify({'tu':"mama"})
    except Exception as ex:
        return jsonify({'message':str(ex)}),500
#retorna todas las obras que hizo el artista
@mainObra.route('/<artist>/<id>')
def get_obras_for_artist(artist,id):
    try:
        return jsonify({'tu':"mama"})
    except Exception as ex:
        return jsonify({'message':str(ex)}),500
    
#registra una obra, hay que ver si puede estar vacia o no, pero de que la agrega, la agrega
@mainObra.route('/add', methods=['POST'])
def add_obra():
    try:
        obra = Obra(uuid.UUID(request.json['id']), request.json['title'],request.json['secondtitle'], request.json['portada'], request.json['oneshot'], request.json['madure'])
        cap = Capitulo(request.json['numero'], request.json['fecha'], request.json['idioma'], request.json['pages'])
        affec_row = ObraModel.add_obra(obra, request.json['tags'],uuid.UUID(request.json['artista']), cap)
        if affec_row == 0:
            return jsonify({'message': "Error on insert"})
        return jsonify({'message':"Ok"})
    except Exception as ex:
        return jsonify({'message':str(ex)}),500

#elimina una obra en espesifico por si hay un artista takito y decile eliminar su obra maestra *incerte cara de moai*
@mainObra.route('/delete/<id>', methods=['DELETE'])
def delete_obra(id):
    try:
        pass
    except Exception as ex:
        return jsonify({'message':str(ex)}),500

#actualiza una obra por id, ya sea por que quiera actualizar la portada, el nombre o qsy    
@mainObra.route('/update/<id>', methods=['PUT'])
def update_obra(id):
    try:
        pass
    except Exception as ex:
        return jsonify({'message':str(ex)}),500

    
@mainObra.route('/exist')
def exist_obra():
    try:
        title = request.args.get('title').replace('-', ' ')
        print(title)
        return jsonify({'exist':ObraModel.exist_obra(title)})
    except Exception as ex:
        return jsonify({'message':str(ex)}),500

@mainObra.route('/getuuid')
def create_uuid():
    try:
        return jsonify(ObraModel.create_uuid())
    except Exception as ex:
        return jsonify({'message':str(ex)}),500

@mainObra.route('/save/<id_obra>/<id_user>')
def save(id_obra, id_user):
    try:
        ObraModel.save_obra(id_obra, id_user)
        return jsonify({'message': 'Ok'})
    except Exception as ex:
        return jsonify({'message':str(ex)}),500

@mainObra.route('/fav/<id_obra>/<id_user>')
def fav(id_obra, id_user):
    try:
        ObraModel.like_obra(id_obra, id_user)
        return jsonify({'message': 'Ok'})
    except Exception as ex:
        return jsonify({'message':str(ex)}),500
