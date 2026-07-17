from sqlalchemy.orm import Session

from app.db.models.customer import Customer

class CustomerRepository:
    def __init__(self, db: Session ):
        self.db = db

    #create customer
    def create(self, customer: Customer):
        self.db.add(customer)
        self.db.commit()
        self.db.refresh(customer)
        return customer

    #get customer name 
    def get_by_phone(self, phone:str ):
        return self.db.query(Customer).filter(Customer.phone == phone).first()