from pydantic import BaseModel, field_validator
from typing import Optional

class CustomerCreate(BaseModel):

    name: str 
    phone: str
    email: Optional[str] = None

    @field_validator("phone", "name")
    @classmethod
    def validate_fields(cls, value: str):
        value = value.strip()
        if not value: 
            raise ValueError("Phone or name cannot be empty or have white space.")
        return value

class CustomerUpdate(BaseModel):
    name: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None
    is_active: Optional[bool] = None

    @field_validator("name", "phone", "email")
    @classmethod
    def validate_fields(cls, value: Optional[str]):
        if value is None:
            return value
        
        value = value.strip()

        if not value:
            raise ValueError("Field cannot be empty")
        return value