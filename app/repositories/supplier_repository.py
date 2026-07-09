from sqlalchemy.orm import Session

from app.db.models.supplier import Supplier

class SupplierRepository:
    def __init__(self, db: Session):
        self.db = db

    #create supplier 
    def create(self, supplier: Supplier):
        self.db.add(supplier)
        self.db.commit()
        self.db.refresh(supplier)
        return supplier
