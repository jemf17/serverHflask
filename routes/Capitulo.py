from fastapi import APIRouter, UploadFile, Path, Body, HTTPException
from models.CapituloModel import CapituloModel, StrategyCapituloArts, StrategyCapituloScan
from models.entities.Capitulo import Capitulo
from helper.sb_help import get_role_user, user_exist
from uuid import UUID
from models.ObraModel import ObraModel
from typing import List

mainCapi = APIRouter(prefix="/cap", tags=['capitulo'], responses={404: {"description": "Not found"}})

@mainCapi.get('/{obra_id}/{numero}')
async def get_capi(obra_id: UUID = Path(...), numero: int = Path(...)):
    try:
        capi = CapituloModel.get_capitulo_by_obra(obra_id, numero)
        return (capi)
    except Exception as ex:
        return ({'message':str(ex)}),500
    
@mainCapi.post('/addcapi')
async def add_capitulo(numero: int = Body(...), fecha: str = Body(...), idioma: str = Body(...), obra: UUID = Body(0), price: float = Body(...), images: List[str] = Body(...)):
    try:
        obram = ObraModel()
        if not obram.exist_obra(obra) and obram.oneshot_bool(obra):
            raise HTTPException(status_code=404, detail="No se puede agregar el capitulo, perdon uwu")
        capim = CapituloModel()
        if capim.get_max_capitulo(obra) >= numero:
            raise HTTPException(status_code=404, detail="El capitulo ya existe")
        capi = Capitulo(numero, fecha, idioma,price, images)
        affec_row = StrategyCapituloArts.add_capitulo(capi, obra)
        if affec_row == 0:
            return ({'message': "Error on insert"})
        return ({'message':"Ok"})
    except Exception as ex:
        return ({'message':str(ex)}),500
@mainCapi.delete('/delete/{numero}/{id_obra}/{id_user}')
async def delete_capitulo(numero: int = Path(...), id_obra: UUID = Path(...), id_user: UUID = Path(...)):
    try:
        if not user_exist(id_user):
            raise HTTPException(status_code=404, detail="User not exist")
        if get_role_user(id_user) == "artist":
            affec_row = CapituloModel(StrategyCapituloArts).delete_capi(numero, id_obra, id_user)
        elif get_role_user(id_user) == "scan":
            affec_row = CapituloModel(StrategyCapituloScan).delete_capi(numero, id_obra, id_user)
        else:
            raise HTTPException(status_code=403, detail="No permitido")
        if affec_row == 0:
            return ({'message': "Error on delete"})
        return ({'message':"Ok"})
    except Exception as ex:
        return ({'message':str(ex)}),500
@mainCapi.put('/update/{id_obra}/{numero}')
async def update_capitulo(numero: int = Path(...), id_obra: UUID = Path(...), oldpages: List[str] = Body(...), newpages: List[str] = Body(...), orden: List[int] = Body(...), id_user: UUID = Body(...)):
    try:
       pass
    except Exception as ex:
        return ({'message':str(ex)}),500

"""
@mainCapi.delete('/deletescan/{numero}/{id_obra}/{id_scan}')
async def delete_capitulo(numero: int = Path(...), id_obra: UUID = Path(...), id_scan: UUID = Path(...)):
    try:
        affec_row = CapituloModel(StrategyCapituloArts).delete_capi(numero, id_obra, id_scan)
        if affec_row == 0:
            return ({'message': "Error on delete"})
        return ({'message':"Ok"})
    except Exception as ex:
        return ({'message':str(ex)}),500"""