## for testing relationships 

##import database session 
from app.db.session import SessionLocal

# import the modules
from app.db.models.commodity import Commodity
from app.db.models.warehouse import Warehouse
from app.db.models.purchase import Purchase
from app.db.models.purchase_item import PurchaseItem
from app.db.models.supplier import Supplier

# create session

db = SessionLocal()

try:
    supplier = db.query(Supplier).filter_by(name="ABC Suppliers").first()
    if Supplier is None:
        supplier = Supplier(name="ABC Suppliers", phone="0709876587")
        db.add(supplier)
        db.commit()
        db.refresh(supplier)
    





##close the script
finally:
    db.close()