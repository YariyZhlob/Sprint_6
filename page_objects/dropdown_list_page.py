import allure
from page_objects.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locators.locators_dropdown_list import LocatorsDropDownListPage


class DropDownListPage(BasePage):
    @allure.step("Click search button")
    def click_search_button(self, locator):
        self.driver.find_element(*LocatorsDropDownListPage.COOKIES_CONFIRMATION).click()
        wait = WebDriverWait(self.driver, 10)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", self.driver.find_element(*locator))
        wait.until(EC.presence_of_element_located(locator))
        self.wait_for_element_visibility_click(locator, timeout=10)
