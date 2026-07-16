from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.warehouse import WarehouseCreate
from app.services.warehouse_service import WarehouseService
from app.repositories.warehouse_repository import WarehouseRepository

router = APIRouter()

#post warehouse
@router.post("/warehouse")
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
@router.get("/warehouse/{warehouse-_id}")
def get_by_id():
    pass