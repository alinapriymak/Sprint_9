from pages.base_page import BasePage
from locators.registration_page_locators import RegistrationPageLocators
from utils.urls import SIGNUP_PAGE
import allure


class RegistrationPage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = RegistrationPageLocators()
    
    @allure.step("Открыть страницу регистрации") 
    def open(self):
        self.driver.get(SIGNUP_PAGE)
        return self
    
    # @allure.step("Заполнить форму регистрации") 
    # def register(self, username, email, password, first_name=None, last_name=None):
    #     if first_name:
    #         self.input_text(self.locators.FIRST_NAME_INPUT, first_name)
    #     if last_name:
    #         self.input_text(self.locators.LAST_NAME_INPUT, last_name)
    #     self.input_text(self.locators.USERNAME_INPUT, username)
    #     self.input_text(self.locators.EMAIL_INPUT, email)
    #     self.input_text(self.locators.PASSWORD_INPUT, password)
    #     self.click(self.locators.REGISTER_BUTTON)
    #     return self
    

    def input_first_name(self, first_name):
        self.input_text(self.locators.FIRST_NAME_INPUT, first_name)
        return self
    
    def input_last_name(self, last_name):
        self.input_text(self.locators.LAST_NAME_INPUT, last_name)
        return self
    
    def input_username(self, username):
        self.input_text(self.locators.USERNAME_INPUT, username)
        return self
    
    def input_email(self, email):
        self.input_text(self.locators.EMAIL_INPUT, email)
        return self
    
    def input_password(self, password):
        self.input_text(self.locators.PASSWORD_INPUT, password)
        return self
    
    @allure.step("Кликнуть на 'Создать аккаунт'") 
    def click_create_account_button(self):
        self.click(self.locators.REGISTER_BUTTON)
        return self
    
    @allure.step("Проверить, что произошел редирект на страницу логина") 
    def is_redirected_to_login_page(self):
        self.wait_for_url_contains("/signin")
        return "/signin" in self.get_current_url()