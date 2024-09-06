from pydantic import BaseModel, EmailStr


class SUserAuth(BaseModel):
    email: EmailStr
    password: str

class SUser(BaseModel):
    id: int
    email: EmailStr
    hashed_password: str