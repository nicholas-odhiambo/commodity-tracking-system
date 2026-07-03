from sqlalchemy import String, Boolean
from typing import Optional
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base

class Commodity(Base):
    __tablename__ = "commodities"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100),unique=True,nullable=False)
    unit_of_measure: Mapped[str] = mapped_column(String(30),nullable=False) 
    description: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)