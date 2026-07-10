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
    
    #get supplier by name
    def get_by_name(self, name: str):
        return self.db.query(Supplier).filter(Supplier.name == name).first() 

    #get supplier by id
    def get_by_id(self, supplier_id: int):
        return self.db.query(Supplier).filter(Supplier.id == supplier_id,Supplier.is_active).first()

    
    #get all suppliers 
    def get_all(self):
        return self.db.query(Supplier).filter(Supplier.is_active).all()

    ##update fields
    def update(self, supplier: Supplier):
        self.db.commit()
        self.db.refresh(supplier)
        return supplier