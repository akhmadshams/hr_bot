import sqlite3
from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from loader import dp, db

def get_titles_from_db():
    rows = db.read_work()
    titles = [row[0] for row in rows]
    return titles



def delete_workplace_from_db(title):
    db.delete_work(title)


# /start buyrug'i uchun handler
@dp.message_handler(text='➖ Ishni tahrirlash')
async def start(message: types.Message):
    titles = get_titles_from_db()
    # ReplyKeyboardMarkup yaratish
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    for title in titles:
        keyboard.add(KeyboardButton(title))
    await message.reply("Ish joylarini tanlang:", reply_markup=keyboard)

@dp.message_handler()
async def handle_message(message: types.Message):
    selected_title = message.text
    delete_workplace_from_db(selected_title)
    response = f"{selected_title} o'chirildi"
    await message.reply(response)

