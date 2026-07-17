from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.customer import CustomerCreate
from app.repositories.customer_repository import CustomerRepository
from app.services.customer_service import CustomerService

router = APIRouter()

#post - create customers 
@router.post("/customers")
def create_customer(payload: CustomerCreate, db: Session = Depends(get_db)):
    repo = CustomerRepository(db)
    service = CustomerService(repo)
    try:
        result = service.create_customer(
            name = payload.name,
            phone = payload.phone,
            email = payload.email
        )
        return result
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))