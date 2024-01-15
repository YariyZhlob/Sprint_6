import time

from selenium.webdriver.common.by import By
from constants import Constants
from data.locators import YaPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestOrderScooter:
    def test_positive_scenario_one(self, driver):
        driver.get(Constants.URL)
        #Клик по кнопке Заказать сверху справа на странице
        driver.find_element(*YaPageLocators.TOP_ORDER_BUTTON).click()
        #Ввод значения в поле Имя
        driver.find_element(*YaPageLocators.FIELD_NAME).send_keys("Афанасий")
        #Ввод значения в поле Фамилия
        driver.find_element(*YaPageLocators.FIELD_SURNAME).send_keys("Никитин")
        #Ввод значения в поле Адрес
        driver.find_element(*YaPageLocators.FIELD_ADDRESS).send_keys("Ботаническая, д.8")
        #Клик по полю Станция метро
        driver.find_element(*YaPageLocators.FIELD_METRO).click()
        #Выбор метро Черкизово
        driver.find_element(*YaPageLocators.CHERKIZOVO_METRO).click()
        # Ввод значения в поле Телефон
        driver.find_element(*YaPageLocators.FIELD_TELEPHONE).send_keys("88888888888")







