from pathlib import Path
import allure
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators.recipe_page_locators import RecipePageLocators
from utils.urls import RECIPES_PAGE
import time
from selenium.webdriver.common.by import By

class RecipePage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = RecipePageLocators()
    
    @allure.step("Кликнуть на кнопку 'Создать рецепт")
    def click_create_recipe_tab(self):
        self.click(self.locators.CREATE_RECIPE_TAB)
        return self
    
    @allure.step("Ввести название")
    def input_title(self, title):
        self.input_text(self.locators.TITLE_INPUT, title)
        return self
    
    @allure.step("Ввести описание")
    def input_description(self, description):
        self.input_text(self.locators.DESCRIPTION_TEXTAREA, description)
        return self
    
    @allure.step("Ввести время приготовления")
    def input_cooking_time(self, cooking_time):
        self.input_text(self.locators.COOKING_TIME_INPUT, str(cooking_time))
        return self
    
    @allure.step("Добавить ингредиенты из списка") 
    def add_ingredient(self, name, quantity):
        partial_name = name[:3] if len(name) >= 3 else name
        ingredient_input = self.find_element(self.locators.INGREDIENT_INPUT)
        ingredient_input.clear()
        ingredient_input.send_keys(partial_name)
        
        # Ждем появления списка предложений
        self.wait.until(EC.visibility_of_element_located(self.locators.INGREDIENT_SUGGESTIONS_CONTAINER))
        
        # Выбираем первый элемент из списка
        first_suggestion = self.find_element(self.locators.INGREDIENT_SUGGESTION_FIRST)
        first_suggestion.click()
        
        # Вводим количество
        quantity_input = self.find_element(self.locators.INGREDIENT_QUANTITY)
        quantity_input.clear()
        quantity_input.send_keys(quantity)
        
        # Нажимаем кнопку "Добавить ингредиент"
        self.click(self.locators.ADD_INGREDIENT_BUTTON)
        
        return self
    
    @allure.step("Загрузить изображение") 
    def upload_image(self, file_path):
    
        # Пробуем найти поле загрузки разными способами
        file_input = None
    
        # Способ 1: через XPATH
        try:
            file_input = self.driver.find_element(By.XPATH, "//input[@type='file']")
            print("Found by XPATH")
        except:
            print("Not found by XPATH")
    
        # Способ 2: через CSS
        if not file_input:
            try:
                file_input = self.driver.find_element(By.CSS_SELECTOR, "input[type='file']")
                print("Found by CSS")
            except:
                print("Not found by CSS")
    
        # Способ 3: ищем все input и проверяем тип
        if not file_input:
            try:
                all_inputs = self.driver.find_elements(By.TAG_NAME, "input")
                for inp in all_inputs:
                    if inp.get_attribute("type") == "file":
                        file_input = inp
                        print("Found by iterating inputs")
                        break
            except:
                print("Not found by iterating")
    
        # Способ 4: через JavaScript
        if not file_input:
            try:
                file_input = self.driver.execute_script("return document.querySelector('input[type=\"file\"]');")
                print("Found by JS")
            except:
                print("Not found by JS")
    
        # Скроллим к элементу
        self.driver.execute_script("arguments[0].scrollIntoView(true);", file_input)
        time.sleep(1)
    
        # Отправляем файл
        absolute_path = str(file_path.absolute())
        file_input.send_keys(absolute_path)
    
        return self
    
    @allure.step("Кликнуть на кнопку подтверждения") 
    def click_submit_button(self):
        self.click(self.locators.SUBMIT_BUTTON)
        return self
    
    @allure.step("Проверить видимость карточки рецепта") 
    def is_recipe_card_visible(self):
        return self.is_element_visible(self.locators.RECIPE_CARD)
    
    @allure.step("Получить название рецепта") 
    def get_recipe_title(self):
        if self.is_element_visible(self.locators.RECIPE_TITLE):
            return self.get_text(self.locators.RECIPE_TITLE)
        return ""
    
    
    @allure.step("Перейти на страницу рецептов") 
    def go_to_recipes_page(self):
        self.driver.get(RECIPES_PAGE)
        return self

    @allure.step("Проверить, что карточка созданного рецепта есть на странице рецептов") 
    def is_recipe_card_visible_with_title(self, expected_title):
        self.wait.until(EC.text_to_be_present_in_element(
            (By.TAG_NAME, "body"), 
            expected_title
        ))
        return expected_title in self.driver.find_element(By.TAG_NAME, "body").text