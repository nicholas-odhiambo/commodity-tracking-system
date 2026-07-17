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
     
    #get all customers 
    def get_customers(self):
        return self.repo.get_all()

    # update all customers
    def update_customer(self, customer_id: int, name: str | None, phone: str | None,
                        email: str | None, is_active: bool | None):
        customer = self.repo.get_by_id(customer_id)
        
        if customer is None:
            raise ValueError("Customer not found")
        
        if phone is not None:
            existing = self.repo.get_by_phone(phone)

            if existing is not None and existing.id != customer.id:
                raise ValueError("A customer with that phone number already exists")

            customer.phone = phone 
        
        if name is not None:
            customer.name = name 
        
        if email is not None:
            customer.email = email
        
        if is_active is not None:
            customer.is_active = is_active
        
        return self.repo.update(customer)

    # detelete customer
    def delete_customer(self, customer_id: int):
        customer = self.repo.get_by_id(customer_id)

        if customer is None:
            raise ValueError("Customer does not exist")
        
        if customer.is_active is False:
            raise ValueError("The customer has already been deleted")
        
        customer.is_active = False
        return self.repo.update(customer)