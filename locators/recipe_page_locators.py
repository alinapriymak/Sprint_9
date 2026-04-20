from selenium.webdriver.common.by import By


class RecipePageLocators:
    """Локаторы страницы рецептов"""
    
    # Навигация
    CREATE_RECIPE_TAB = (By.XPATH, "//a[contains(text(), 'Создать рецепт')]")
    
    # Поля формы
    TITLE_INPUT = (By.XPATH, "//div[contains(text(), 'Название рецепта')]/following-sibling::input")
    DESCRIPTION_TEXTAREA = (By.XPATH, "//div[contains(text(), 'Описание')]/following-sibling::textarea")
    COOKING_TIME_INPUT = (By.XPATH, "//div[contains(text(), 'Время приготовления')]/following-sibling::input")
    
    # Ингредиенты
    INGREDIENT_INPUT = (By.CSS_SELECTOR, "input.styles_ingredientsInput__1zzql")
    INGREDIENT_QUANTITY = (By.CSS_SELECTOR, "input.styles_ingredientsAmountValue__2matT")
    ADD_INGREDIENT_BUTTON = (By.XPATH, "//div[contains(@class, 'styles_ingredientAdd__3fc32')]")
    # Список предложений ингредиентов
    INGREDIENT_SUGGESTIONS_CONTAINER = (By.CSS_SELECTOR, "div.styles_container__3ukwm")
    INGREDIENT_SUGGESTION_FIRST = (By.XPATH, "//div[contains(@class, 'styles_container__3ukwm')]/div[1]")
    # INGREDIENT_SUGGESTIONS_CONTAINER = (By.CLASS_NAME, "styles_container__3ukwm")
    # INGREDIENT_SUGGESTIONS_CONTAINER_ALT = (By.CSS_SELECTOR, "div.styles_container__3ukwm")
    # INGREDIENT_SUGGESTIONS_ITEMS = (By.XPATH, "//div[contains(@class, 'styles_container__3ukwm')]/div")
    # INGREDIENT_SUGGESTION_FIRST = (By.XPATH, "//div[contains(@class, 'styles_container__3ukwm')]/div[1]")
    
    # Загрузка изображения
    FILE_INPUT = (By.XPATH, "//input[@type='file']")
    
    # Кнопки
    SUBMIT_BUTTON = (By.XPATH, "//button[contains(text(), 'Создать рецепт')]")
    
    # Карточка рецепта
    RECIPE_CARD = (By.XPATH, "//div[contains(@class, 'recipe-card')]")
    RECIPE_TITLE = (By.XPATH, "//h2[contains(@class, 'recipe-title')]")