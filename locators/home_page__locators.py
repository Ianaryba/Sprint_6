ACCORDION_MAIN = "div[class*='Home_FAQ'] .accordion"

ACCORDION_ITEM_HOW_PAY = "//div[@class='accordion__item']/div/div[text()='Сколько это стоит? И как оплатить?']"
ACCORDION_ITEM_FEW_SCOOTER = "//div[@class='accordion__item']/div/div[text()='Хочу сразу несколько самокатов! Так можно?']"
ACCORDION_ITEM_RENT_TIME = "//div[@class='accordion__item']/div/div[text()='Как рассчитывается время аренды?']"
ACCORDION_ITEM_RENT_FOR_TODAY = "//div[@class='accordion__item']/div/div[text()='Можно ли заказать самокат прямо на сегодня?']"
ACCORDION_ITEM_RENEW_OR_RETURN_EARLIER = "//div[@class='accordion__item']/div/div[text()='Можно ли продлить заказ или вернуть самокат раньше?']"
ACCORDION_ITEM_CHARGER = "//div[@class='accordion__item']/div/div[text()='Вы привозите зарядку вместе с самокатом?']"
ACCORDION_ITEM_DECLINE_ORDER = "//div[@class='accordion__item']/div/div[text()='Можно ли отменить заказ?']"
ACCORDION_ITEM_LIVE_OUTSIDE_OF_MKAD = "//div[@class='accordion__item']/div/div[text()='Я жизу за МКАДом, привезёте?']"

ACCORDION_PANEL_HOW_PAY = "//p[text()='Сутки — 400 рублей. Оплата курьеру — наличными или картой.']"
ACCORDION_PANEL_FEW_SCOOTER = "//p[text()='Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.']"
ACCORDION_PANEL_RENT_TIME = "//p[text()='Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.']"
ACCORDION_PANEL_RENT_FOR_TODAY = "//p[text()='Только начиная с завтрашнего дня. Но скоро станем расторопнее.']"
ACCORDION_PANEL_RENEW_OR_RETURN_EARLIER = "//p[text()='Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.']"
ACCORDION_PANEL_CHARGER = "//p[text()='Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.']"
ACCORDION_PANEL_DECLINE_ORDER = "//p[text()='Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.']"
ACCORDION_PANEL_LIVE_OUTSIDE_OF_MKAD = "//p[text()='Да, обязательно. Всем самокатов! И Москве, и Московской области.']"

ACCORDION_PANEL_MAIN = "div[class*='Home_FAQ'] .accordion__panel"

ORDER_BUTTON_TOP = "//div[starts-with(@class, 'Header_Nav')]/button[text()='Заказать']"
ORDER_BUTTON_BOTTOM = "//div[starts-with(@class, 'Home_FinishButton')]/button[text()='Заказать']"

ORDER_NAME = "//input[@placeholder = '* Имя']"
ORDER_LAST_NAME = "//input[@placeholder = '* Фамилия']"
ORDER_ADDRESS = "//input[@placeholder = '* Адрес: куда привезти заказ']"
ORDER_METRO = "//input[@placeholder = '* Станция метро']"
ORDER_PHONE_NUMBER = "//input[@placeholder = '* Телефон: на него позвонит курьер']"
ORDER_NEXT_BUTTON = "//div//button[text() = 'Далее']"

ORDER_WHEN = "//input[@placeholder = '* Когда привезти самокат']"
ORDER_HOW_LONG = "//div[text() = '* Срок аренды']"
ORDER_COMMENT = "//input[@placeholder = 'Комментарий для курьера']"
ORDER_COMPLETE = "//div[starts-with(@class, 'Order_Buttons')]/button[text()='Заказать']"
SCOOTER_COLOR_BLACK = "input#black"
SCOOTER_COLOR_GRAY = "input#grey"

ORDER_CONFIRMATION_BUTTON = "//button[text() = 'Да']"

MESSAGE_ABOUT_SUCCESSFUL_ORDER_CREATION = "//div[text() = 'Заказ оформлен']"
WATCH_STATUS_BUTTON = "//button[text() = 'Посмотреть статус']"
YANDEX_LOGO = "//a/img[@alt = 'Yandex']"
SCOOTER_LOGO = "//a/img[@alt = 'Scooter']"

