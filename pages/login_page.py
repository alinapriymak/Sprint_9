from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators
from utils.urls import SIGNIN_PAGE
import allure


class LoginPage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = LoginPageLocators()
    
    @allure.step("Открыть страницу логина")
    def open(self):
        self.driver.get(SIGNIN_PAGE)
        return self
    
    @allure.step("Кликнуть на кнопку 'Войти'")
    def click_login_button(self):
        self.click(self.locators.LOGIN_BUTTON)
        return self
    
    @allure.step("Ввести email")
    def input_email(self, email):
        self.input_text(self.locators.EMAIL_INPUT, email)
        return self
    
    @allure.step("Ввести пароль")
    def input_password(self, password):
        self.input_text(self.locators.PASSWORD_INPUT, password)
        return self
    
    @allure.step("Проверить видимость формы авторизации")
    def is_login_form_visible(self):
        return self.is_element_visible(self.locators.LOGIN_FORM)
    
    @allure.step("Проверить видимость кнопки 'Выйти'")
    def is_logout_button_visible(self):
        return self.is_element_visible(self.locators.LOGOUT_BUTTON, timeout=5)
    
    @allure.step("Дождаться перехода на страницу рецептов после успешного входа")
    def wait_for_redirect_after_login(self):
        self.wait_for_url_contains("/recipes")
        return "/recipes" in self.get_current_url()
    
    @allure.step("Кликнуть на кнопку 'Выйти'")
    def click_logout_button(self):
        if self.is_element_visible(self.locators.LOGOUT_BUTTON):
            self.click(self.locators.LOGOUT_BUTTON)
        return self