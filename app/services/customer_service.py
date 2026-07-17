from app.db.models.customer import Customer
from app.repositories.customer_repository import CustomerRepository
from typing import Optional

class CustomerService:
    def __init__(self, repo: CustomerRepository):
        self.repo = repo

    #create customer
    def create_customer(self, name: str, phone: str, email: Optional[str] = None):
        existing = self.repo.get_by_phone(phone)
        if existing:
            raise ValueError("The phone number already exist")
        
        customer = Customer(
            name = name,
            phone = phone,
            email = email
        )
        return self.repo.create(customer)

    #get customer by id.
    def get_customer(self, customer_id: int):
        customer = self.repo.get_by_id(customer_id)
        if customer is None:
            raise ValueError("Customer not found")
        return customer
        