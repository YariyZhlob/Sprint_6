import allure
from page_objects.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from constants import Constants
from selenium.webdriver.common.by import By


class LocatorsScenarioOne:
    # Кнопка Заказать сверху справа на странице
    TOP_ORDER_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g']")
    # Локатор поля Имя
    FIELD_NAME = (By.XPATH, '//input[@placeholder="* Имя"]')
    # Локатор поля Фамилия
    FIELD_SURNAME = (By.XPATH, '//input[@placeholder="* Фамилия"]')
    # Локатор поля Адрес
    FIELD_ADDRESS = (By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]')
    # Локатор поля Станция метро
    FIELD_METRO = (By.XPATH, '//input[@placeholder="* Станция метро"]')
    # Поле метро Черкизовская
    CHERKIZOVO_METRO = (By.XPATH, '//li[@class="select-search__row" and @data-index="1"]')
    # Локатор поля Телефон
    FIELD_TELEPHONE = (By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]')
    # Кнопка согласия с куками
    COOKIES_CONFIRMATION = (By.XPATH, '//button[@id="rcc-confirm-button"]')
    # Локатор кнопки Далее
    ONWARDS_BUTTON = (By.XPATH, "//button[text()='Далее']")
    # Локатор чекбокса Черный жемчуг
    BLACK_PEARL = (By.XPATH, "//input[@id='black']")
    # Поле когда привезти самокат
    TIME_OF_DELIVERY = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    # выбор 23 числа
    DESIRABLE_DATE = (By.XPATH, "//div[text()='23']")
    # Поле срока аренды
    RENTAL_FIELD = (By.XPATH, "//div[text()='* Срок аренды']")
    # Выбор срока аренды 2 дня
    RENTAL_TIME = (By.XPATH, "//div[@class='Dropdown-option' and text()='двое суток']")
    # Выбор поля комментариев для курьера
    COMMENT_FIELD = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    # Кнопка подтверждения заказа
    CONFIRMATION_ORDER_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Заказать']")
    # Кнопка Да
    YES_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Да']")
    # Заказ оформлен
    ORDER_IS_CONFIRMED = (By.XPATH, "//div[@class='Order_ModalHeader__3FDaJ']")
    # Кнопка посмотреть статус
    LOOK_STATUS_BUTTON = (By.XPATH, "//button[text()='Посмотреть статус']")
    # Лого Яндекса
    YANDEX_LOGO = (By.XPATH, "//img[@alt='Yandex']")
    # Лого Самоката
    SCOOTER_LOGO = (By.XPATH, "//img[@alt='Scooter']")



class OrderScooterPage(BasePage):
    @allure.step("test order scooter scenario one")
    def order_scooter_scenario_one(self, name, surname, address, phone):
        # Клик по кнопке Заказать сверху справа на странице
        self.driver.find_element(*LocatorsScenarioOne.TOP_ORDER_BUTTON).click()
        # self.driver.find_element(*LocatorsScenarioOne.TOP_ORDER_BUTTON).click()
        # Ввод значения в поле Имя
        self.driver.find_element(*LocatorsScenarioOne.FIELD_NAME).send_keys(name) #)("Афанасий")
        # Ввод значения в поле Фамилия
        self.driver.find_element(*LocatorsScenarioOne.FIELD_SURNAME).send_keys(surname)#("Никитин")
        # Ввод значения в поле Адрес
        self.driver.find_element(*LocatorsScenarioOne.FIELD_ADDRESS).send_keys(address)#("Ботаническая, д.8")
        # Клик по полю Станция метро
        self.driver.find_element(*LocatorsScenarioOne.FIELD_METRO).click()
        # Выбор метро Черкизово
        self.driver.find_element(*LocatorsScenarioOne.CHERKIZOVO_METRO).click()
        # Ввод значения в поле Телефон
        self.driver.find_element(*LocatorsScenarioOne.FIELD_TELEPHONE).send_keys(phone)#("88888888888")
        # Клик по кнопке согласия с куками
        self.driver.find_element(*LocatorsScenarioOne.COOKIES_CONFIRMATION).click()
        # Клик по кнопке Далее
        self.driver.find_element(*LocatorsScenarioOne.ONWARDS_BUTTON).click()
        # ожидание загрузки страницы
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(LocatorsScenarioOne.BLACK_PEARL))
        # Клик по полю когда привезти самокат
        self.driver.find_element(*LocatorsScenarioOne.TIME_OF_DELIVERY).click()
        # Клик по 23 числу
        self.driver.find_element(*LocatorsScenarioOne.DESIRABLE_DATE).click()
        # Клик по полю срока аренды
        self.driver.find_element(*LocatorsScenarioOne.RENTAL_FIELD).click()
        # Клик по количеству дней аренды
        self.driver.find_element(*LocatorsScenarioOne.RENTAL_TIME).click()
        # Клик по чекбоксу черный жемчуг
        self.driver.find_element(*LocatorsScenarioOne.BLACK_PEARL).click()
        # Клик по полю комментариев для курьера
        self.driver.find_element(*LocatorsScenarioOne.COMMENT_FIELD).send_keys(Constants.COURIER_COMMENT)
        # Клик по кнопке подтверждения заказа
        self.driver.find_element(*LocatorsScenarioOne.CONFIRMATION_ORDER_BUTTON).click()
        # Клик по кнопке Да
        # time.sleep(15)
        self.driver.find_element(*LocatorsScenarioOne.YES_BUTTON).click()
