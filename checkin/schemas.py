# 【核酸采集平台】checkin/schemas.py
from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime
from person.schemas import Person
# 登记数据模型
class CheckIn(BaseModel):
    id: Optional[int] = None
    bqbh: str
    bqxh: int
    cjdd: Optional[str]
    cjry: Optional[int] = None
    person_id: Optional[int]
    class Config:
        orm_mode = True

# 登记响应模型
class CheckInResponse(CheckIn, Person):
    pass
