from app.db.models.supplier import Supplier
from app.repositories.supplier_repository import SupplierRepository
from typing import Optional

class SupplierService:
    def __init__(self, repo: SupplierRepository):
        self.repo = repo 
 
    ##create and save to db
    def create_supplier(self, name: str, phone: str, email: Optional[str] = None):
        existing = self.repo.get_by_name(name)
        if existing:
            raise ValueError("Supplier already exists")
        
        ##create supplier
        supplier = Supplier(
            name = name,
            phone = phone,
            email = email
        )
        self.repo.create(supplier) 

    ##get supplier by id
    def get_supplier(self, supplier_id: int):
        supplier = self.repo.get_by_id(supplier_id)
        if supplier is None:
            raise ValueError("Supplier not found")
        return supplier
        
