import pytest
from constants import Constants
from page_objects.dropdown_list_page import DropDownListPage, TupplesOfLocators
import allure
from conftest import driver


class TestDropDownList:
    @pytest.mark.parametrize("arrow_locator, locator, desirable_text", [
        *TupplesOfLocators.TUPPLES_OF_LOCATORS])
    @allure.title('Сравнение текста в Вопросах о важном')
    def test_how_much_it_costs(self, driver, arrow_locator, locator, desirable_text):
        page = DropDownListPage(driver)
        page.go_to_site(Constants.URL)
        page.click_search_button(arrow_locator)
        assert page.wait_for_element_visibility(locator, 10).text == desirable_text
