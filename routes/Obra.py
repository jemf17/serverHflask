from flask import Blueprint, jsonify

main = Blueprint('obra_blueprint', __name__)

#retorna una obra por id
@main.route('/<id>')
def get_obra_id(id):
    try:
        return jsonify({'tu':id})
    except Exception as ex:
        return jsonify({'message':str(ex)}),500
#retorna un conjunto de obras con el to_JSON_view recomendadas para un usuario que no esta logueado
@main.route('/')
def get_obras():
    try:
        return jsonify({'tu':"mamaxdxdxd"})
    except Exception as ex:
        return jsonify({'message':str(ex)}),500

#retorna un conjunto de obras con el to_JSON_view recomendasas por basada en sus tags mas buscados y en las vistas de otros usuarios con su mismas o parecidos gustos , para usuarios logeados
@main.route('/user/<id>')
def get_obras_for_user(id):
    try:
        return jsonify({'tu':"mama"})
    except Exception as ex:
        return jsonify({'message':str(ex)}),500
#retorna todas las obras que hizo el artista
@main.route('/artist/<id>')
def get_obras_for_artist(id):
    try:
        return jsonify({'tu':"mama"})
    except Exception as ex:
        return jsonify({'message':str(ex)}),500
    
#registra una obra, hay que ver si puede estar vacia o no, pero de que la agrega, la agrega
@main.route('/add', methods=['POST'])
def add_obra():
    try:
        pass
    except Exception as ex:
        return jsonify({'message':str(ex)}),500

#elimina una obra en espesifico por si hay un artista takito y decile eliminar su obra maestra *incerte cara de moai*
@main.route('/delete/<id>', methods=['DELETE'])
def delete_obra(id):
    try:
        pass
    except Exception as ex:
        return jsonify({'message':str(ex)}),500

#actualiza una obra por id, ya sea por que quiera actualizar la portada, el nombre o qsy    
@main.route('/update/<id>', methods=['PUT'])
def update_obra(id):
    try:
        pass
    except Exception as ex:
        return jsonify({'message':str(ex)}),500
    