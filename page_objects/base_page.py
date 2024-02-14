from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Открытие страницы")
    def go_to_site(self, url):
        self.driver.get(url)

    @allure.step("Нахождение элемента")
    def wait_for_element_visibility(self, locator, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        element = wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        return element

    @allure.step("Клик по элементу")
    def wait_for_element_visibility_click(self, locator, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.element_to_be_clickable(locator)).click()
