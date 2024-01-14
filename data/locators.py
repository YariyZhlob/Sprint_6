from selenium.webdriver.common.by import By


class YaPageLocators:
    PRICE_ARROW = (By.XPATH, "//div[@id='accordion__heading-0' and @class='accordion__button']")
    ARRAY_OF_TUPLES = [(By.XPATH, f'//div[@id="accordion__panel-{i}"]/p[text()]') for i in range(8)]

# print(*YaPageLocators.ARRAY_OF_TUPLES[1])