from flask import Blueprint, jsonify, request
from models.entities.Comentario import *
from models.ComentarioModel import ComentarioModel
import uuid

mainComent = Blueprint('coment_blueprint', __name__)

@mainComent.route('/', methods=['POST'])
def add_coment():
    try:
        return jsonify({'tu':"mama"})
    except Exception as ex:
        return jsonify({'message':str(ex)}),500

@mainComent.route('/<id>', methods=['DELETE'])
def delete_coment_id(id):
    try:
        return jsonify({'tu':"mama"})
    except Exception as ex:
        return jsonify({'message':str(ex)}),500
@mainComent.route('/user/<user>')
def get_coment_user(user):
    try:
        coments = ComentarioModel().get_all_coments_by_user(user)
        return jsonify(coments)
    except Exception as ex:
        return jsonify({'message':str(ex)}),500