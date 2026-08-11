from sqlalchemy.orm import Session

from app.db.models.purchase import Purchase
from app.db.models.purchase_item import PurchaseItem


class PurchaseRepository:

    def __init__(self,db: Session ):
        self.db = db 

    ## create the purchase 
    def create_purchase(self, supplier_id: int, warehouse_id: int, items: list[dict]):

        try:
            purchase = Purchase(
                supplier_id = supplier_id,
                warehouse_id = warehouse_id
                )
            self.db.add(purchase)
            self.db.flush()

            #create purchase items 
            for item in items:
                purchase_item = PurchaseItem(
                    purchase_id = purchase.id,
                    commodity_id = item["commodity_id"],
                    quantity = item["quantity"],
                    unit_price = item["unit_price"]
                    )
                self.db.add(purchase_item)

            self.db.commit()
            self.db.refresh(purchase)
            return purchase
        except Exception:
            self.db.rollback()
            raise
