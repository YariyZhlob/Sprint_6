import time

from selenium.webdriver.common.by import By
from constants import Constants
from data.locators import YaPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestDropDownList:
    def test_how_much_it_costs(self, driver):
        driver.get(Constants.URL)
        wait = WebDriverWait(driver, 10)
        arrow = driver.find_element(*YaPageLocators.PRICE_ARROW)

        # print(*YaPageLocators.PRICE_ARROW)
        driver.execute_script("arguments[0].scrollIntoView(true);", arrow)
        element = wait.until(EC.visibility_of_element_located(YaPageLocators.PRICE_ARROW))
        time.sleep(3)
        element.click()

        necessary_text = driver.find_element(By.XPATH, '//div[@id="accordion__panel-0"]/p[text()]').text
        print(necessary_text)



