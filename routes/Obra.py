from flask import Blueprint, jsonify

main = Blueprint('obra_blueprint', __name__)

@main.route('/:id')
def get_obra_id():
    return jsonify({'tu':"mama"})