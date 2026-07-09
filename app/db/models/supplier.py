from sqlalchemy import String, Boolean, DateTime, func
import datetime
from typing import Optional
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base

class Supplier(Base):
    __tablename__ = "suppliers"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]=mapped_column(String(100),unique=True, nullable=False )
    phone: Mapped[str] = mapped_column(String(20),unique=True, nullable=False)
    email: Mapped[Optional[str]] = mapped_column(String(200), unique=True, nullable=True)
    date_registered: Mapped[datetime.datetime] = mapped_column(DateTime, server_default=func.now())
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)