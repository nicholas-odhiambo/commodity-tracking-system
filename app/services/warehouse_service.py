from app.db.models.warehouse import Warehouse
from app.repositories.warehouse_repository import WarehouseRepository

class WarehouseService:
    def __init__(self, repo: WarehouseRepository):
        self.repo = repo
    
    #create warehouse and save to db
    def create_warehouse(self, name: str, location: str, capacity: int):
        existing = self.repo.get_by_name(name)
        if existing:
            return ValueError("Warehouse with the name already exist")
        
        warehouse = Warehouse(
            name = name,
            location = location,
            capacity = capacity
        )
        self.repo.create(warehouse)

    ##get by id
    def get_warehouse(self, warehouse_id: int):
        warehouse = self.repo.get_by_id(warehouse_id)
        if warehouse is None:
            raise ValueError("Warehouse does not exist")
        return warehouse