from selenium.webdriver.common.by import By

class Constants:
    URL = "https://qa-scooter.praktikum-services.ru/"
    PHRASE = "Сутки — 400 рублей. Оплата курьеру — наличными или картой."
    COURIER_COMMENT = 'Миру - мир!'
    ARRAY_OF_TUPLES = (
        (
            ("//div[@id='accordion__heading-0' and @class='accordion__button']"),
            ('//div[@id="accordion__panel-0"]/p[text()]'),
            ("Сутки — 400 рублей. Оплата курьеру — наличными или картой.")
        ),
                       (
                        ("//div[@id='accordion__heading-1' and @class='accordion__button']"),
                        ('//div[@id="accordion__panel-1"]/p[text()]'),
                        ("Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.")
                       ),
        (
            ("//div[@id='accordion__heading-2' and @class='accordion__button']"),
            ('//div[@id="accordion__panel-2"]/p[text()]'),
            ("Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.")
        ),
        (
            ("//div[@id='accordion__heading-3' and @class='accordion__button']"),
            ('//div[@id="accordion__panel-3"]/p[text()]'),
            ("Только начиная с завтрашнего дня. Но скоро станем расторопнее.")
        ),
        (
            ("//div[@id='accordion__heading-4' and @class='accordion__button']"),
            ('//div[@id="accordion__panel-4"]/p[text()]'),
            ("Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.")
        ),
        (
            ("//div[@id='accordion__heading-5' and @class='accordion__button']"),
            ('//div[@id="accordion__panel-5"]/p[text()]'),
            ("Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.")
        ),
        (
            ("//div[@id='accordion__heading-6' and @class='accordion__button']"),
            ('//div[@id="accordion__panel-6"]/p[text()]'),
            ("Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.")
        ),
        (
            ("//div[@id='accordion__heading-7' and @class='accordion__button']"),
            ('//div[@id="accordion__panel-7"]/p[text()]'),
            ("Да, обязательно. Всем самокатов! И Москве, и Московской области.")
        )
                       )