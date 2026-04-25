from __future__ import annotations

from datetime import datetime
from typing import Optional

from sqlalchemy import func
from sqlalchemy.orm import Session

from .models import Meal, Order


ACTIVE_STATUSES = ("Pending", "Preparing")


def estimate_waiting_time(db: Session, meal: Meal, quantity: int = 1) -> int:
    active_orders = db.query(Order).filter(Order.status.in_(ACTIVE_STATUSES)).count()
    queue_minutes = active_orders * 3
    prep_minutes = meal.preparation_time + max(quantity - 1, 0) * 2
    return min(max(prep_minutes + queue_minutes, 4), 45)


def recommendation_reason(meal: Meal) -> str:
    if meal.category == "Healthy":
        return "Option equilibree avec une bonne disponibilite pendant les pauses."
    if meal.category == "Budget etudiant":
        return "Excellent rapport qualite-prix pour les journees chargees."
    if meal.popularity_score >= 90:
        return "Tres populaire chez les etudiants FPK cette semaine."
    return "Choix rapide avec un temps de preparation previsible."


def recommend_meals(db: Session, category: Optional[str] = None, limit: int = 4) -> list[dict]:
    query = db.query(Meal).filter(Meal.is_available.is_(True))
    if category:
        query = query.filter(Meal.category == category)

    meals = (
        query.order_by(Meal.popularity_score.desc(), Meal.preparation_time.asc())
        .limit(limit)
        .all()
    )

    return [
        {
            "meal": meal,
            "reason": recommendation_reason(meal),
            "confidence": round(min(0.62 + meal.popularity_score / 260, 0.96), 2),
        }
        for meal in meals
    ]


def predict_peak_hours(db: Session) -> list[dict]:
    order_counts = dict(
        db.query(func.strftime("%H", Order.created_at), func.count(Order.id))
        .group_by(func.strftime("%H", Order.created_at))
        .all()
    )

    # Combines sample order history with the known FPK break rhythm.
    campus_pattern = {
        "08:00": 45,
        "10:00": 82,
        "12:00": 96,
        "13:00": 88,
        "15:00": 74,
        "17:00": 51,
    }

    predictions = []
    for hour_label, baseline in campus_pattern.items():
        hour_key = hour_label[:2]
        observed = int(order_counts.get(hour_key, 0))
        demand_score = min(baseline + observed * 4, 100)
        predictions.append(
            {
                "hour": hour_label,
                "demand_score": demand_score,
                "level": "High" if demand_score >= 80 else "Medium" if demand_score >= 60 else "Low",
                "recommendation": "Precommander 20 min avant" if demand_score >= 80 else "Precommander 10 min avant",
            }
        )

    return predictions


def build_ai_summary(db: Session) -> dict:
    active_orders = db.query(Order).filter(Order.status.in_(ACTIVE_STATUSES)).count()
    top_meal = db.query(Meal).order_by(Meal.popularity_score.desc()).first()
    current_hour = datetime.utcnow().hour
    is_peak_now = current_hour in (10, 12, 13, 15)

    return {
        "active_orders": active_orders,
        "top_recommendation": top_meal.name if top_meal else "Aucun plat",
        "campus_load": "Elevee" if is_peak_now or active_orders >= 5 else "Normale",
        "insight": "Les precommandes peuvent economiser 12 a 20 minutes pendant les pics de pause.",
    }
