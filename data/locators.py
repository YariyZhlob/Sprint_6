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
    #Локатор кнопки Далее
    ONWARDS_BUTTON = (By.XPATH, "//button[text()='Далее']")
    #Локатор чекбокса Черный жемчуг
    BLACK_PEARL = (By.XPATH, "//input[@id='black']")
    #Кнопка согласия с куками
    COOKIES_CONFIRMATION = (By.XPATH, '//button[@id="rcc-confirm-button"]')
    #Поле когда привезти самокат
    TIME_OF_DELIVERY = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    #выбор 23 числа
    DESIRABLE_DATE = (By.XPATH, "//div[text()='23']")
    #Поле срока аренды
    RENTAL_FIELD = (By.XPATH, "//div[text()='* Срок аренды']")
    #Выбор срока аренды 2 дня
    RENTAL_TIME = (By.XPATH, "//div[@class='Dropdown-option' and text()='двое суток']")
    #Выбор поля комментариев для курьера
    COMMENT_FIELD = (By.XPATH,"//input[@placeholder='Комментарий для курьера']")
    #Кнопка подтверждения заказа
    CONFIRMATION_ORDER_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Заказать']")
    #Кнопка Да
    YES_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Да']")
    #Заказ оформлен
    ORDER_IS_CONFIRMED = (By.XPATH, "//div[@class='Order_ModalHeader__3FDaJ']")
    #Лого Яндекса
    YANDEX_LOGO = (By.XPATH, "//img[@alt='Yandex']")
    #Кнопка посмотреть статус
    LOOK_STATUS_BUTTON = (By.XPATH, "//button[text()='Посмотреть статус']")
    #Надпись Новости на Дзене
    # DZEN_NEWS = (By.XPATH, "//div[@data-testid='floor-title-text' and text()='Новости']")
    DZEN_NEWS = (By.XPATH, "//form[@role='search']")
    #Лого Самоката
    SCOOTER_LOGO = (By.XPATH, "//img[@alt='Scooter']")
    #Вторая кнопка Заказать
    SECOND_ORDER_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']")
    #Поле метро Академическая
    AKADEMKA_METRO = (By.XPATH, '//li[@class="select-search__row" and @data-index="94"]')
    #выбор 25 числа
    DESIRABLE_DATE_TWO = (By.XPATH, "//div[text()='25']")
    #Выбор срока аренды 3 дня
    RENTAL_TIME_TWO = (By.XPATH, "//div[@class='Dropdown-option' and text()='трое суток']")
    #Локатор чекбокса Серая безысходность
    GRAY_COLOR = (By.XPATH, "//input[@id='grey']")


# print(*YaPageLocators.ARRAY_OF_TUPLES[1])