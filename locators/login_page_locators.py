from selenium.webdriver.common.by import By


class LoginPageLocators:
    """Локаторы страницы авторизации"""
    
    # Поля ввода
    EMAIL_INPUT = (By.NAME, "email")
    PASSWORD_INPUT = (By.NAME, "password")
    
    # Кнопки
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Войти')]")
    LOGOUT_BUTTON = (By.XPATH, "//a[contains(text(), 'Выход')]")
    
    # Форма
    LOGIN_FORM = (By.XPATH, "//form")