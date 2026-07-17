from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.customer import CustomerCreate, CustomerUpdate
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

#get customer by id
@router.get("/customers/{customer_id}")
def get_customer(customer_id: int, db: Session = Depends(get_db)):
    repo = CustomerRepository(db)
    service = CustomerService(repo)
    try:
        result = service.get_customer(customer_id)
        return result
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

#get all customers 
@router.get("/customers")
def get_customers(db: Session = Depends(get_db)):
    repo = CustomerRepository(db)
    service = CustomerService(repo)
    try:
        result = service.get_customers()
        return result
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

#update customer
@router.put("/customers/{customer_id}")
def update_customer(customer_id: int, payload: CustomerUpdate,
                    db: Session = Depends(get_db)):
    repo = CustomerRepository(db)
    service = CustomerService(repo)
    try:
        result = service.update_customer(
            customer_id = customer_id,
            name = payload.name,
            phone = payload.phone,
            email = payload.email,
            is_active = payload.is_active
        )
        return result
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))