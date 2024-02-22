from selenium.webdriver.common.by import By
from constants import ConstantUrl
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from page_objects.order_scooter_page_scenario_two import OrderScooterPageScenarioTwo, LocatorsScenarioTwo
from page_objects.order_scooter_page_scenario_one import OrderScooterPageScenarioTwo, LocatorsScenarioTwo
from conftest import driver
import allure


class TestOrderScooterScenarioTwo:
    @allure.title("Заказ с помощью кнопки Заказать сверху справа на странице сценарий два")
    def test_order_scooter_scenario_two(self, driver):
        order_page = OrderScooterPageScenarioTwo(driver)
        order_page.go_to_site(ConstantUrl.URL)
        # Скроллинг до элемента
        driver.execute_script("arguments[0].scrollIntoView(true);",
                              driver.find_element(*LocatorsScenarioTwo.SECOND_ORDER_BUTTON))
        order_page.wait_for_element_visibility_click(LocatorsScenarioTwo.COOKIES_CONFIRMATION)
        order_page.order_scooter_scenario_two(name="Дмитрий", surname="Менделеев",
                                      address="Пр. Химиков, д.10", phone="89999999999")

        assert "Заказ оформлен" in order_page.wait_for_element_visibility(LocatorsScenarioTwo.ORDER_IS_CONFIRMED).text

    @allure.title("Проверка открытия главной страницы Дзена при нажатии на логотип Яндекса сценарий два")
    def test_logo_yandex_scenario_two(self, driver):
        order_page = OrderScooterPageScenarioTwo(driver)
        order_page.go_to_site(ConstantUrl.URL)
        # Скроллинг до элемента
        driver.execute_script("arguments[0].scrollIntoView(true);",
                              driver.find_element(*LocatorsScenarioTwo.SECOND_ORDER_BUTTON))
        order_page.wait_for_element_visibility_click(LocatorsScenarioTwo.COOKIES_CONFIRMATION)
        order_page.order_scooter_scenario_two(name="Дмитрий", surname="Менделеев",
                                      address="Пр. Химиков, д.10", phone="89999999999")
        order_page.wait_for_element_visibility_click(LocatorsScenarioTwo.LOOK_STATUS_BUTTON)
        order_page.wait_for_element_visibility_click(LocatorsScenarioTwo.YANDEX_LOGO)
        driver.switch_to.window(driver.window_handles[1])
        WebDriverWait(driver, 10).until(EC.staleness_of(driver.find_element(By.TAG_NAME, 'html')))
        WebDriverWait(driver, 10).until(EC.url_contains('https://dzen.ru/'))
        assert "dzen.ru" in driver.current_url

    @allure.title("Проверка попадания на главную страницу при нажатии логотип Самоката сценарий два")
    def test_logo_scooter_scenario_two(self, driver):
        order_page = OrderScooterPageScenarioTwo(driver)
        order_page.go_to_site(ConstantUrl.URL)
        # Скроллинг до элемента
        driver.execute_script("arguments[0].scrollIntoView(true);",
                              driver.find_element(*LocatorsScenarioTwo.SECOND_ORDER_BUTTON))
        order_page.wait_for_element_visibility_click(LocatorsScenarioTwo.COOKIES_CONFIRMATION)
        order_page.order_scooter_scenario_two(name="Дмитрий", surname="Менделеев",
                                      address="Пр. Химиков, д.10", phone="89999999999")
        order_page.wait_for_element_visibility_click(LocatorsScenarioTwo.LOOK_STATUS_BUTTON)
        # Клик по лого Самоката
        driver.find_element(*LocatorsScenarioTwo.SCOOTER_LOGO).click()
        # Проверка перехода на страницу Самоката
        assert "qa-scooter.praktikum-services.ru" in driver.current_url

