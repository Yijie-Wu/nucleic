# 【核酸采集平台】 person/services.py
from typing import Optional

from sqlalchemy import func
from sqlalchemy.orm import Session

from .models import PersonInDB
from .schemas import Person

# 定义依赖函数
async def get_params(xm: Optional[str] = None,
                     lxdh: Optional[str] = None,
                     jzdz: Optional[str] = None,
                     page: Optional[int] = 1,
                     size: Optional[int] = 10):
    return {'xm': xm, 'lxdh': lxdh, 'jzdz': jzdz, 'page': page, 'size': size}

# 保存预约信息
def save_person(db: Session, data: Person):
    dbdata = PersonInDB(**data.dict())
    db.add(dbdata)
    db.commit()
    db.refresh(dbdata)
    return dbdata

def get_person(db: Session, zjhm):
    data = db.query(PersonInDB).filter(PersonInDB.zjhm == zjhm).first()
    return data

# 分页取出预约信息列表,默认第1页，10条记录
def list_person(db: Session, params):
    # 用于查询当前条件下的总数量
    qcnt = db.query(func.count('*'))
    q = db.query(PersonInDB)
    if params['xm']:
        q = q.filter(PersonInDB.xm == params['xm'])
        qcnt = qcnt.filter(PersonInDB.xm == params['xm'])
    if params['lxdh']:
        q = q.filter(PersonInDB.lxdh == params['lxdh'])
        qcnt = qcnt.filter(PersonInDB.lxdh == params['lxdh'])
    if params['jzdz']:
        q = q.filter(PersonInDB.jzdz.like('%' + params['jzdz'] + '%'))
        qcnt = qcnt.filter(PersonInDB.jzdz.like('%' + params['jzdz'] + '%'))
    cnt = qcnt.scalar()
    data = q.limit(params['size']).offset((params['page'] - 1) * params['size'])
    return {"count": cnt, "list": data.all()}
