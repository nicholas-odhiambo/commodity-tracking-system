from app.db.models.customer import Customer
from app.repositories.customer_repository import CustomerRepository
from typing import Optional

class CustomerService:
    def __init__(self, repo: CustomerRepository):
        self.repo = repo

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