from fastapi import APIRouter, UploadFile, Path, Body, HTTPException
from uuid import UUID
mainSoli = APIRouter(prefix="/soli", tags=['solicitud'], responses={404: {"description": "Not found"}})

@mainSoli.get("/{id_user}")
async def get_bool_solicitudes(id_user: UUID = Path(...)):
    return {"solicitudes": id_user}
@mainSoli.get('/{id_user}/{id_obra}')
async def get_solicitudes(id_user: UUID = Path(...), id_obra: UUID = Path(...)):
    return {"solicitudes": id_user, "obra": id_obra}