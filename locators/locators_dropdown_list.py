from selenium.webdriver.common.by import By

class TupplesOfLocators:
    TUPPLES_OF_LOCATORS = (
        (
            (By.XPATH, "//div[@id='accordion__heading-0' and @class='accordion__button']"), #локатор стрелочки 1
            (By.XPATH, '//div[@id="accordion__panel-0"]/p[text()]'), #локатор текста1
            ("Сутки — 400 рублей. Оплата курьеру — наличными или картой.")
        ),
                       (
                        (By.XPATH, "//div[@id='accordion__heading-1' and @class='accordion__button']"), #локатор стрелочки 2
                        (By.XPATH, '//div[@id="accordion__panel-1"]/p[text()]'), #локатор текста2
                        ("Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.")
                       ),
        (
            (By.XPATH, "//div[@id='accordion__heading-2' and @class='accordion__button']"),#локатор стрелочки 3
            (By.XPATH, '//div[@id="accordion__panel-2"]/p[text()]'), #локатор текста3
            ("Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.")
        ),
        (
            (By.XPATH, "//div[@id='accordion__heading-3' and @class='accordion__button']"),#локатор стрелочки 4
            (By.XPATH, '//div[@id="accordion__panel-3"]/p[text()]'), #локатор текста4
            ("Только начиная с завтрашнего дня. Но скоро станем расторопнее.")
        ),
        (
            (By.XPATH, "//div[@id='accordion__heading-4' and @class='accordion__button']"),#локатор стрелочки 5
            (By.XPATH, '//div[@id="accordion__panel-4"]/p[text()]'), #локатор текста5
            ("Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.")
        ),
        (
            (By.XPATH, "//div[@id='accordion__heading-5' and @class='accordion__button']"), #локатор стрелочки 6
            (By.XPATH, '//div[@id="accordion__panel-5"]/p[text()]'), #локатор текста6
            ("Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.")
        ),
        (
            (By.XPATH, "//div[@id='accordion__heading-6' and @class='accordion__button']"), #локатор стрелочки 7
            (By.XPATH, '//div[@id="accordion__panel-6"]/p[text()]'), #локатор текста7
            ("Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.")
        ),
        (
            (By.XPATH, "//div[@id='accordion__heading-7' and @class='accordion__button']"), #локатор стрелочки 8
            (By.XPATH, '//div[@id="accordion__panel-7"]/p[text()]'), #локатор текста8
            ("Да, обязательно. Всем самокатов! И Москве, и Московской области.")
        )
    )


class LocatorsDropDownListPage:
    # Кнопка согласия с куками
    COOKIES_CONFIRMATION = (By.XPATH, '//button[@id="rcc-confirm-button"]')