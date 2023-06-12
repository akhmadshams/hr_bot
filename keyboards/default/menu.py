from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text="📇️️️️️️ Anketa"),
            KeyboardButton(text="🆓 Bo\'sh ish o\'rinlari")
        ],
        [
            KeyboardButton(text="💼 Ish o\'rinlari")
        ],
        [
            KeyboardButton(text="📍️️️️️️ Location")
        ],
        [
            KeyboardButton(text="🌐 Ma\'lumot")
        ]
    ],
    resize_keyboard=True
)



location_key = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text="📍️️️️️️ Location yuborish", request_location=True)
        ],
        [
            KeyboardButton(text='🎯 Bosh menu')
        ]
    ],
    resize_keyboard=True
)