from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.commodity import CommodityCreate, CommodityUpdate
from app.services.commodity_service import CommodityService
from app.repositories.commodity_repository import CommodityRepository

router = APIRouter()

#post commodity
@router.post("/commodities")
def create_commodity(payload:  CommodityCreate, db: Session = Depends(get_db)):
    repo = CommodityRepository(db)
    service = CommodityService(repo)

    try:
        result = service.create_commodity(
            name = payload.name,
            unit_of_measure=payload.unit_of_measure,
            description=payload.description,
        )
        return result
    
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

#get by id
@router.get("/commodities/{commodity_id}")
def get_commodity(commodity_id: int, db: Session = Depends(get_db)):
    repo = CommodityRepository(db)
    service = CommodityService(repo)
    try:
        result = service.get_commodity(commodity_id)
        return result
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

#get all commodities
@router.get("/commodities")
def get_commodities(db: Session = Depends(get_db)):
    repo = CommodityRepository(db)
    service = CommodityService(repo)
    return service.get_commodities()


##update commodity 
@router.put("/commodities/{commodity_id}")
def update_commodity(commodity_id: int, payload: CommodityUpdate, db: Session = Depends(get_db)):
    repo = CommodityRepository(db)
    service = CommodityService(repo)

    try:
        result = service.update_commodity(
            commodity_id=commodity_id,
            name = payload.name,
            unit_of_measure = payload.unit_of_measure,
            description = payload.description,
            is_active = payload.is_active
        )
        return result
    
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

##delete commodity 
@router.delete("/commodities/{commodity_id}")
def delete_commodity(commodity_id: int, db: Session = Depends(get_db)):
    repo = CommodityRepository(db)
    service = CommodityService(repo)
    try:
        result = service.delete_commodity(commodity_id)
        return result
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))