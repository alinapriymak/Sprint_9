from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import allure


class BasePage:
    
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout
        self.wait = WebDriverWait(driver, timeout)
    
    @allure.step("Найти элемент на странице") 
    def find_element(self, locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        )
    
    @allure.step("Кликнуть по элементу") 
    def click(self, locator):
        element = self.find_element(locator)
        element.click()
        return self
    
    @allure.step("Ввести текст в поле") 
    def input_text(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)
        return self
    
    @allure.step("Получить текст")
    def get_text(self, locator):
        return self.find_element(locator).text
    
    @allure.step("Проверить видимость элемента")
    def is_element_visible(self, locator, timeout=None):
        try:
            wait = WebDriverWait(self.driver, timeout or self.timeout)
            wait.until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False
    
    @allure.step("Проверить урл")
    def wait_for_url_contains(self, text):
        self.wait.until(EC.url_contains(text))
        return self
    
    @allure.step("Получить текущий урл")
    def get_current_url(self):
        return self.driver.current_url