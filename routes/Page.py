from fastapi import APIRouter, UploadFile, Path, Body
from models.PageModel import PageModel
from models.entities.Page import Page

mainPage = APIRouter(prefix="/page", tags=['pages'], responses={404: {"description": "Not found"}})

@mainPage.post('/add')
def add_page():
    try:
        pass
    except Exception as ex:
        return {'message':str(ex),'status':500}

@mainPage.put('/putpage') #o PATCH, no se cual es mejor xd
def upload_page():
    try:
        pass
    except Exception as ex:
        return {'message':str(ex),'status':500}
    
@mainPage.delete('/delete')
def delete_page():
    try:
        pass
    except Exception as ex:
        return {'message':str(ex),'status':500}