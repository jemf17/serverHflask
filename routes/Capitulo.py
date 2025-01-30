from fastapi import APIRouter, UploadFile, Path, Body, HTTPException, Depends
from models.CapituloModel import CapituloModel, StrategyCapituloArts, StrategyCapituloScan
from models.entities.Capitulo import Capitulo
from helper.sb_help import get_role_user, user_exist
from uuid import UUID
from models.ObraModel import ObraModel
from typing import List
from auth.auth import decode_token_scan, decode_token_art
mainCapi = APIRouter(prefix="/cap", tags=['capitulo'], responses={404: {"description": "Not found"}})

@mainCapi.get('/{obra_id}/{numero}')
async def get_capi(obra_id: UUID = Path(...), numero: int = Path(...)):
    try:
        capi = CapituloModel.get_capitulo_by_obra(obra_id, numero)
        return (capi)
    except Exception as ex:
        return ({'message':str(ex)}),500
@mainCapi.get('/{id_scan}/{obra_id}/{numero}')
async def get_capi(id_scan: UUID = Path(...),obra_id: UUID = Path(...), numero: int = Path(...)):
    try:
        capi = CapituloModel.get_capitulo_by_obra_scan(obra_id, numero, id_scan)
        return (capi)
    except Exception as ex:
        return ({'message':str(ex)}),500
@mainCapi.post('/addscancapi')
async def add_scan_capi(id_user: UUID = Depends(decode_token_scan), numero: int = Body(...), fecha: str = Body(...), idioma: str = Body(...), obra: UUID = Body(...), price: float = Body(...), images: List[str] = Body(...)):
    try:
        obram = ObraModel()
        if not obram.exist_obra_by_id(obra):
            raise HTTPException(status_code=404, detail="obra no existente")
        capim = CapituloModel()
        if capim.get_max_capitulo(obra) < numero:
            raise HTTPException(status_code=404, detail="El capitulo original no existe")
        if capim.idioma_original(obra, numero) == idioma:
            raise HTTPException(status_code=404, detail="ese es el idioma original .-.")
        capi = Capitulo(numero, fecha, idioma,price, images)
        affec_row = StrategyCapituloScan.add_capitulo(capi, obra, id_user, id_user)
        if affec_row == 0:
            return ({'message': "Error on insert"})
        return ({'message':"Ok"})
    except Exception as ex:
        return ({'message':str(ex)}),500    
@mainCapi.post('/addcapi')
async def add_capitulo(id_user: UUID = Depends(decode_token_art),numero: int = Body(...), fecha: str = Body(...), idioma: str = Body(...), obra: UUID = Body(0), price: float = Body(...), images: List[str] = Body(...)):
    try:
        obram = ObraModel()
        if not obram.artis_permition(id_user, obra):
            raise HTTPException(status_code=404, detail="No tienes permisos para agregar el capitulo")
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
@mainCapi.delete('/delete/{numero}/{id_obra}')
async def delete_capitulo(numero: int = Path(...), id_obra: UUID = Path(...), id_user: UUID = Depends(decode_token_art)):
    try:
        affec_row = StrategyCapituloArts.delete_capi(numero, id_obra, id_user)
        if affec_row == 0:
            return ({'message': "Error on delete"})
        return ({'message':"Ok"})
    except Exception as ex:
        return ({'message':str(ex)}),500
@mainCapi.delete('/deletescan/{numero}/{id_obra}')
async def delete_capi_scan(numero: int = Path(...), id_obra: UUID = Path(...), id_user: UUID = Depends(decode_token_scan)):
    try:
        affec_row = StrategyCapituloScan.delete_capi(numero, id_obra, id_user)
        if affec_row == 0:
            return ({'message': "Error on delete"})
        return ({'message':"Ok"})
    except Exception as ex:
        return ({'message':str(ex)}),500
@mainCapi.put('/update/{id_obra}/{numero}')
async def update_capitulo(numero: int = Path(...), id_obra: UUID = Path(...), oldpages: List[str] = Body(...), newpages: List[str] = Body(...), orden: List[int] = Body(...), id_user: UUID = Depends(decode_token_art)):
    try:
       pass
    except Exception as ex:
        return ({'message':str(ex)}),500
@mainCapi.put('/updatescan/{id_obra}/{numero}')
async def update_capitulo_scan(numero: int = Path(...), id_obra: UUID = Path(...), oldpages: List[str] = Body(...), newpages: List[str] = Body(...), orden: List[int] = Body(...), id_user: UUID = Depends(decode_token_scan)):
    try:
       pass
    except Exception as ex:
        return ({'message':str(ex)}),500
