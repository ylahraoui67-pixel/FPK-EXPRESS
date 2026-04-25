from datetime import datetime

from sqlalchemy import Boolean, DateTime, Float, ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .database import Base


class Meal(Base):
    __tablename__ = "meals"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(120), index=True)
    category: Mapped[str] = mapped_column(String(60), index=True)
    price: Mapped[float] = mapped_column(Float)
    description: Mapped[str] = mapped_column(Text)
    image_url: Mapped[str] = mapped_column(String(500))
    preparation_time: Mapped[int] = mapped_column(Integer)
    is_available: Mapped[bool] = mapped_column(Boolean, default=True)
    popularity_score: Mapped[int] = mapped_column(Integer, default=50)

    orders: Mapped[list["Order"]] = relationship(back_populates="meal")


class Order(Base):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    student_name: Mapped[str] = mapped_column(String(120), index=True)
    student_department: Mapped[str] = mapped_column(String(120), index=True)
    meal_id: Mapped[int] = mapped_column(ForeignKey("meals.id"))
    quantity: Mapped[int] = mapped_column(Integer, default=1)
    pickup_time: Mapped[str] = mapped_column(String(20))
    status: Mapped[str] = mapped_column(String(30), default="Pending", index=True)
    total_price: Mapped[float] = mapped_column(Float)
    estimated_waiting_time: Mapped[int] = mapped_column(Integer)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, index=True)

    meal: Mapped[Meal] = relationship(back_populates="orders")
