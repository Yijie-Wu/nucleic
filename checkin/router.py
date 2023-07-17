# 【核酸采集平台】checkin/router.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from utils.response import PageResponse
from .schemas import CheckIn
from .services import QueryParams, save_checkin, list_checkin

route = APIRouter(
    tags=['登记']
)

@route.post('/submit', response_model=CheckIn)
async def submit(data: CheckIn, db: Session = Depends(get_db)):
    return save_checkin(db, data)

@route.get('/list', response_model=PageResponse, )
async def list(params: QueryParams = Depends(), db: Session = Depends(get_db), ):
    return list_checkin(db, params)
