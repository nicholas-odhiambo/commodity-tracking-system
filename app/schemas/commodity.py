from pydantic import BaseModel, field_validator
from typing import Optional

class CommodityCreate(BaseModel):
    name: str 
    unit_of_measure: str
    description: Optional[str] = None 

    @field_validator("name")
    @classmethod
    def validate_commodity_name(cls, value: str):
        value = value.strip()
        if not value:
            raise ValueError("Commodity Name cannot be empty or white space")
        return value

#the update endpoint schema 
class CommodityUpdate(BaseModel):
    name: str 
    unit_of_measure: str
    description: Optional[str] = None
    is_active: bool 

    @field_validator("name", "unit_of_measure")
    @classmethod
    def validate_fields(cls, value: str):
        value = value.strip()

        if not value:
            raise ValueError("The field cannot be empty")
        return value