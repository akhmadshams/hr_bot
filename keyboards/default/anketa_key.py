from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

back_key = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text="🚫️️️️️️ Bekor qilish")
        ]
    ],
    resize_keyboard=True
)

back_key1 = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text="🚫️️️️️️ To\'xtatish")
        ]
    ],
    resize_keyboard=True
)



phone_key = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text='📲 Tel raqamni yuborish', request_contact=True)
        ],
        [
            KeyboardButton(text="🚫️️️️️️ Bekor qilish")
        ]
    ],
    resize_keyboard=True
)


region_key = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text="Qo\'qon shahar"),
            KeyboardButton(text="Dang'ara tumani")

        ],
        [
            KeyboardButton(text="Uchko\'prik tumani"),
            KeyboardButton(text="Bag\'dod tumani")
        ],
        [
            KeyboardButton(text="Furqat tumani"),
            KeyboardButton(text="O\'zbekiston tumani")
        ],
        [
            KeyboardButton(text='🚫️️️️️️ Bekor qilish')
        ]
    ],
    resize_keyboard=True
)


degree_key = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text="👨‍🎓 Oliy"),
            KeyboardButton(text='👨‍💼 O\'rta maxsus')
        ],
        [
            KeyboardButton(text='🧑‍🏫 Tugallanmagan oliy'),

        ],
        [
            KeyboardButton(text='🚫️️️️️️ Bekor qilish')
        ]
    ],
    resize_keyboard=True
)


work_key = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text='♻️ Hech qayerda ishlamaganman')
        ],
        [
            KeyboardButton(text='🚫️️️️️️ Bekor qilish')
        ]
    ],
    resize_keyboard=True
)


addition_key = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text="⏭ O\'tkazib yuborish")
        ],
        [
            KeyboardButton(text='🚫️️️️️️ Bekor qilish')
        ]
    ],
    resize_keyboard=True
)