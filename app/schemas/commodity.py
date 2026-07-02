from pydantic import BaseModel, field_validator
from typing import Optional

class CommodityCreate(BaseModel):
    commodity_name: str 
    unit_of_measure: str
    description: Optional[str] = None 

    @field_validator("commodity_name")
    @classmethod
    def validate_commodity_name(cls, value: str):
        value = value.strip()
        if not value:
            raise ValueError("Commodity Name cannot be empty or white space")
        return value