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
    
    ##get all 
    def get_warehouses(self):
        return self.repo.get_all()

    ##update warehouse 
    def update_warehouse(self, warehouse_id: int,  name: str | None, location : str | None, 
                         capacity: int | None, is_active: bool | None):
        warehouse = self.repo.get_by_id(warehouse_id)

        if warehouse is None:
            raise ValueError("Warehouse not found")
        
        if name is not None:
            existing = self.repo.get_by_name(name)

            if existing is not None and existing.id != warehouse.id:
                raise ValueError("A warehouse with the name already exists")
        
            warehouse.name = name

        if location is not None:
            warehouse.location = location 
        
        if capacity is not None:
            warehouse.capacity = capacity
        
        if is_active is not None:
            warehouse.is_active = is_active

        return self.repo.update(warehouse)
    
    ##delete warehouse
    def delete_warehouse(self, warehouse_id: int):
        warehouse = self.repo.get_by_id(warehouse_id)

        if warehouse is None: 
            raise ValueError("The warehouse does not exists")
        
        if warehouse.is_active is False:
            raise ValueError("The warehouse has aleady been deleted")
        
        warehouse.is_active = False
        return self.repo.update(warehouse)