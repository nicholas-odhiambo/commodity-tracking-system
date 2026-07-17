from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String,Boolean, DateTime, func
from typing import Optional
import datetime

from app.db.base import Base

class Customer(Base):
    __tablename__ = "customers"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    phone: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    email: Mapped[Optional[str]] = mapped_column(String(100), nullable=True, unique=True)
    date_registered: Mapped[datetime.datetime] = mapped_column(DateTime, server_default=func.now())
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)


