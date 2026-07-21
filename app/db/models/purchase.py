from sqlalchemy import Boolean, func, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
import datetime

from app.db.base import Base

## warehouse and supplier models for the relationship

from app.db.models.warehouse import Warehouse
from app.db.models.supplier import Supplier

class Purchase(Base):
    __tablename__ = "purchases"
    id: Mapped[int] = mapped_column(primary_key=True)
    supplier_id: Mapped[int] = mapped_column(ForeignKey("suppliers.id"), nullable=False)
    warehouse_id: Mapped[int] = mapped_column(ForeignKey("warehouses.id"), nullable=False)
    purchase_date: Mapped[datetime.datetime] =mapped_column(DateTime, server_default=func.now())
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)

    ## relationships 
    supplier = relationship("Supplier")
    warehouse = relationship("Warehouse")

    ##
    purchase_items= relationship("PurchaseItem", back_populates="purchase")