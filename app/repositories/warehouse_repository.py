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