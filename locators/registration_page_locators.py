from selenium.webdriver.common.by import By


class RegistrationPageLocators:
    """Локаторы страницы регистрации"""
    
    # Поля ввода
    FIRST_NAME_INPUT = (By.NAME, "first_name")  
    LAST_NAME_INPUT = (By.NAME, "last_name")   
    USERNAME_INPUT = (By.NAME, "username")    
    EMAIL_INPUT = (By.NAME, "email")            
    PASSWORD_INPUT = (By.NAME, "password") 
    
    # Кнопки
    REGISTER_BUTTON = (By.XPATH, "//button[contains(text(), 'Создать аккаунт')]")
    
    # Ссылки
    SIGNIN_LINK = (By.XPATH, "//a[contains(text(), 'Войти')]")
    
    # Форма
    REGISTRATION_FORM = (By.XPATH, "//form")