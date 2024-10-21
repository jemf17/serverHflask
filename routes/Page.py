from flask import Blueprint, jsonify, request
from models.PageModel import PageModel
from models.entities.Page import Page

mainPage = Blueprint('page_blueprint', __name__)

@mainPage.route('/add', methods=['POST'])
def add_page():
    try:
        pass
    except Exception as ex:
        return jsonify({'message':str(ex)}),500

@mainPage.route('/putpage', methods=['PUT']) #o PATCH, no se cual es mejor xd
def upload_page():
    try:
        pass
    except Exception as ex:
        return jsonify({'message':str(ex)}),500
    
@mainPage.route('/delete', methods=['DELETE'])
def delete_page():
    try:
        pass
    except Exception as ex:
        return jsonify({'message':str(ex)}),500