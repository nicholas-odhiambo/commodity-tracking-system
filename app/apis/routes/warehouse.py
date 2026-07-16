from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.warehouse import WarehouseCreate, WarehouseUpdate
from app.services.warehouse_service import WarehouseService
from app.repositories.warehouse_repository import WarehouseRepository

router = APIRouter()

#post warehouse
@router.post("/warehouses")
def create_warehouse(payload: WarehouseCreate, db: Session = Depends(get_db)):
    repo = WarehouseRepository(db)
    service = WarehouseService(repo)
    try:
        result = service.create_warehouse(
            name = payload.name,
            location = payload.location,
            capacity = payload.capacity
        )
        return result
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

#get by id
@router.get("/warehouses/{warehouse_id}")
def get_warehouse(warehouse_id: int, db: Session = Depends(get_db)):
    repo = WarehouseRepository(db)
    service = WarehouseService(repo)
    try: 
        result = service.get_warehouse(warehouse_id)
        return result
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

#get all 
@router.get("/warehouses")
def get_warehouses(db: Session = Depends(get_db)):
    repo = WarehouseRepository(db)
    service = WarehouseService(repo)
    return service.get_warehouses()

#update warehouse 
@router.put("/warehouses/{warehouse_id}")
def update_warehouse(warehouse_id: int, payload: WarehouseUpdate, db: Session = Depends(get_db)):

    repo = WarehouseRepository(db)
    service = WarehouseService(repo)
    try:
        result = service.update_warehouse(
            warehouse_id = warehouse_id,
            name = payload.name,
            location = payload.location,
            capacity = payload.capacity,
            is_active = payload.is_active
        )
        return result 
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    

## delete warehouse
@router.delete("/warehouse/{warehouse_id}")
def delete_warehouse(warehouse_id: int, db: Session = Depends(get_db)):
    repo = WarehouseRepository(db)
    service = WarehouseService(repo)
    try:
        result = service.delete_warehouse(warehouse_id)
        return result
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))