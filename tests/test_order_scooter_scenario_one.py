from selenium.webdriver.common.by import By
from constants import ConstantUrl
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_objects.order_scooter_page_scenario_one import OrderScooterPage, LocatorsScenarioOne, PageFillingData, PageFillingDataLogoYandex, PageFillingDataLogoScooter, PageFillingDataScenarioTwo
from conftest import driver
import allure


class TestOrderScooter:
    @allure.title("Заказ с помощью кнопки Заказать сверху справа на странице сценарий один")
    def test_order_scooter_pom(self, driver):  #, driver):
        # order_page = OrderScooterPage(driver)
        # order_page.go_to_site(ConstantUrl.URL)
        # order_page.order_scooter_scenario_one(name="Афанасий", surname="Никитин",
        #                               address="Ботаническая, д.8", phone="88888888888")

        # Проверка успешного создания заказа
        # assert "Заказ оформлен" in order_page.wait_for_element_visibility(LocatorsScenarioOne.ORDER_IS_CONFIRMED).text
        # print(order_page.wait_for_element_visibility(LocatorsScenarioOne.ORDER_IS_CONFIRMED).text)
        # assert "Заказ оформлен" in PageFillingData.page_fulfilling
        # print(PageFillingData.page_fulfilling)
        page_filler = PageFillingData(driver)
        assert "Заказ оформлен" in page_filler.page_fulfilling()
        # print(result)

    @allure.title("Проверка открытия главной страницы Дзена при нажатии на логотип Яндекса сценарий один")
    def test_logo_yandex(self, driver):
        # order_page = OrderScooterPage(driver)
        # order_page.go_to_site(ConstantUrl.QA_SCOOTER_URL)
        # order_page.order_scooter_scenario_one(name="Афанасий", surname="Никитин",
        #                               address="Ботаническая, д.8", phone="88888888888")
        # order_page.wait_for_element_visibility_click(LocatorsScenarioOne.LOOK_STATUS_BUTTON)
        # order_page.wait_for_element_visibility_click(LocatorsScenarioOne.YANDEX_LOGO)
        # driver.switch_to.window(driver.window_handles[1])
        # WebDriverWait(driver, 10).until(EC.staleness_of(driver.find_element(By.TAG_NAME, 'html')))
        # WebDriverWait(driver, 10).until(EC.url_contains(ConstantUrl.DZEN_URL))
        # assert "dzen.ru" in driver.current_url
        current_url = PageFillingDataLogoYandex(driver)
        assert "dzen.ru" in current_url.page_fulfilling_logo_yandex()



    @allure.title("Проверка попадания на главную страницу при нажатии логотип Самоката сценарий один")
    def test_logo_scooter(self, driver):
        # order_page = OrderScooterPage(driver)
        # order_page.go_to_site(ConstantUrl.QA_SCOOTER_URL)
        # order_page.order_scooter_scenario_one(name="Афанасий", surname="Никитин",
        #                               address="Ботаническая, д.8", phone="88888888888")
        # order_page.wait_for_element_visibility_click(LocatorsScenarioOne.LOOK_STATUS_BUTTON)
        # driver.execute_script("arguments[0].scrollIntoView(true);", driver.find_element(*LocatorsScenarioOne.SCOOTER_LOGO))
        # # Клик по лого Самоката
        # driver.find_element(*LocatorsScenarioOne.SCOOTER_LOGO).click()
        # WebDriverWait(driver, 10).until(EC.url_contains(ConstantUrl.QA_SCOOTER_URL))
        # assert "qa-scooter.praktikum-services.ru" in driver.current_url
        current_url = PageFillingDataLogoScooter(driver)
        assert "qa-scooter.praktikum-services.ru" in current_url.page_fulfilling_logo_scooter()
