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
    if supplier is None:
        supplier = Supplier(name="ABC Suppliers", phone="0709876587")
        db.add(supplier)
        db.commit()
        db.refresh(supplier)

    warehouse = db.query(Warehouse).filter_by(name="The Millers").first()
    if warehouse is None:
        warehouse = Warehouse(name="The Millers", location="South K", capacity=2000)
        db.add(warehouse)
        db.commit()
        db.refresh(warehouse)

    grapes = db.query(Commodity).filter_by(name="grapes").first()
    if grapes is None:
        grapes = Commodity(name="grapes",unit_of_measure=60)
        db.add(grapes)
        db.commit()
        db.refresh(grapes)
     

    apples = db.query(Commodity).filter_by(name="apples").first()
    if apples is None:
        apples = Commodity(name="apples", unit_of_measure=70)
        db.add(apples)
        db.commit()
        db.refresh(apples)


    ## A purchase
    purchase = Purchase(
        supplier_id=supplier.id,
        warehouse_id=warehouse.id
    )
    db.add(purchase)
    db.commit()
    db.refresh(purchase)

    ### purchaseItem 1
    purchaseitem1 = PurchaseItem(
        purchase_id=purchase.id,
        commodity_id=grapes.id,
        quantity=100, 
        unit_price=Decimal("3500.00")
    )  
    db.add(purchaseitem1)
    db.commit()
    db.refresh(purchaseitem1) 

     ### purchaseItem 2
    ### purchaseItem 1
    purchaseitem2 = PurchaseItem(
        purchase_id=purchase.id,
        commodity_id=apples.id,
        quantity=100, 
        unit_price=Decimal("3500.00")
    )  
    db.add(purchaseitem2)
    db.commit()
    db.refresh(purchaseitem2) 

    ## retrieve purchase 
    saved_purchase = (
        db.query(Purchase).filter(Purchase.id == purchase.id).first()
    )

    ## test every relationship 
    print(f"Purchase ID: {saved_purchase.id}")
    print(f"Supplier: {saved_purchase.supplier.name}")
    print(f"warehouse: {saved_purchase.warehouse.name}")

    for item in saved_purchase.purchase_items:
        print("-----------------------")
        print(item.commodity.name)
        print(item.quantity)
        print(item.unit_price)





##close the script
finally:
    db.close()