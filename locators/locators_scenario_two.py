from selenium.webdriver.common.by import By


class LocatorsScenarioTwo:
    # Вторая кнопка Заказать
    SECOND_ORDER_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']")
    # Локатор поля Имя
    FIELD_NAME = (By.XPATH, '//input[@placeholder="* Имя"]')
    # Локатор поля Фамилия
    FIELD_SURNAME = (By.XPATH, '//input[@placeholder="* Фамилия"]')
    # Локатор поля Адрес
    FIELD_ADDRESS = (By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]')
    # Локатор поля Станция метро
    FIELD_METRO = (By.XPATH, '//input[@placeholder="* Станция метро"]')
    # Поле метро Академическая
    AKADEMKA_METRO = (By.XPATH, '//li[@class="select-search__row" and @data-index="94"]')
    # Локатор поля Телефон
    FIELD_TELEPHONE = (By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]')
    # Кнопка согласия с куками
    COOKIES_CONFIRMATION = (By.XPATH, '//button[@id="rcc-confirm-button"]')
    # Локатор кнопки Далее
    ONWARDS_BUTTON = (By.XPATH, "//button[text()='Далее']")
    # Локатор чекбокса Серая безысходность
    GRAY_COLOR = (By.XPATH, "//input[@id='grey']")
    # Поле когда привезти самокат
    TIME_OF_DELIVERY = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    # выбор 25 числа
    DESIRABLE_DATE_TWO = (By.XPATH, "//div[text()='25']")
    # Поле срока аренды
    RENTAL_FIELD = (By.XPATH, "//div[text()='* Срок аренды']")
    # Выбор срока аренды 3 дня
    RENTAL_TIME_TWO = (By.XPATH, "//div[@class='Dropdown-option' and text()='трое суток']")
    # Выбор поля комментариев для курьера
    COMMENT_FIELD = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    # Кнопка подтверждения заказа
    CONFIRMATION_ORDER_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Заказать']")
    # Кнопка Да
    YES_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Да']")
    # Заказ оформлен
    ORDER_IS_CONFIRMED = (By.XPATH, "//div[@class='Order_ModalHeader__3FDaJ']")
    # Кнопка посмотреть статус
    LOOK_STATUS_BUTTON = (By.XPATH, "//button[text()='Посмотреть статус']")
    # Лого Яндекса
    YANDEX_LOGO = (By.XPATH, "//img[@alt='Yandex']")
    # Лого Самоката
    SCOOTER_LOGO = (By.XPATH, "//img[@alt='Scooter']")
