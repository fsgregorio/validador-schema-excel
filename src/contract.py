from pydantic import BaseModel, EmailStr, PositiveFloat, PositiveInt, field_validator
from datetime import datetime
from enum import Enum

class CategoryEnum(str, Enum):
    category1 = "category1"
    category2 = "category2"
    category3 = "category3"
class Sales(BaseModel):
    email: EmailStr
    date: datetime
    valor: PositiveFloat
    product: str
    quantity: PositiveInt
    category: CategoryEnum
    
@field_validator("category")
def category_validate(cls, value):
    if value not in CategoryEnum:
        raise ValueError(f"Category {value} not exist")
    return value