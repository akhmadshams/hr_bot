from aiogram.types import ReplyKeyboardMarkup, KeyboardButton



admin_menu = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text="📈 Umumiy ma\'lumot"),
            KeyboardButton(text="📈 Oylik ma\'lumotlar")
        ],
        [
            KeyboardButton(text="📈 Haftalik ma\'lumotlar"),
            KeyboardButton(text="📈 Kunlik ma\'lumotlar")
        ],
        [
            KeyboardButton(text="🆓 Ish o\'rinlarini tahrirlash"),
            KeyboardButton(text="🎯 Reklama"),
        ],
        [
            KeyboardButton(text="🔄 Foydalanuvchilar soni")
        ],
        [
            KeyboardButton(text="🎯 Bosh menu")
        ]
    ],
    resize_keyboard=True
)


work_edit = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text='➕ Ish qo\'shish'),
            KeyboardButton(text='➖ Ishni tahrirlash')
        ],
        [
            KeyboardButton(text="🔙 Ortga")
        ]
    ],
    resize_keyboard=True
)