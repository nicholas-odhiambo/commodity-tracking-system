from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.suppliers import SupplierCreate, SupplierUpdate
from app.services.supplier_service import SupplierService
from app.repositories.supplier_repository import SupplierRepository

router = APIRouter()

#post supplier
@router.post("/suppliers")
def create_supplier(payload: SupplierCreate, db: Session = Depends(get_db)):
    repo = SupplierRepository(db)
    service =SupplierService(repo)
    try:
        result = service.create_supplier(
            name = payload.name,
            phone = payload.phone,
            email = payload.email
        )
        return result
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

## get by id
@router.get("/suppliers/{supplier_id}")
def get_supplier(supplier_id: int, db: Session = Depends(get_db)):
    repo = SupplierRepository(db)
    service = SupplierService(repo)
    try:
        result = service.get_supplier(supplier_id)
        return result
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

#get all suppliers 
@router.get("/suppliers")
def get_suppliers(db: Session = Depends(get_db)):
    repo = SupplierRepository(db)
    service = SupplierService(repo)
    return service.get_suppliers()

#update suppliers 
@router.put("/suppliers/{supplier_id}")
def update_supplier(supplier_id: int, payload: SupplierUpdate, db: Session = Depends(get_db)):
    repo = SupplierRepository(db)
    service = SupplierService(repo)

    try:
        result = service.update_supplier(
            supplier_id = supplier_id,
            name = payload.name,
            phone = payload.phone,
            email = payload.email,
            is_active = payload.is_active
        )
        return result
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

#delete supplier
@router.delete("/supplier/{supplier_id}")
def delete_supplier(supplier_id: int, db: Session = Depends(get_db)):
    repo = SupplierRepository(db)
    service = SupplierService(repo)
    try:
        result = service.delete_supplier(supplier_id)
        return result
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))