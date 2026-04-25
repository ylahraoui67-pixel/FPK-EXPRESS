from datetime import datetime

from sqlalchemy.orm import Session

from .models import Meal, Order


MEALS = [
    {
        "name": "Sandwich Poulet",
        "category": "Sandwichs",
        "price": 18,
        "description": "Poulet grille, salade, tomate, sauce maison et pain frais.",
        "image_url": "https://images.unsplash.com/photo-1553909489-cd47e0907980?auto=format&fit=crop&w=900&q=80",
        "preparation_time": 8,
        "is_available": True,
        "popularity_score": 94,
    },
    {
        "name": "Tacos Mixte",
        "category": "Tacos",
        "price": 32,
        "description": "Tacos poulet et viande hachee avec frites et sauce fromagere.",
        "image_url": "https://images.unsplash.com/photo-1624300629298-e9de39c13be8?auto=format&fit=crop&w=900&q=80",
        "preparation_time": 14,
        "is_available": True,
        "popularity_score": 91,
    },
    {
        "name": "Panini Thon",
        "category": "Sandwichs",
        "price": 16,
        "description": "Panini chaud au thon, fromage, olives et mais.",
        "image_url": "https://images.unsplash.com/photo-1528735602780-2552fd46c7af?auto=format&fit=crop&w=900&q=80",
        "preparation_time": 7,
        "is_available": True,
        "popularity_score": 78,
    },
    {
        "name": "Salade Healthy",
        "category": "Healthy",
        "price": 24,
        "description": "Riz, legumes frais, oeuf, thon, mais et vinaigrette legere.",
        "image_url": "https://images.unsplash.com/photo-1512621776951-a57141f2eefd?auto=format&fit=crop&w=900&q=80",
        "preparation_time": 6,
        "is_available": True,
        "popularity_score": 86,
    },
    {
        "name": "Jus d'orange",
        "category": "Boissons",
        "price": 10,
        "description": "Jus d'orange frais, parfait avant un cours du matin.",
        "image_url": "https://images.unsplash.com/photo-1600271886742-f049cd451bba?auto=format&fit=crop&w=900&q=80",
        "preparation_time": 4,
        "is_available": True,
        "popularity_score": 84,
    },
    {
        "name": "Cafe",
        "category": "Boissons",
        "price": 5,
        "description": "Cafe noir rapide pour les pauses courtes.",
        "image_url": "https://images.unsplash.com/photo-1495474472287-4d71bcdd2085?auto=format&fit=crop&w=900&q=80",
        "preparation_time": 3,
        "is_available": True,
        "popularity_score": 88,
    },
    {
        "name": "Couscous Friday Bowl",
        "category": "Healthy",
        "price": 35,
        "description": "Bol couscous revisite avec legumes, pois chiches et poulet.",
        "image_url": "https://images.unsplash.com/photo-1585937421612-70a008356fbe?auto=format&fit=crop&w=900&q=80",
        "preparation_time": 12,
        "is_available": True,
        "popularity_score": 89,
    },
    {
        "name": "Budget Student Menu",
        "category": "Budget etudiant",
        "price": 20,
        "description": "Mini sandwich, boisson et fruit pour un repas simple et abordable.",
        "image_url": "https://images.unsplash.com/photo-1542838132-92c53300491e?auto=format&fit=crop&w=900&q=80",
        "preparation_time": 6,
        "is_available": True,
        "popularity_score": 93,
    },
]


def seed_database(db: Session) -> None:
    if db.query(Meal).count() == 0:
        meals = [Meal(**item) for item in MEALS]
        db.add_all(meals)
        db.commit()

    if db.query(Order).count() > 0:
        return

    meals_by_name = {meal.name: meal for meal in db.query(Meal).all()}
    today = datetime.utcnow().replace(second=0, microsecond=0)
    sample_orders = [
        ("Sara El Amrani", "GI", "Cafe", 1, "08:40", "Completed", 6, 8, 40),
        ("Yassine Berrada", "MIP", "Sandwich Poulet", 1, "10:15", "Completed", 10, 10, 15),
        ("Hiba Mansouri", "BCG", "Salade Healthy", 1, "12:20", "Ready", 9, 12, 20),
        ("Omar Idrissi", "SMA", "Tacos Mixte", 1, "12:35", "Preparing", 17, 12, 35),
        ("Nour Saidi", "GI", "Budget Student Menu", 1, "13:10", "Pending", 12, 13, 10),
        ("Amine Ziani", "PC", "Jus d'orange", 2, "15:05", "Completed", 7, 15, 5),
        ("Meryem Alaoui", "MIP", "Panini Thon", 1, "15:20", "Completed", 8, 15, 20),
        ("Karim Naciri", "GI", "Sandwich Poulet", 1, "10:35", "Completed", 9, 10, 35),
        ("Lina Qasmi", "MIP", "Budget Student Menu", 1, "12:45", "Completed", 11, 12, 45),
        ("Salma Radi", "BCG", "Sandwich Poulet", 1, "13:25", "Completed", 9, 13, 25),
        ("Anas Bennani", "PC", "Tacos Mixte", 1, "15:40", "Ready", 15, 15, 40),
        ("Imane Fassi", "SVI", "Cafe", 1, "16:10", "Completed", 5, 16, 10),
    ]

    for student, department, meal_name, quantity, pickup, status, wait, hour, minute in sample_orders:
        meal = meals_by_name[meal_name]
        db.add(
            Order(
                student_name=student,
                student_department=department,
                meal_id=meal.id,
                quantity=quantity,
                pickup_time=pickup,
                status=status,
                total_price=round(meal.price * quantity + 1.0, 2),
                estimated_waiting_time=wait,
                created_at=today.replace(hour=hour, minute=minute),
            )
        )

    db.commit()
