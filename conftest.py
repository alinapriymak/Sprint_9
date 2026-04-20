import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pathlib import Path


@pytest.fixture(scope="function")
def driver():
    """Фикстура для создания экземпляра драйвера"""
    selenoid_url = "http://localhost:4444/wd/hub"
    
    chrome_options = Options()
    chrome_options.set_capability("browserName", "chrome")
    chrome_options.set_capability("browserVersion", "128.0")
    chrome_options.set_capability("selenoid:options", {
        "enableVNC": True,
        "enableVideo": False
    })
    
    driver = webdriver.Remote(
        command_executor=selenoid_url,
        options=chrome_options
    )
    
    driver.maximize_window()
    
    yield driver
    
    driver.quit()


@pytest.fixture(scope="function")
def test_user_data():
    """Фикстура с тестовыми данными пользователя"""
    from utils.data import generate_unique_username, generate_unique_email, generate_valid_password, generate_first_name, generate_last_name
    
    return {
        "username": generate_unique_username(),
        "email": generate_unique_email(),
        "password": generate_valid_password(),
        "first_name": generate_first_name(),
        "last_name": generate_last_name()
    }


@pytest.fixture(scope="function")
def test_recipe_data():
    """Фикстура с тестовыми данными рецепта"""
    from utils.data import generate_recipe_title, generate_recipe_description, generate_ingredients, generate_cooking_time
    
    return {
        "title": generate_recipe_title(),
        "description": generate_recipe_description(),
        "ingredients": generate_ingredients(),
        "cooking_time": generate_cooking_time()
    }


@pytest.fixture(scope="function")
def test_image_path():
    """Фикстура с путем к тестовому изображению"""
    project_root = Path(__file__).parent
    image_path = project_root / "assets" / "manul.jpg"
    #image_path = Path("/Users/alinaprijmak/Sprint_9/assets/manul.jpg")
    
    # Проверяем, существует ли файл
    if not image_path.exists():
        raise FileNotFoundError(f"Test image not found at {image_path}")
    
    print(f"Image path: {image_path}")
    return image_path