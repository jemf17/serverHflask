from fastapi import APIRouter, UploadFile, Path, Body
from models.ArtistModel import ArtistModel
from models.UsuarioModel import UsuarioModel
from models.TraductorModel import TraductorModel

mainUser = APIRouter(prefix="/user", tags=['users'], responses={404: {"description": "Not found"}})