from pydantic import BaseModel, field_validator
from typing import Optional

class SupplierCreate(BaseModel):
    name: str
    phone: str 
    email: Optional[str] = None

    @field_validator("name", "phone")
    @classmethod

    def validate_supplier_name(cls, value: str):
        value = value.strip()
        if not value:
            raise ValueError("Supplier Name or phone_no cannot be empty or have whitespace")
        return value
    
class SupplierUpdate(BaseModel):
    name: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None
    is_active: Optional[bool] = None

    @field_validator("name", "phone", "email")
    @classmethod
    def validate_fields(cls, value: Optional[str]):
        #fields not supplied 
        if value is None:
            return value
        
        value = value.strip()
        
        if not value:
            raise ValueError("The fileds cannot be empty")
        return value