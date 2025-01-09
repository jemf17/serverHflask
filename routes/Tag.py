from fastapi import APIRouter, UploadFile, Path, Body, HTTPException
from models.TagModel import TagModel
#from typing import List

mainTag = APIRouter(prefix="/tag", tags=['tag'], responses={404: {"description": "Not found"}})

@mainTag.get('search/{tag}/{next}')
async def get_obras_by_tag(tag: str = Path(...), next: int =Path(...)):
    try:
        if next < 0:
            raise HTTPException(status_code=400, detail="next must be greater than 0")
        return {'obras': TagModel.get_obras_by_tag_order_time(tag, next)}
    except Exception as ex:
        return {'message':str(ex),'status':500}
@mainTag.get('searchpopu/{tag}/{next}')
async def get_obras_by_tag(tag: str = Path(...), next: int =Path(...)):
    try:
        if next < 0:
            raise HTTPException(status_code=400, detail="next must be greater than 0")
        return {'obras': TagModel.get_obras_by_tag_order_popular(tag, next)}
    except Exception as ex:
        return {'message':str(ex),'status':500}

@mainTag.get('/all/{next}')
async def get_all_tags(next: int =Path(...)):
    try:
        if next < 0:
            raise HTTPException(status_code=400, detail="next must be greater than 0")
        return {'tags': TagModel.get_all_tags(next)}
    except Exception as ex:
        return {'message':str(ex),'status':500}