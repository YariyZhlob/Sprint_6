from page_objects.order_scooter_page_scenario_one import PageFillingData, PageFillingDataLogoYandex, PageFillingDataLogoScooter
from conftest import driver
import allure


class TestOrderScooter:
    @allure.title("Заказ с помощью кнопки Заказать сверху справа на странице сценарий один")
    def test_order_scooter_pom(self, driver):
        page_filler = PageFillingData(driver)
        assert "Заказ оформлен" in page_filler.page_fulfilling()

    @allure.title("Проверка открытия главной страницы Дзена при нажатии на логотип Яндекса сценарий один")
    def test_logo_yandex(self, driver):
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
