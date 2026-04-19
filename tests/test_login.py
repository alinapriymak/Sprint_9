import pytest
import allure
import time
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage


@allure.feature("Авторизация")
class TestLogin:
    
    @pytest.fixture(autouse=True)
    def setup(self, driver, test_user_data):
        self.driver = driver
        self.login_page = LoginPage(driver)
        self.registration_page = RegistrationPage(driver)
        self.test_user_data = test_user_data
        
        # Создание пользователя 
        with allure.step(f"Создать тестового пользователя {self.test_user_data['username']}"):
            self.registration_page.open()
            self.registration_page.input_first_name(self.test_user_data["first_name"])
            self.registration_page.input_last_name(self.test_user_data["last_name"])
            self.registration_page.input_username(self.test_user_data["username"])
            self.registration_page.input_email(self.test_user_data["email"])
            self.registration_page.input_password(self.test_user_data["password"])
            self.registration_page.click_create_account_button()
            
            time.sleep(2)
            print(f"1. URL after registration: {self.driver.current_url}")
    
    @allure.title("Авторизация")
    def test_login(self):
        with allure.step("Нажать кнопку «Войти»"):
            self.login_page.open()
        
        with allure.step("Заполнить поле Email (используем username)"):
            self.login_page.input_email(self.test_user_data["username"])
        
        with allure.step("Заполнить поле Пароль"):
            self.login_page.input_password(self.test_user_data["password"])
        
        with allure.step("Нажать кнопку «Войти»"):
            self.login_page.click_login_button()
            print(f"5. Clicked login button")
        
        with allure.step("Проверить, что произошел переход на страницу рецептов"):
            assert self.login_page.wait_for_redirect_after_login()
        
        with allure.step("Проверить, что отображается кнопка «Выход»"):
            assert self.login_page.is_logout_button_visible()