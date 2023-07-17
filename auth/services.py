# 【核酸采集平台】 auth/services.py
from fastapi import Depends, HTTPException, status
from jose import JWTError
from sqlalchemy.orm import Session

from app.database import get_db
from app.settings import AUTH_SCHEMA
from utils.password import get_password_hash, verify_password
from utils.token import extract_token
from .models import UserInDB
from .schemas import UserCreate


# 获取单个用户
def get_user(db: Session, username: str):
    return db.query(UserInDB).filter(UserInDB.username == username).first()


# 创建一个用户
def create_user(db: Session, user: UserCreate):
    # 计算密码的哈希值
    hashed_password = get_password_hash(user.password)
    db_user = UserInDB(username=user.username, hashed_password=hashed_password, )
    # 第二步，将实例添加到会话
    db.add(db_user)
    # 第三步，提交会话
    db.commit()
    # 第四步，刷新实例，用于获取数据或者生成数据库中的ID
    db.refresh(db_user)
    return db_user


# 验证用户和密码
def authenticate_user(db: Session, username: str, password: str):
    user = get_user(db, username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user


# 获取当前用户信息的依赖函数
async def get_current_user(token: str = Depends(AUTH_SCHEMA), db: Session = Depends(get_db)):
    invalid_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="无效的用户任据",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        username: str = extract_token(token)
        if username is None:
            raise invalid_exception
    except JWTError:
        raise invalid_exception
    user = get_user(db, username=username)
    if user is None:
        raise invalid_exception
    return user
