from sqlalchemy.orm import Session

from app.db.models.warehouse import Warehouse

class WarehouseRepository:
    def __init__(self, db: Session):
        self.db = db
    
    #create warehouse
    def create(self, warehouse: Warehouse):
        self.db.add(warehouse)
        self.db.commit()
        self.db.refresh(warehouse)
        return warehouse

    #get warehouse by name
    def get_by_name(self, name: str):
        return self.db.query(Warehouse).filter(Warehouse.name == name).first()
    
    #get by_id
    def get_by_id(self, warehouse_id: int):
        return self.db.query(Warehouse).filter(Warehouse.id == warehouse_id,Warehouse.is_active).first()
    

    ## get all warehouses 
    def get_all(self):
        return self.db.query(Warehouse).filter(Warehouse.is_active).all()
    

    ##update warehouse 
    def update(self, warehouse: Warehouse):
        self.db.commit()
        self.db.refresh(warehouse)
        return warehouse