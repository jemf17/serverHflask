from fastapi import APIRouter, UploadFile, Path, Body
from models.CapituloModel import CapituloModel, StrategyCapituloArts, StrategyCapituloScan
from models.entities.Capitulo import Capitulo
from uuid import UUID

mainCapi = APIRouter(prefix="/cap", tags=['capitulo'], responses={404: {"description": "Not found"}})

@mainCapi.get('/{obra_id}/{numero}')
async def get_capi(obra_id: UUID = Path(...), numero: int = Path(...)):
    try:
        capi = CapituloModel.get_capitulo_by_obra(obra_id, numero)
        return (capi)
    except Exception as ex:
        return ({'message':str(ex)}),500
    
@mainCapi.post('/addcapi')
async def add_capitulo(numero: int = Body(...), fecha: str = Body(...), idioma: str = Body(...), obra: UUID = Body(...)):
    try:
        capi = Capitulo('', numero, fecha, idioma)
        affec_row = CapituloModel.add_capitulo(capi, obra)
        if affec_row == 0:
            return ({'message': "Error on insert"})
        return ({'message':"Ok"})
    except Exception as ex:
        return ({'message':str(ex)}),500
@mainCapi.delete('/delete/{numero}/{id_obra}/{id_user}')
async def delete_capitulo(numero: int = Path(...), id_obra: UUID = Path(...), id_user: UUID = Path(...)):
    try:
        affec_row = CapituloModel(StrategyCapituloArts).delete_capi(numero, id_obra, id_user)
        if affec_row == 0:
            return ({'message': "Error on delete"})
        return ({'message':"Ok"})
    except Exception as ex:
        return ({'message':str(ex)}),500

@mainCapi.delete('/deletescan/{numero}/{id_obra}/{id_scan}')
async def delete_capitulo(numero: int = Path(...), id_obra: UUID = Path(...), id_scan: UUID = Path(...)):
    try:
        affec_row = CapituloModel(StrategyCapituloArts).delete_capi(numero, id_obra, id_scan)
        if affec_row == 0:
            return ({'message': "Error on delete"})
        return ({'message':"Ok"})
    except Exception as ex:
        return ({'message':str(ex)}),500