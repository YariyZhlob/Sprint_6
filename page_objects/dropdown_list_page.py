import allure
from page_objects.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locators.locators_dropdown_list import LocatorsDropDownListPage


# class TupplesOfLocators:
#     TUPPLES_OF_LOCATORS = (
#         (
#             (By.XPATH, "//div[@id='accordion__heading-0' and @class='accordion__button']"),
#             (By.XPATH, '//div[@id="accordion__panel-0"]/p[text()]'),
#             ("Сутки — 400 рублей. Оплата курьеру — наличными или картой.")
#         ),
#                        (
#                         (By.XPATH, "//div[@id='accordion__heading-1' and @class='accordion__button']"),
#                         (By.XPATH, '//div[@id="accordion__panel-1"]/p[text()]'),
#                         ("Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.")
#                        ),
#         (
#             (By.XPATH, "//div[@id='accordion__heading-2' and @class='accordion__button']"),
#             (By.XPATH, '//div[@id="accordion__panel-2"]/p[text()]'),
#             ("Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.")
#         ),
#         (
#             (By.XPATH, "//div[@id='accordion__heading-3' and @class='accordion__button']"),
#             (By.XPATH, '//div[@id="accordion__panel-3"]/p[text()]'),
#             ("Только начиная с завтрашнего дня. Но скоро станем расторопнее.")
#         ),
#         (
#             (By.XPATH, "//div[@id='accordion__heading-4' and @class='accordion__button']"),
#             (By.XPATH, '//div[@id="accordion__panel-4"]/p[text()]'),
#             ("Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.")
#         ),
#         (
#             (By.XPATH, "//div[@id='accordion__heading-5' and @class='accordion__button']"),
#             (By.XPATH, '//div[@id="accordion__panel-5"]/p[text()]'),
#             ("Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.")
#         ),
#         (
#             (By.XPATH, "//div[@id='accordion__heading-6' and @class='accordion__button']"),
#             (By.XPATH, '//div[@id="accordion__panel-6"]/p[text()]'),
#             ("Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.")
#         ),
#         (
#             (By.XPATH, "//div[@id='accordion__heading-7' and @class='accordion__button']"),
#             (By.XPATH, '//div[@id="accordion__panel-7"]/p[text()]'),
#             ("Да, обязательно. Всем самокатов! И Москве, и Московской области.")
#         )
#     )
#
#
# class LocatorsDropDownListPage:
#     # Кнопка согласия с куками
#     COOKIES_CONFIRMATION = (By.XPATH, '//button[@id="rcc-confirm-button"]')



class DropDownListPage(BasePage):
    @allure.step("Click search button")
    def click_search_button(self, locator):
        self.driver.find_element(*LocatorsDropDownListPage.COOKIES_CONFIRMATION).click()
        wait = WebDriverWait(self.driver, 10)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", self.driver.find_element(*locator))
        wait.until(EC.presence_of_element_located(locator))
        self.wait_for_element_visibility_click(locator, timeout=10)
