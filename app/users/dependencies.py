from datetime import datetime

from fastapi import Request, Depends
from jose import jwt, JWTError

from app.config import settings
from app.users.dao import UsersDAO
from app.exceptions import *
from app.users.models import Users


def get_token(request: Request):
    token = request.cookies.get('bookings_access_token')
    if not token:
        raise TokenAbsentException
    return token


async def get_current_user(token: str = Depends(get_token)):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, settings.ALGORITHM)
    except JWTError:
        raise IncorrectTokenFormatException
    expire: int | None = payload.get('exp')
    if (not expire) or (datetime.utcnow() >= datetime.utcfromtimestamp(expire)):
        raise TokenExpiredException
    user_id: str | None = payload.get('sub')
    if not user_id:
        raise UserInfoAbsentInToken
    user = await UsersDAO.find_by_id(int(user_id))
    if not user:
        raise UserNotExistsException

    return user

