from fastapi import APIRouter, UploadFile, Path, Body
from models.entities.Comentario import *
from models.ComentarioModel import ComentarioModel
from uuid import UUID
mainComent = APIRouter(prefix="/coment", tags=['comentario'], responses={404: {"description": "Not found"}})

@mainComent.post('/addcoment')
async def add_coment(fecha: str = Body(...), desc: str = Body(...), user: UUID=Body(...), obra: UUID=Body(...)):
    try:
        comentario = ContextComentario(ComentUser(fecha,desc, user))
        afect_rows = ComentarioModel.add_coment(obra, comentario)
        if afect_rows == 0:
            return {'message': "Error on insert"}
        return {'message':"Ok"}
    except Exception as ex:
        return {'message':str(ex),'status':500}

@mainComent.route('/<id>', methods=['DELETE'])
async def delete_coment_id(id):
    try:
        return {'tu':"mama"}
    except Exception as ex:
        return {'message':str(ex),'status':500}
@mainComent.route('/user/<user>')
async def get_coment_user(user):
    try:
        coments = ComentarioModel().get_all_coments_by_user(user)
        return coments
    except Exception as ex:
        return {'message':str(ex),'status':500}