from pydantic import BaseModel, field_validator

class WarehouseCreate(BaseModel):
    name: str 
    location: str 
    capacity: int 
    
    @field_validator("name", "location")
    @classmethod
    def validate_warehouse_name(cls, value: str):
        value = value.strip()
        if not value:
            raise ValueError("Warehouse_name or warehouse_location cannot be empty or whitespace")
        return value
    
    @field_validator("capacity")
    @classmethod
    def validate_warehouse_capacity(cls, value: int):
        if value <= 0:
            raise ValueError("Capacity should not be less or equal to zero")
        return value


