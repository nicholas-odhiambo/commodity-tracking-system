
from sqlalchemy import Boolean,ForeignKey, Numeric
from decimal import Decimal
from sqlalchemy.orm import Mapped, mapped_column, relationship

## models related to the puchase item
from app.db.models.purchase import Purchase
from app.db.models.commodity import Commodity

from app.db.base import Base

class PurchaseItem(Base):
    __tablename__ = "purchase_item"
    id: Mapped[int] = mapped_column(primary_key=True)
    purchase_id: Mapped = mapped_column(ForeignKey("purchases.id"), nullable=False)
    commodity_id: Mapped[int] = mapped_column(ForeignKey("commodities.id"), nullable=False)
    quantity: Mapped[int] = mapped_column(nullable=False)
    unit_price: Mapped[Decimal] = mapped_column(Numeric(10,2), nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean,default=True, nullable=False) 
    
    #relationships 
    purchase = relationship("Purchase")
    commodity = relationship("Commodity")

    ## 
    purchase = relationship("Purchase", back_populates="purchase_items")
    commodity = relationship("Commodity", back_populates="purchase_items")

