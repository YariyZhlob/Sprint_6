from page_objects.order_scooter_page import PageFillingDataLogoScooterScenarioTwo, PageFillingDataScenarioTwo, PageFillingDataLogoYandexScenarioTwo
from conftest import driver
import allure


class TestOrderScooterScenarioTwo:
    @allure.title("Заказ с помощью кнопки Заказать сверху справа на странице сценарий два")
    def test_order_scooter_scenario_two(self, driver):
        page_filler = PageFillingDataScenarioTwo(driver)
        assert "Заказ оформлен" in page_filler.page_fulfilling()

    @allure.title("Проверка открытия главной страницы Дзена при нажатии на логотип Яндекса сценарий два")
    def test_logo_yandex_scenario_two(self, driver):
        current_url = PageFillingDataLogoYandexScenarioTwo(driver)
        assert "dzen.ru" in current_url.page_fulfilling_logo_yandex()

    @allure.title("Проверка попадания на главную страницу при нажатии логотип Самоката сценарий два")
    def test_logo_scooter_scenario_two(self, driver):
        current_url = PageFillingDataLogoScooterScenarioTwo(driver)
        assert "qa-scooter.praktikum-services.ru" in current_url.page_fulfilling_logo_scooter()

