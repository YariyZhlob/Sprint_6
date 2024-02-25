from page_objects.order_scooter_page import PageFillingData, PageFillingDataLogoYandex, PageFillingDataLogoScooter
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
        current_url = PageFillingDataLogoScooter(driver)
        assert "qa-scooter.praktikum-services.ru" in current_url.page_fulfilling_logo_scooter()
