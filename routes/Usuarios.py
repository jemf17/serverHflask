from flask import Blueprint, jsonify, request
from models.ArtistModel import ArtistModel
from models.UsuarioModel import UsuarioModel
from models.TraductorModel import TraductorModel

mainUser = Blueprint('users_blueprint', __name__)