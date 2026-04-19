import uuid
from faker import Faker

fake = Faker()


def generate_unique_username():
    """Генерация уникального username"""
    return f"testuser_{uuid.uuid4().hex[:8]}"

def generate_first_name():
    """Генерация имени"""
    return fake.first_name()


def generate_last_name():
    """Генерация фамилии"""
    return fake.last_name()


def generate_unique_email():
    """Генерация уникального email"""
    return f"test_{uuid.uuid4().hex[:8]}@example.com"


def generate_valid_password():
    """Генерация валидного пароля"""
    return f"TestPass_{uuid.uuid4().hex[:8]}!"


def generate_weak_password():
    """Генерация слабого пароля"""
    return "123"


def generate_recipe_title():
    """Генерация названия рецепта"""
    return f"Тестовый рецепт {uuid.uuid4().hex[:4]}"


def generate_recipe_description():
    """Генерация описания рецепта"""
    return f"Описание тестового рецепта {uuid.uuid4().hex[:4]}"


def generate_ingredients():
    """Генерация ингредиентов"""
    return [
        {"name": "мука", "quantity": "500"},
        {"name": "сахар", "quantity": "200"},
        {"name": "яйцо", "quantity": "3"}
    ]


def generate_cooking_time():
    """Генерация времени приготовления"""
    return 60