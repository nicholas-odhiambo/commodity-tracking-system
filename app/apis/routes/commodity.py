from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.commodity import CommodityCreate
from app.services.commodity_service import CommodityService
from app.repositories.commodity_repository import CommodityRepository

router = APIRouter()

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
    
@router.get("/commodities/{commodity_id}")
def get_commodities():
    pass
