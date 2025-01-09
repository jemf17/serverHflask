from fastapi import APIRouter, UploadFile, Path, Body, HTTPException
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

@mainComent.delete('/{id_coment}/{token_user}')
async def delete_coment_id(id_coment: UUID = Path(...)):
    try:
        afect_rows = ComentarioModel.delete_coment(id_coment)
        if afect_rows == 0:
            raise HTTPException(status_code=404, detail="Item not found")
        return {'message':"Ok"}
    except Exception as ex:
        return {'message':str(ex),'status':500}
@mainComent.get('/{user}')
async def get_coment_user(user):
    try:
        return ComentarioModel().get_all_coments_by_user(user)
    except Exception as ex:
        return {'message':str(ex),'status':500}

@mainComent.get('/{obra}')
async def get_coment_obra(obra: UUID = Path(...)):
    try:
        return {'comentarios':ComentarioModel().get_all_coments_by_obra(obra)}
    except Exception as ex:
        return {'message':str(ex),'status':500}