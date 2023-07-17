# 【核酸采集平台】 person/router.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from auth.services import AUTH_SCHEMA
from utils.response import PageResponse
from .schemas import Person
from .services import save_person, list_person, get_person, get_params

route = APIRouter(
    tags=['预约']
)

@route.post('/submit', response_model=Person)
async def submit(data: Person, db: Session = Depends(get_db)):
    return save_person(db, data)

@route.get('/get', response_model=Person, dependencies=[Depends(AUTH_SCHEMA)])
async def get(zjhm: str, db: Session = Depends(get_db)):
    return get_person(db, zjhm)

@route.get('/list', response_model=PageResponse, dependencies=[Depends(AUTH_SCHEMA)])
async def list(params: dict = Depends(get_params), db: Session = Depends(get_db), ):
    return list_person(db, params)
