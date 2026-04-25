from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class MealBase(BaseModel):
    name: str = Field(..., min_length=2, max_length=120)
    category: str = Field(..., min_length=2, max_length=60)
    price: float = Field(..., ge=1, le=200)
    description: str = Field(..., min_length=5)
    image_url: str
    preparation_time: int = Field(..., ge=1, le=90)
    is_available: bool = True
    popularity_score: int = Field(default=50, ge=0, le=100)


class MealCreate(MealBase):
    pass


class MealRead(MealBase):
    model_config = ConfigDict(from_attributes=True)

    id: int


class OrderCreate(BaseModel):
    student_name: str = Field(..., min_length=2, max_length=120)
    student_department: str = Field(..., min_length=2, max_length=120)
    meal_id: int
    quantity: int = Field(default=1, ge=1, le=10)
    pickup_time: str = Field(..., min_length=4, max_length=20)


class OrderStatusUpdate(BaseModel):
    status: str = Field(..., pattern="^(Pending|Preparing|Ready|Completed)$")


class OrderRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    student_name: str
    student_department: str
    meal_id: int
    quantity: int
    pickup_time: str
    status: str
    total_price: float
    estimated_waiting_time: int
    created_at: datetime
    meal: MealRead


class RecommendationItem(BaseModel):
    meal: MealRead
    reason: str
    confidence: float


class DashboardStats(BaseModel):
    total_orders: int
    revenue_today: float
    average_waiting_time: float
    popular_meal: str
    orders_per_hour: list[dict]
    popular_meals: list[dict]
    waiting_time_by_hour: list[dict]
