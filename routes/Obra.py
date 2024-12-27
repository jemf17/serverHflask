from fastapi import APIRouter, UploadFile, Path, Body
from models.ObraModel import ObraModel
from models.entities.Obra import Obra
from models.entities.Capitulo import Capitulo
from uuid import UUID
from typing import List

mainObra = APIRouter(prefix="/obra", tags=['obra'], responses={404: {"description": "Not found"}})

#retorna una obra por id
@mainObra.get('/{id}')
def get_obra_id(id):
    try:
        obra = ObraModel.get_obra(id)
        if obra == None:
            return {'message': None}
        return {obra}
    except Exception as ex:
        return {'message':str(ex),'status':500}
#retorna un conjunto de obras con el to_JSON_view recomendadas para un usuario que no esta logueado
@mainObra.get('/')
def get_obras():
    try:
        obras = ObraModel.get_obras()
        print(obras)
        if obras == []:
            return {'message': None}
        return {'obras': obras}
    except Exception as ex:
        return {'message':str(ex),'status':500}

#retorna un conjunto de obras con el to_JSON_view recomendasas por basada en sus tags mas buscados y en las vistas de otros usuarios con su mismas o parecidos gustos , para usuarios logeados
@mainObra.get('/user/{id}')
def get_obras_for_user(id: UUID = Path(...)):
    try:
        return {'tu':"mama"}
    except Exception as ex:
        return {'message':str(ex),'status':500}
#retorna todas las obras que hizo el artista
@mainObra.get('/{artist}')
def get_obras_for_artist(artist: UUID = Path(...)):
    try:
        return {'tu':"mama"}
    except Exception as ex:
        return {'message':str(ex),'status':500}
    
#registra una obra, hay que ver si puede estar vacia o no, pero de que la agrega, la agrega
@mainObra.post('/addObra')
def add_obra(id: UUID = Body(...), title: str = Body(...), secondtitle: str = Body(...), portada: str = Body(...), oneshot: bool = Body(...), madure: bool = Body(...), 
            tags: List[str] = Body(...), artista: UUID = Body(...), numero: int = Body(...), fecha: str = Body(...), idioma: str = Body(...), pages: List[str] = Body(...)):
    try:
        obra = Obra(id, title,secondtitle, portada, oneshot, madure)
        cap = Capitulo(numero, fecha, idioma, pages)
        affec_row = ObraModel.add_obra(obra, tags,artista, cap)
        if affec_row == 0:
            return {'message': "Error on insert"}
        return {'message':"Ok"}
    except Exception as ex:
        return {'message':str(ex),'status':500}

#elimina una obra en espesifico por si hay un artista takito y decile eliminar su obra maestra *incerte cara de moai*
@mainObra.delete('/delete/{id}')
def delete_obra(id: UUID = Path(...)):
    try:
        return {'message': ObraModel.delete_obra(id)}
    except Exception as ex:
        return {'message':str(ex),'status':500}

#actualiza una obra por id, ya sea por que quiera actualizar la portada, el nombre o qsy    
@mainObra.put('/update/{id}')
def update_obra(id: UUID = Path(...), title: str = Body(...), secondtitle: str = Body(...), portada: str = Body(...), oneshot: bool = Body(...), madure: bool = Body(...)):
    try:
        obra = Obra(UUID(id), title,secondtitle,portada,oneshot,madure)
        return {'message': ObraModel.update_obra(obra)}
    except Exception as ex:
        return {'message':str(ex),'status':500}

    
@mainObra.get('/exist/{title}')
def exist_obra(title: str=Path(...)):
    try:
        #title = request.args.get('title').replace('-', ' ')
        #print(title)
        return {'exist':ObraModel.exist_obra(title)}
    except Exception as ex:
        return {'message':str(ex),'status':500}

@mainObra.get('/getuuid')
def create_uuid():
    try:
        return ObraModel.create_uuid()
    except Exception as ex:
        return {'message':str(ex),'status':500}

@mainObra.get('/save/{id_obra}/{id_user}')
def save(id_obra: UUID=Path(...), id_user: UUID=Path(...)):
    try:
        ObraModel.save_obra(id_obra, id_user)
        return {'message': 'Ok'}
    except Exception as ex:
        return {'message':str(ex),'status':500}

@mainObra.get('/fav/{id_obra}/{id_user}')
def fav(id_obra: UUID=Path(...), id_user: UUID=Path(...)):
    try:
        ObraModel.like_obra(id_obra, id_user)
        return {'message': 'Ok'}
    except Exception as ex:
        return {'message':str(ex),'status':500}
