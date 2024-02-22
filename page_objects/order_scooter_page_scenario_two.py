import allure
from page_objects.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from constants import ConstantPhrases
from locators.locators_scenario_two import LocatorsScenarioTwo
# from selenium.webdriver.common.by import By
#
#
# class LocatorsScenarioTwo:
#     # Вторая кнопка Заказать
#     SECOND_ORDER_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']")
#     # Локатор поля Имя
#     FIELD_NAME = (By.XPATH, '//input[@placeholder="* Имя"]')
#     # Локатор поля Фамилия
#     FIELD_SURNAME = (By.XPATH, '//input[@placeholder="* Фамилия"]')
#     # Локатор поля Адрес
#     FIELD_ADDRESS = (By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]')
#     # Локатор поля Станция метро
#     FIELD_METRO = (By.XPATH, '//input[@placeholder="* Станция метро"]')
#     # Поле метро Академическая
#     AKADEMKA_METRO = (By.XPATH, '//li[@class="select-search__row" and @data-index="94"]')
#     # Локатор поля Телефон
#     FIELD_TELEPHONE = (By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]')
#     # Кнопка согласия с куками
#     COOKIES_CONFIRMATION = (By.XPATH, '//button[@id="rcc-confirm-button"]')
#     # Локатор кнопки Далее
#     ONWARDS_BUTTON = (By.XPATH, "//button[text()='Далее']")
#     # Локатор чекбокса Серая безысходность
#     GRAY_COLOR = (By.XPATH, "//input[@id='grey']")
#     # Поле когда привезти самокат
#     TIME_OF_DELIVERY = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
#     # выбор 25 числа
#     DESIRABLE_DATE_TWO = (By.XPATH, "//div[text()='25']")
#     # Поле срока аренды
#     RENTAL_FIELD = (By.XPATH, "//div[text()='* Срок аренды']")
#     # Выбор срока аренды 3 дня
#     RENTAL_TIME_TWO = (By.XPATH, "//div[@class='Dropdown-option' and text()='трое суток']")
#     # Выбор поля комментариев для курьера
#     COMMENT_FIELD = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
#     # Кнопка подтверждения заказа
#     CONFIRMATION_ORDER_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Заказать']")
#     # Кнопка Да
#     YES_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Да']")
#     # Заказ оформлен
#     ORDER_IS_CONFIRMED = (By.XPATH, "//div[@class='Order_ModalHeader__3FDaJ']")
#     # Кнопка посмотреть статус
#     LOOK_STATUS_BUTTON = (By.XPATH, "//button[text()='Посмотреть статус']")
#     # Лого Яндекса
#     YANDEX_LOGO = (By.XPATH, "//img[@alt='Yandex']")
#     # Лого Самоката
#     SCOOTER_LOGO = (By.XPATH, "//img[@alt='Scooter']")


class OrderScooterPageScenarioTwo(BasePage):
    @allure.step("test order scooter scenario two")
    def order_scooter_scenario_two(self, name, surname, address, phone):
        # Клик по кнопке Заказать в середине страницы
        self.driver.find_element(*LocatorsScenarioTwo.SECOND_ORDER_BUTTON).click()
        # Ввод значения в поле Имя
        self.driver.find_element(*LocatorsScenarioTwo.FIELD_NAME).send_keys(name)  # )("Дмитрий")
        # Ввод значения в поле Фамилия
        self.driver.find_element(*LocatorsScenarioTwo.FIELD_SURNAME).send_keys(surname)  # ("Менделеев")
        # Ввод значения в поле Адрес
        self.driver.find_element(*LocatorsScenarioTwo.FIELD_ADDRESS).send_keys(address)  # ("Пр. Химиков, д.10")
        # Клик по полю Станция метро
        self.driver.find_element(*LocatorsScenarioTwo.FIELD_METRO).click()
        # Выбор метро Академичечкая
        self.driver.find_element(*LocatorsScenarioTwo.AKADEMKA_METRO).click()
        # Ввод значения в поле Телефон
        self.driver.find_element(*LocatorsScenarioTwo.FIELD_TELEPHONE).send_keys(phone)  # ("89999999999")
        # # Клик по кнопке согласия с куками
        # self.driver.find_element(*LocatorsScenarioTwo.COOKIES_CONFIRMATION).click()
        # Клик по кнопке Далее
        self.driver.find_element(*LocatorsScenarioTwo.ONWARDS_BUTTON).click()
        # ожидание загрузки страницы
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(LocatorsScenarioTwo.GRAY_COLOR))
        # Клик по полю когда привезти самокат
        self.driver.find_element(*LocatorsScenarioTwo.TIME_OF_DELIVERY).click()
        # Клик по 25 числу
        self.driver.find_element(*LocatorsScenarioTwo.DESIRABLE_DATE_TWO).click()
        # Клик по полю срока аренды
        self.driver.find_element(*LocatorsScenarioTwo.RENTAL_FIELD).click()
        # Клик по количеству дней аренды
        self.driver.find_element(*LocatorsScenarioTwo.RENTAL_TIME_TWO).click()
        # Клик по чекбоксу серая безысходность
        self.driver.find_element(*LocatorsScenarioTwo.GRAY_COLOR).click()
        # Клик по полю комментариев для курьера
        self.driver.find_element(*LocatorsScenarioTwo.COMMENT_FIELD).send_keys(ConstantPhrases.COURIER_COMMENT_TWO)
        # Клик по кнопке подтверждения заказа
        self.driver.find_element(*LocatorsScenarioTwo.CONFIRMATION_ORDER_BUTTON).click()
        # Клик по кнопке Да
        self.driver.find_element(*LocatorsScenarioTwo.YES_BUTTON).click()
