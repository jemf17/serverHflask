from fastapi import HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from jwt import PyJWTError, decode
import os
from uuid import UUID
def decode_token_scan(token: str = Depends(OAuth2PasswordBearer(tokenUrl="token"))):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        SECRET_KEY = os.getenv('KEY_SUPABASE')
        payload = decode(token, SECRET_KEY, algorithms=["HS256"])
        rol: str = payload.get("rol")
        id_user: UUID = payload.get("id_user")
        if id_user is None and rol != 'scan':
            raise credentials_exception
        return  id_user
    except PyJWTError:
        raise credentials_exception
def decode_token_art(token: str = Depends(OAuth2PasswordBearer(tokenUrl="token"))):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        SECRET_KEY = os.getenv('KEY_SUPABASE')
        payload = decode(token, SECRET_KEY, algorithms=["HS256"])
        rol: str = payload.get("rol")
        id_user: UUID = payload.get("id_user")
        if id_user is None and rol != 'artist':
            raise credentials_exception
        return id_user
    except PyJWTError:
        raise credentials_exception
def decode_token_admin(token: str = Depends(OAuth2PasswordBearer(tokenUrl="token"))):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        SECRET_KEY = os.getenv('KEY_SUPABASE')
        payload = decode(token, SECRET_KEY, algorithms=["HS256"])
        rol: str = payload.get("rol")
        id_user: UUID = payload.get("id_user")
        if id_user is None and rol != 'admin':
            raise credentials_exception
        return  id_user
    except PyJWTError:
        raise credentials_exception
def decode_token(token: str = Depends(OAuth2PasswordBearer(tokenUrl="token"))):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        SECRET_KEY = os.getenv('KEY_SUPABASE')
        payload = decode(token, SECRET_KEY, algorithms=["HS256"])
        id_user: UUID = payload.get("id_user")
        if id_user is None and rol != 'scan':
            raise credentials_exception
        return  id_user
    except PyJWTError:
        raise credentials_exception