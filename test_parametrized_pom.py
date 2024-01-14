import time
import pytest
from selenium.webdriver.common.by import By
from constants import Constants
from data.locators import YaPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestDropDownList:
    @pytest.mark.parametrize("arrow_locator, locator, desirable_text", [
        # ('//div[@id="accordion__panel-0"]/p[text()]', "Сутки — 400 рублей. Оплата курьеру — наличными или картой.")
        *Constants.ARRAY_OF_TUPLES
    ])
    def test_how_much_it_costs(self, driver, arrow_locator, locator, desirable_text):
        driver.get(Constants.URL)
        wait = WebDriverWait(driver, 10)
        # arrow = driver.find_element(*YaPageLocators.PRICE_ARROW)
        arrow = driver.find_element(By.XPATH, arrow_locator)

        # print(*YaPageLocators.PRICE_ARROW)
        driver.execute_script("arguments[0].scrollIntoView(true);", arrow)
        # element = wait.until(EC.visibility_of_element_located(YaPageLocators.PRICE_ARROW))
        element = wait.until(EC.visibility_of_element_located((By.XPATH, arrow_locator)))
        time.sleep(3)
        element.click()
        print(driver.find_element(By.XPATH, locator).text)

        assert driver.find_element(By.XPATH, locator).text == desirable_text

