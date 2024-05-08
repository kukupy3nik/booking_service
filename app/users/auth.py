# Passlib при определенных версиях bcrypt бросает назойливую ошибку, т.к. не может проверить версию.
# Поэтому данная реализация закомментирована и ниже идет реализация с использованием библиотеки bcrypt напрямую
# from passlib.context import CryptContext
#
# pwd_context = CryptContext( schemes=["bcrypt"], deprecated="auto")
#
#
# def get_password_hash(password: str) -> str:
#     return pwd_context.hash(password)
#
#
# def verify_password(plain_password: str, hashed_password: str) -> bool:
#     return pwd_context.verify(plain_password, hashed_password)

import bcrypt


def get_password_hash(password: str) -> str:
    pwd_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password=pwd_bytes, salt=salt)
    return hashed_password.decode('utf-8')


# Check if the provided password matches the stored password (hashed)
def verify_password(plain_password: str, hashed_password: str) -> bool:
    password_byte_enc = plain_password.encode('utf-8')
    hashed_password_byte_enc = hashed_password.encode('utf-8')
    return bcrypt.checkpw(password=password_byte_enc, hashed_password=hashed_password_byte_enc)
