from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

post_callback = CallbackData("create_post", "action")
confirmation_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(text="🆗 Tasdiqlash", callback_data=post_callback.new(action="post")),
        InlineKeyboardButton(text="❌ Bekor qilish", callback_data=post_callback.new(action="cancel")),
    ]]
)


edit_key = InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(text="🗑 Delete", callback_data='delete'),
        InlineKeyboardButton(text="🖋 Edit", callback_data='edit'),
    ]]
)
