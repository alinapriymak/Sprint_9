import pytest
import allure
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage
from pages.recipe_page import RecipePage


@allure.feature("Создание рецепта")
class TestRecipe:
    
    @pytest.fixture(autouse=True)
    def setup(self, driver, test_user_data, test_recipe_data, test_image_path):
        self.driver = driver
        self.login_page = LoginPage(driver)
        self.registration_page = RegistrationPage(driver)
        self.recipe_page = RecipePage(driver)
        self.test_user_data = test_user_data
        self.test_recipe_data = test_recipe_data
        self.test_image_path = test_image_path
        
        # Создание пользователя
        with allure.step("Создать пользователя"):
            self.registration_page.open()
            self.registration_page.input_first_name(self.test_user_data["first_name"])
            self.registration_page.input_last_name(self.test_user_data["last_name"])
            self.registration_page.input_username(self.test_user_data["username"])
            self.registration_page.input_email(self.test_user_data["email"])
            self.registration_page.input_password(self.test_user_data["password"])
            self.registration_page.click_create_account_button()
        
        # Авторизация
        with allure.step("Авторизоваться"):
            self.login_page.open()
            self.login_page.input_email(self.test_user_data["username"])
            self.login_page.input_password(self.test_user_data["password"])
            self.login_page.click_login_button()
            self.login_page.wait_for_redirect_after_login()
    
    @allure.title("Создание рецепта")
    def test_create_recipe(self):
        with allure.step("Перейти на таб «Создать рецепт»"):
            self.recipe_page.click_create_recipe_tab()
        
        with allure.step("Заполнить поле Название рецепта"):
            self.recipe_page.input_title(self.test_recipe_data["title"])
        
        with allure.step("Заполнить поле Описание"):
            self.recipe_page.input_description(self.test_recipe_data["description"])
        
        with allure.step("Добавить ингредиенты"):
            for ingredient in self.test_recipe_data["ingredients"]:
                self.recipe_page.add_ingredient(ingredient["name"], ingredient["quantity"])
        
        with allure.step("Заполнить поле Время приготовления"):
            self.recipe_page.input_cooking_time(self.test_recipe_data["cooking_time"])
        
        with allure.step("Загрузить изображение"):
            self.recipe_page.upload_image(self.test_image_path)
        
        with allure.step("Нажать кнопку «Создать рецепт»"):
            self.recipe_page.click_submit_button()
        
        with allure.step("Нажать кнопку «Создать рецепт»"):
            self.recipe_page.click_submit_button()
        

        with allure.step("Перейти на страницу рецептов"):
            self.recipe_page.go_to_recipes_page()
        
        with allure.step("Проверить, что отображается карточка созданного рецепта"):
            assert self.recipe_page.is_recipe_card_visible_with_title(self.test_recipe_data["title"])