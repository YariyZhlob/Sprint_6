import allure
from page_objects.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from constants import ConstantPhrases, ConstantUrl, ConstantsScenarioOne, ConstantsScenarioTwo
from locators.locators_scenario_one import LocatorsScenarioOne
from locators.locators_scenario_two import LocatorsScenarioTwo
from conftest import driver
from selenium.webdriver.common.by import By


class OrderScooterPage(BasePage):
    @allure.step("test order scooter scenario one")
    def order_scooter_scenario_one(self, name, surname, address, phone):
        # Клик по кнопке Заказать сверху справа на странице
        self.driver.find_element(*LocatorsScenarioOne.TOP_ORDER_BUTTON).click()
        # Ввод значения в поле Имя
        self.field_filling(LocatorsScenarioOne.FIELD_NAME, name)
        # Ввод значения в поле Фамилия
        self.field_filling(LocatorsScenarioOne.FIELD_SURNAME, surname)
        # Ввод значения в поле Адрес
        self.field_filling(LocatorsScenarioOne.FIELD_ADDRESS, address)
        # Клик по полю Станция метро
        self.driver.find_element(*LocatorsScenarioOne.FIELD_METRO).click()
        # Выбор метро Черкизово
        self.driver.find_element(*LocatorsScenarioOne.CHERKIZOVO_METRO).click()
        # Ввод значения в поле Телефон
        self.field_filling(LocatorsScenarioOne.FIELD_TELEPHONE, phone)
        # Клик по кнопке согласия с куками
        self.driver.find_element(*LocatorsScenarioOne.COOKIES_CONFIRMATION).click()
        # Клик по кнопке Далее
        self.driver.find_element(*LocatorsScenarioOne.ONWARDS_BUTTON).click()
        # ожидание загрузки страницы
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(LocatorsScenarioOne.BLACK_PEARL))
        #Клик по полю когда привезти самокат
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
        self.field_filling(LocatorsScenarioOne.COMMENT_FIELD, ConstantPhrases.COURIER_COMMENT)
        # Клик по кнопке подтверждения заказа
        self.driver.find_element(*LocatorsScenarioOne.CONFIRMATION_ORDER_BUTTON).click()
        # Клик по кнопке Да
        self.driver.find_element(*LocatorsScenarioOne.YES_BUTTON).click()


class OrderScooterPageScenarioTwo(BasePage):
    @allure.step("test order scooter scenario two")
    def order_scooter_scenario_two(self, name, surname, address, phone):
        # Клик по кнопке Заказать в середине страницы
        self.driver.find_element(*LocatorsScenarioTwo.SECOND_ORDER_BUTTON).click()
        # Ввод значения в поле Имя
        self.field_filling(LocatorsScenarioTwo.FIELD_NAME, name)
        # Ввод значения в поле Фамилия
        self.field_filling(LocatorsScenarioTwo.FIELD_SURNAME, surname)
        # Ввод значения в поле Адрес
        self.field_filling(LocatorsScenarioTwo.FIELD_ADDRESS, address)
        # Клик по полю Станция метро
        self.driver.find_element(*LocatorsScenarioTwo.FIELD_METRO).click()
        # Выбор метро Академичечкая
        self.driver.find_element(*LocatorsScenarioTwo.AKADEMKA_METRO).click()
        # Ввод значения в поле Телефон
        self.field_filling(LocatorsScenarioTwo.FIELD_TELEPHONE, phone)
        # # Клик по кнопке согласия с куками
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
        self.field_filling(LocatorsScenarioTwo.COMMENT_FIELD, ConstantPhrases.COURIER_COMMENT_TWO)
        # Клик по кнопке подтверждения заказа
        self.driver.find_element(*LocatorsScenarioTwo.CONFIRMATION_ORDER_BUTTON).click()
        # Клик по кнопке Да
        self.driver.find_element(*LocatorsScenarioTwo.YES_BUTTON).click()


class PageFillingData(OrderScooterPage):
    @allure.step("Fulfill page with data")
    def page_fulfilling(self,
                        name=ConstantsScenarioOne.NAME, surname=ConstantsScenarioOne.SURNAME,
                        address=ConstantsScenarioOne.ADDRESS, phone=ConstantsScenarioOne.PHONE):
        self.go_to_site(ConstantUrl.QA_SCOOTER_URL)
        self.order_scooter_scenario_one(name, surname, address, phone)
        return self.wait_for_element_visibility(LocatorsScenarioOne.ORDER_IS_CONFIRMED).text


class PageFillingDataLogoYandex(OrderScooterPage):
    @allure.step("Fulfill page with data Logo Yandex")
    def page_fulfilling_logo_yandex(self,
                                    name=ConstantsScenarioOne.NAME, surname=ConstantsScenarioOne.SURNAME,
                                    address=ConstantsScenarioOne.ADDRESS, phone=ConstantsScenarioOne.PHONE):
        self.go_to_site(ConstantUrl.QA_SCOOTER_URL)
        self.order_scooter_scenario_one(name, surname, address, phone)
        self.wait_for_element_visibility_click(LocatorsScenarioOne.LOOK_STATUS_BUTTON)
        self.wait_for_element_visibility_click(LocatorsScenarioOne.YANDEX_LOGO)
        self.driver.switch_to.window(self.driver.window_handles[1])
        WebDriverWait(self.driver, 10).until(EC.staleness_of(self.driver.find_element(By.TAG_NAME, 'html')))
        WebDriverWait(self.driver, 10).until(EC.url_contains(ConstantUrl.DZEN_URL))
        return self.driver.current_url


class PageFillingDataLogoScooter(OrderScooterPage):
    @allure.step("Fulfill page with data Logo Scooter")
    def page_fulfilling_logo_scooter(self,
                                     name=ConstantsScenarioOne.NAME, surname=ConstantsScenarioOne.SURNAME,
                                     address=ConstantsScenarioOne.ADDRESS, phone=ConstantsScenarioOne.PHONE):
        self.go_to_site(ConstantUrl.QA_SCOOTER_URL)
        self.order_scooter_scenario_one(name, surname, address, phone)
        self.wait_for_element_visibility_click(LocatorsScenarioOne.LOOK_STATUS_BUTTON)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", self.driver.find_element(*LocatorsScenarioOne.SCOOTER_LOGO))
        # Клик по лого Самоката
        self.driver.find_element(*LocatorsScenarioOne.SCOOTER_LOGO).click()
        WebDriverWait(self.driver, 10).until(EC.url_contains(ConstantUrl.QA_SCOOTER_URL))
        return self.driver.current_url


class PageFillingDataScenarioTwo(OrderScooterPageScenarioTwo):
    @allure.step("Fulfill page with data Scenario Two")
    def page_fulfilling(self,
                        name=ConstantsScenarioTwo.NAME, surname=ConstantsScenarioTwo.SURNAME,
                        address=ConstantsScenarioTwo.ADDRESS, phone=ConstantsScenarioTwo.PHONE):
        self.go_to_site(ConstantUrl.QA_SCOOTER_URL)
        # Скроллинг до элемента
        self.driver.execute_script("arguments[0].scrollIntoView(true);",
                              self.driver.find_element(*LocatorsScenarioTwo.SECOND_ORDER_BUTTON))
        self.wait_for_element_visibility_click(LocatorsScenarioTwo.COOKIES_CONFIRMATION)
        self.order_scooter_scenario_two(name, surname, address, phone)
        return self.wait_for_element_visibility(LocatorsScenarioTwo.ORDER_IS_CONFIRMED).text


class PageFillingDataLogoYandexScenarioTwo(OrderScooterPageScenarioTwo):
    @allure.step("Fulfill page with data Logo Yandex Scenario Two")
    def page_fulfilling_logo_yandex(self, name=ConstantsScenarioTwo.NAME, surname=ConstantsScenarioTwo.SURNAME,
                        address=ConstantsScenarioTwo.ADDRESS, phone=ConstantsScenarioTwo.PHONE):
        self.go_to_site(ConstantUrl.QA_SCOOTER_URL)
        # Скроллинг до элемента
        self.driver.execute_script("arguments[0].scrollIntoView(true);",
                              self.driver.find_element(*LocatorsScenarioTwo.SECOND_ORDER_BUTTON))
        self.wait_for_element_visibility_click(LocatorsScenarioTwo.COOKIES_CONFIRMATION)
        self.order_scooter_scenario_two(name, surname, address, phone)
        self.wait_for_element_visibility_click(LocatorsScenarioTwo.LOOK_STATUS_BUTTON)
        self.wait_for_element_visibility_click(LocatorsScenarioTwo.YANDEX_LOGO)
        self.driver.switch_to.window(self.driver.window_handles[1])
        WebDriverWait(self.driver, 10).until(EC.staleness_of(self.driver.find_element(By.TAG_NAME, 'html')))
        WebDriverWait(self.driver, 10).until(EC.url_contains('https://dzen.ru/'))
        return self.driver.current_url


class PageFillingDataLogoScooterScenarioTwo(OrderScooterPageScenarioTwo):
    @allure.step("Fulfill page with data Logo Scooter Scenario Two")
    def page_fulfilling_logo_scooter(self):
        self.go_to_site(ConstantUrl.QA_SCOOTER_URL)
        # Скроллинг до элемента
        self.driver.execute_script("arguments[0].scrollIntoView(true);",
                              self.driver.find_element(*LocatorsScenarioTwo.SECOND_ORDER_BUTTON))
        self.wait_for_element_visibility_click(LocatorsScenarioTwo.COOKIES_CONFIRMATION)
        self.order_scooter_scenario_two(name="Дмитрий", surname="Менделеев",
                                      address="Пр. Химиков, д.10", phone="89999999999")
        self.wait_for_element_visibility_click(LocatorsScenarioTwo.LOOK_STATUS_BUTTON)
        # Клик по лого Самоката
        self.driver.find_element(*LocatorsScenarioTwo.SCOOTER_LOGO).click()
        return self.driver.current_url
