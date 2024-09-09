from fastapi import HTTPException, status


class BookingException(HTTPException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    detail = "Неизвестная ошибка на стороне сервера"
    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)


class UserAlreadyExistsException(BookingException):
    status_code = status.HTTP_409_CONFLICT
    detail = "Пользователь уже существует"


class IncorrectEmailOrPassword(BookingException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Неверная пара логин-пароль"


class TokenExpiredException(BookingException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Токен доступа истек"


class TokenAbsentException(BookingException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Отсутствует токен доступа"


class IncorrectTokenFormatException(BookingException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Токен не валиден"


class UserInfoAbsentInToken(BookingException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Отсутствует информация о пользователе в токене"


class UserNotExistsException(BookingException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Пользователь не существует"


class RoomCannotBeBooked(BookingException):
    status_code = status.HTTP_409_CONFLICT
    detail = "Закончились номера данного типа"



