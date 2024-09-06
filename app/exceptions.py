from fastapi import HTTPException, status


class BookingException(HTTPException):
    status_code = 500  # по умолчанию
    detail = ""
    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)


class UserAlreadyExistsException(HTTPException):
    status_code = status.HTTP_409_CONFLICT,
    detail = "Пользователь уже существует"


class IncorrectEmailOrPassword(HTTPException):
    status_code = status.HTTP_401_UNAUTHORIZED,
    detail = "Неверная пара логин-пароль"


class TokenExpiredException(HTTPException):
    status_code = status.HTTP_401_UNAUTHORIZED,
    detail = "Токен доступа истек"


class TokenAbsentException(HTTPException):
    status_code = status.HTTP_401_UNAUTHORIZED,
    detail = "Отсутствует токен доступа"


class IncorrectTokenFormatException(HTTPException):
    status_code = status.HTTP_401_UNAUTHORIZED,
    detail = "Токен не валиден"


class UserInfoAbsentInToken(HTTPException):
    status_code = status.HTTP_401_UNAUTHORIZED,
    detail = "Отсутствует информация о пользователе в токене"


class UserNotExistsException(HTTPException):
    status_code = status.HTTP_401_UNAUTHORIZED,
    detail = "Пользователь не существует"

