from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Ru'), KeyboardButton(text='En'), KeyboardButton(text='Kz')],
    ],
    resize_keyboard=True,
)


#RU RU RU RU RURU RU RU RU

rukatalog = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='О Нас'), KeyboardButton(text='Блог'), KeyboardButton(text='Спонсоры')],
        [KeyboardButton(text='Цены')],
    ],
    resize_keyboard=True,
    one_time_keyboard=False
)

ruprice = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Корпоративный сайт'), KeyboardButton(text='Премиум сайт'), KeyboardButton(text='Интернет-магазин')],
        [KeyboardButton(text='Назад в Меню')],
    ],
    resize_keyboard=True
)

#======================EN EN EN EN+=======
enkatalog = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='About Us'), KeyboardButton(text='Blog'), KeyboardButton(text='Sponsors')],
        [KeyboardButton(text='Prices')],
    ],
    resize_keyboard=True,
    one_time_keyboard=False
)

enprice = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Corporate site'), KeyboardButton(text='Premium site'), KeyboardButton(text='Online store')],
        [KeyboardButton(text='Back to Menu')],
    ],
    resize_keyboard=True
)

#KZ KZ KZ KZ KZ KZ KZ KZ KZ

kzkatalog = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Біз туралы'), KeyboardButton(text='Блог'), KeyboardButton(text='Спонсорлар')],
        [KeyboardButton(text='Бағалар')],
    ],
    resize_keyboard=True,
    one_time_keyboard=False
)

kzprice = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Корпоративті сайт'), KeyboardButton(text='премиум сайт'), KeyboardButton(text='Интернет-дүкен')],
        [KeyboardButton(text='Менюге қайту')],
    ],
    resize_keyboard=True
)