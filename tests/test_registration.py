import pytest
import allure
from pages.registration_page import RegistrationPage
from pages.login_page import LoginPage


@allure.feature("Создание аккаунта")
class TestRegistration:
    
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.driver = driver
        self.registration_page = RegistrationPage(driver)
        self.login_page = LoginPage(driver)
    
    @allure.title("Создание аккаунта")
    def test_create_account(self, test_user_data):
        with allure.step("Открыть страницу регистрации"):
            self.registration_page.open()
        
        with allure.step("Заполнить поле Имя"):
            self.registration_page.input_first_name(test_user_data["first_name"])
        
        with allure.step("Заполнить поле Фамилия"):
            self.registration_page.input_last_name(test_user_data["last_name"])
        
        with allure.step("Заполнить поле Имя пользователя"):
            self.registration_page.input_username(test_user_data["username"])
        
        with allure.step("Заполнить поле Email"):
            self.registration_page.input_email(test_user_data["email"])
        
        with allure.step("Заполнить поле Пароль"):
            self.registration_page.input_password(test_user_data["password"])
        
        with allure.step("Нажать кнопку «Создать аккаунт»"):
            self.registration_page.click_create_account_button()
        
        with allure.step("Проверить, что произошел переход на страницу авторизации"):
            assert self.registration_page.is_redirected_to_login_page()
        
        with allure.step("Проверить, что отображается форма авторизации"):
            assert self.login_page.is_login_form_visible()