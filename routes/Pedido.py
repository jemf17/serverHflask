from fastapi import APIRouter, UploadFile, Path, Body, HTTPException
from uuid import UUID

mainPedido = APIRouter(prefix="/pedi", tags=['pedido'], responses={404: {"description": "Not found"}})

@mainPedido.get("/{next}")
async def get_pedidos(next: int = Path(..., ge=0, description="numero negativo error")):
    return {"next": next}

@mainPedido.get('/{id}')
async def get_pedido(id: UUID = Path(...))