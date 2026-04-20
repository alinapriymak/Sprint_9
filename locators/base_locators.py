
from selenium.webdriver.common.by import By


class BaseLocators:
    """Базовые локаторы, используемые на всех страницах"""
    
    # Навигация
    HEADER = (By.TAG_NAME, "header")
    FOOTER = (By.TAG_NAME, "footer")
    MAIN_CONTENT = (By.TAG_NAME, "main")
    
    # Общие элементы
    LOADER = (By.CLASS_NAME, "loader")
    MODAL = (By.CLASS_NAME, "modal")
    MODAL_CLOSE = (By.CLASS_NAME, "modal-close")
    TOAST_MESSAGE = (By.CLASS_NAME, "toast-message")
    ERROR_MESSAGE = (By.CLASS_NAME, "error-message")
    SUCCESS_MESSAGE = (By.CLASS_NAME, "success-message")
    
    # Кнопки
    SUBMIT_BUTTON = (By.XPATH, "//button[@type='submit']")
    CANCEL_BUTTON = (By.XPATH, "//button[contains(text(), 'Отмена')]")
    BACK_BUTTON = (By.XPATH, "//button[contains(text(), 'Назад')]")
    
    # Сообщения
    ALERT_DANGER = (By.CLASS_NAME, "alert-danger")
    ALERT_SUCCESS = (By.CLASS_NAME, "alert-success")
    ALERT_WARNING = (By.CLASS_NAME, "alert-warning")
    
    @staticmethod
    def get_button_by_text(text: str):
        """Получение кнопки по тексту"""
        return (By.XPATH, f"//button[contains(text(), '{text}')]")
    
    @staticmethod
    def get_link_by_text(text: str):
        """Получение ссылки по тексту"""
        return (By.XPATH, f"//a[contains(text(), '{text}')]")