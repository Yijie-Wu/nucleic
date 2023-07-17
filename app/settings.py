# 【核酸采集平台】 app/settings.py
from fastapi.security import OAuth2PasswordBearer

# 定义配置项
# 密钥,使用 命令 # openssl rand -hex 32 生成
JWT_SECRET_KEY = '121a7ca2894627374a4a3326bc9f7f82a10d11e9742670840e9d327b13928d87'
# 加密算法
JWT_ALGORITHM = 'HS256'
# JWT中TOKEN有效期
ACCESS_TOKEN_EXPIRE_MINUTES = 1440
# 安全依赖项
AUTH_SCHEMA = OAuth2PasswordBearer(tokenUrl="auth/login")

# 数据库配置
DB_HOST = 'localhost'
DB_USERNAME = 'root'
DB_PASSWORD = 'www.isoftstone.CoM'
DB_DATABASE = 'nucleic'
