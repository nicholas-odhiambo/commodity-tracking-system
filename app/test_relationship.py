## for testing relationships 

from decimal import Decimal
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

    warehouse = db.query(Warehouse).filter_by(name="The Millers").first()
    if Warehouse is None:
        warehouse = Warehouse(name="The Millers")
        db.add(Warehouse)
        db.commit()
        db.refresh(warehouse)


    ## A purchase
    purchase = Purchase(
        supplier_id=supplier.id,
        warehouse_id=warehouse.id
    )
    db.add(purchase)
    db.commit()
    db.refresh(purchase)

    ### purchaseItem 1
    PurchaseItem(
        purchase_id=purchase.id,
        commodity_id=maize.id,
        quantity=100, 
        unit_price=Decimal("3500.00")
    )  
    db.add(PurchaseItem)
    db.commit()
    db.refresh(PurchaseItem) 

     ### purchaseItem 2
    PurchaseItem(
        purchase_id=purchase.id,
        commodity_id=beans.id,
        quantity=100, 
        unit_price=Decimal("3500.00")
    )  
    db.add(PurchaseItem)
    db.commit()
    db.refresh(PurchaseItem) 





##close the script
finally:
    db.close()