from selenium.webdriver.common.by import By


class YaPageLocators:
    PRICE_ARROW = (By.XPATH, "//div[@id='accordion__heading-0' and @class='accordion__button']")
    ARRAY_OF_TUPLES = [(By.XPATH, f'//div[@id="accordion__panel-{i}"]/p[text()]') for i in range(8)]
    #Кнопка Заказать сверху справа на странице
    TOP_ORDER_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g']")
    #Локатор поля Имя
    FIELD_NAME = (By.XPATH, '//input[@placeholder="* Имя"]')
    #Локатор поля Фамилия
    FIELD_SURNAME = (By.XPATH, '//input[@placeholder="* Фамилия"]')
    #Локатор поля Адрес
    FIELD_ADDRESS = (By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]')
    #Локатор поля Станция метро
    FIELD_METRO = (By.XPATH, '//input[@placeholder="* Станция метро"]')
    #Поле со списокм станций метро
    STATIONS_LIST = (By.XPATH, "//div[@class='select-search__select']")
    #Поле метро Черкизовская
    # CHERKIZOVO_METRO = (By.XPATH, "//div[@class='Order_Text__2broi' and text()='Черкизовская']")
    CHERKIZOVO_METRO = (By.XPATH, '//li[@class="select-search__row" and @data-index="1"]')
    #Локатор поля Телефон
    FIELD_TELEPHONE = (By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]')

# print(*YaPageLocators.ARRAY_OF_TUPLES[1])