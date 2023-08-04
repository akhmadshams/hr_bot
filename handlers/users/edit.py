import sqlite3
from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from loader import dp, db


def create_keyboard(buttons):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    for button in buttons:
        name = button  # name nomli ustun qiymati
        keyboard.add(types.KeyboardButton(name))
    return keyboard

@dp.message_handler(text='➖ Ishni tahrirlash')
async def start(message: types.Message):
    data = await db.read_work()
    keyboard = create_keyboard(data)
    await message.reply("Ish joylarini tanlang:", reply_markup=keyboard)

@dp.message_handler()
async def handle_message(message: types.Message):
    title = message.text
    await db.delete_work(title)
    response = f"{title} o'chirildi"
    await message.reply(response)

