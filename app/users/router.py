from fastapi import APIRouter, Response, Depends

from app.users.auth import get_password_hash, authenticate_user, create_access_token
from app.users.dao import UsersDAO
from app.users.dependencies import get_current_user
from app.users.models import Users
from app.users.schemas import SUserAuth, SUser
from app.exceptions import IncorrectEmailOrPassword, UserAlreadyExistsException

router = APIRouter(
    prefix="/auth",
    tags=["Auth & Пользователи"],
)

@router.post('/register')
async def register_user(user_data: SUserAuth):
    existing_user = await UsersDAO.find_one_or_none(email=user_data.email)
    if existing_user:
        raise UserAlreadyExistsException
    pass_hash = get_password_hash(user_data.password)
    await UsersDAO.add(email=user_data.email, hashed_password=pass_hash)


@router.post('/login')
async def login_user(response: Response, user_data: SUserAuth):
    user = await authenticate_user(user_data.email, user_data.password)
    if not user:
        raise IncorrectEmailOrPassword
    access_token = create_access_token(data={"sub": str(user.id)})
    response.set_cookie('bookings_access_token', access_token, httponly=True)
    return {'access_token': access_token}


@router.post('/logout')
def logout_user(response: Response):
    response.delete_cookie('bookings_access_token')


@router.get('/me')
def get_user_info(user: Users = Depends(get_current_user)) -> SUser:
    return user


