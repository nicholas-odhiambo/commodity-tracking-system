from decimal import Decimal

from app.db.session import SessionLocal

#imports 
from app.db.models.supplier import Supplier
from app.db.models.warehouse import Warehouse
from app.db.models.commodity import Commodity
from app.repositories.purchase_repository import PurchaseRepository

#create session 

db = SessionLocal()

try:
    supplier = db.query(Supplier).filter_by(name="ABC Suppliers").first()
    warehouse = db.query(Warehouse).filter_by(name="The Millers").first()
    grapes = db.query(Commodity).filter_by(name="grapes").first()
    apples = db.query(Commodity).filter_by(name="apples").first()

    #create the repository 
    repo = PurchaseRepository(db)

    ## items 

    items = [
        {
            "commodity_id": grapes.id, 
            "quantity": 100,
            "unit_price": Decimal("3500.00")
        },
        {
            "commodity_id": grapes.id, 
            "quantity": 100,
            "unit_price": Decimal("3500.00")
        }
    ]

    ## call the repository 
    
    purchase = repo.create_purchase(
        supplier_id = supplier.id,
        warehouse_id = warehouse.id,
        items = items
    )

    #
    print(f"Purchase ID: {purchase.id}")
    print(f"Supplier ID: {purchase.supplier_id}")
    print(f"Warehouse {purchase.warehouse_id}")

    ## 
    for item in purchase.purchase_items:
        print("-----------------------")
        print(f"Purchase Item ID: {item.id}")
        print(f"Commodity ID: {item.commodity_id}")
        print(f"Quantity: {item.quantity}")
        print(f"Unit Price: {item.unit_price}")
finally:
    db.close()
