from pydantic import BaseModel, field_validator
from typing import Optional


class WarehouseCreate(BaseModel):
    name: str 
    location: str 
    capacity: int 
    
    @field_validator("name", "location")
    @classmethod
    def validate_warehouse_name(cls, value: str):
        value = value.strip()
        if not value:
            raise ValueError("The field cannot be empty or whitespace")
        return value
    
    @field_validator("capacity")
    @classmethod
    def validate_capacity(cls, value: int):
        if value <= 0:
            raise ValueError("Capacity should not be less or equal to zero")
        return value

class WarehouseUpdate(BaseModel):
    name : Optional[str] = None
    location: Optional[str] = None
    capacity: Optional[int] = None
    is_active : Optional[bool] = None

    @field_validator("name", "location")
    @classmethod
    def validate_fields(cls, value: Optional[str]):
        if value is None:
            return None
        value = value.strip()

        if not value:
            raise ValueError("Warehouse name and location cannot be empty")
        return value
        
    @field_validator("capacity")
    @classmethod
    def validate_capacity(cls, value: Optional[int]):
        if value is None:
            return None

        if value <= 0:
            raise ValueError("Capacity must be greater than zero")
        return value
    



