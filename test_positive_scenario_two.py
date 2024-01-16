import time

from selenium.webdriver.common.by import By
from constants import Constants
from data.locators import YaPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestOrderScooterScenarioTwo:
    def test_create_order_two(self, driver):
        driver.get(Constants.URL)
        #Клик по кнопке Заказать в середине страницы
        driver.find_element(*YaPageLocators.SECOND_ORDER_BUTTON).click()
        #Ввод значения в поле Имя
        driver.find_element(*YaPageLocators.FIELD_NAME).send_keys("Дмитрий")
        #Ввод значения в поле Фамилия
        driver.find_element(*YaPageLocators.FIELD_SURNAME).send_keys("Менделеев")
        #Ввод значения в поле Адрес
        driver.find_element(*YaPageLocators.FIELD_ADDRESS).send_keys("Пр. Химиков, д.10")
        #Клик по полю Станция метро
        driver.find_element(*YaPageLocators.FIELD_METRO).click()
        #Выбор метро Академичечкая
        driver.find_element(*YaPageLocators.AKADEMKA_METRO).click()
        #Ввод значения в поле Телефон
        driver.find_element(*YaPageLocators.FIELD_TELEPHONE).send_keys("89999999999")
        #Клик по кнопке согласия с куками
        driver.find_element(*YaPageLocators.COOKIES_CONFIRMATION).click()
        #Клик по кнопке Далее
        driver.find_element(*YaPageLocators.ONWARDS_BUTTON).click()
        #ожидание загрузки страницы
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((YaPageLocators.BLACK_PEARL)))
        #Клик по полю когда привезти самокат
        driver.find_element(*YaPageLocators.TIME_OF_DELIVERY).click()
        #Клик по 25 числу
        driver.find_element(*YaPageLocators.DESIRABLE_DATE_TWO).click()
        #Клик по полю срока аренды
        driver.find_element(*YaPageLocators.RENTAL_FIELD).click()
        #Клик по количеству дней аренды
        driver.find_element(*YaPageLocators.RENTAL_TIME_TWO).click()
        #Клик по чекбоксу серая безысходность
        driver.find_element(*YaPageLocators.GRAY_COLOR).click()
        #Клик по полю комментариев для курьера
        driver.find_element(*YaPageLocators.COMMENT_FIELD).send_keys(Constants.COURIER_COMMENT)
        #Клик по кнопке подтверждения заказа
        driver.find_element(*YaPageLocators.CONFIRMATION_ORDER_BUTTON).click()
        #Клик по кнопке Да
        driver.find_element(*YaPageLocators.YES_BUTTON).click()
        #Проверка успешного создания заказа
        # assert "Заказ оформлен" in driver.find_element(*YaPageLocators.ORDER_IS_CONFIRMED).text
        # #Клик по кнопке посмотреть статус
        # driver.find_element(*YaPageLocators.LOOK_STATUS_BUTTON).click()
        # #Клик по лого Яндекса
        # driver.find_element(*YaPageLocators.YANDEX_LOGO).click()
        #
        # # WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
        #
        # driver.switch_to.window(driver.window_handles[1])
        # WebDriverWait(driver, 10).until(EC.staleness_of(driver.find_element(By.TAG_NAME, 'html')))
        # # Запоминаем идентификаторы текущих вкладок
        # # main_window_handle = driver.current_window_handle
        # # new_window_handle = [handle for handle in driver.window_handles if handle != main_window_handle][0]
        # #
        # # # Переключение на новую вкладку
        # # driver.switch_to.window(new_window_handle)
        #
        # WebDriverWait(driver, 10).until(EC.url_contains("dzen.ru"))
        # time.sleep(5)
        #
        # # element = wait.until(EC.presence_of_element_located((By.XPATH, "//form[@role='search']")))
        # # print(driver.current_url)
        #
        # assert "dzen.ru" in driver.current_url

    def test_logo_yandex_two(self, driver):
        self.test_create_order_two(driver)
        # Клик по кнопке посмотреть статус
        driver.find_element(*YaPageLocators.LOOK_STATUS_BUTTON).click()
        # Клик по лого Яндекса
        driver.find_element(*YaPageLocators.YANDEX_LOGO).click()

        # WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))

        driver.switch_to.window(driver.window_handles[1])
        WebDriverWait(driver, 10).until(EC.staleness_of(driver.find_element(By.TAG_NAME, 'html')))
        # Запоминаем идентификаторы текущих вкладок
        # main_window_handle = driver.current_window_handle
        # new_window_handle = [handle for handle in driver.window_handles if handle != main_window_handle][0]
        #
        # # Переключение на новую вкладку
        # driver.switch_to.window(new_window_handle)

        WebDriverWait(driver, 10).until(EC.url_contains("dzen.ru"))
        time.sleep(5)

        # element = wait.until(EC.presence_of_element_located((By.XPATH, "//form[@role='search']")))
        #print(driver.current_url)
        #Проверка перехода на страницу Дзена
        assert "dzen.ru" in driver.current_url

    def test_logo_scooter_two(self, driver):
        self.test_create_order_two(driver)
        #Клик по кнопке посмотреть статус
        driver.find_element(*YaPageLocators.LOOK_STATUS_BUTTON).click()
        time.sleep(5)
        #Клик по лого Самоката
        driver.find_element(*YaPageLocators.SCOOTER_LOGO).click()
        #Проверка перехода на страницу Самоката
        assert "qa-scooter.praktikum-services.ru" in driver.current_url
