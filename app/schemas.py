from enum import Enum
from typing import Union
from fastapi_camelcase import CamelModel
from pydantic import BaseModel


class Token(CamelModel):
    access_token: str
    token_type: str


class TokenData(CamelModel):
    username: Union[str, None] = None


class Role(str, Enum):
    ADMIN = "ADMIN"
    USER = "USER"


class User(CamelModel):
    id: int
    username: str
    is_active: Union[bool, None] = None
    role: Role

    class Config:
        from_attributes = True


class BasketBase(BaseModel):
    user_id: int
    table_name: str
    product_id: int


class BasketCreate(BasketBase):
    pass


class Basket(BasketBase):
    id: int

    class Config:
        from_attributes = True
