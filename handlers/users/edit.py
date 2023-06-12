import sqlite3
from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from loader import dp, db


# Malumotlar bazasidan "title" ustunidagi malumotlarni olish
def get_titles_from_db():
    # conn = sqlite3.connect("data/main.db")
    # cursor = conn.cursor()
    # cursor.execute("SELECT work_title FROM Workplace")
    rows = db.read_work()
    titles = [row[0] for row in rows]
    # conn.close()
    return titles


# Workplace jadvalidan tanlangan malumotni o'chirish
def delete_workplace_from_db(title):
    # conn = sqlite3.connect("data/main.db")
    # cursor = conn.cursor()
    # cursor.execute("DELETE FROM Workplace WHERE work_title=?", (title,))
    # conn.commit()
    # conn.close()
    db.delete_work(title=title)


# /start buyrug'i uchun handler
@dp.message_handler(text='➖ Ishni tahrirlash')
async def start(message: types.Message):
    titles = get_titles_from_db()
    # ReplyKeyboardMarkup yaratish
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    for title in titles:
        keyboard.add(KeyboardButton(title))
    await message.reply("Ish joylarini tanlang:", reply_markup=keyboard)

# KeyboardButton bosilganda tanlangan malumotni o'chirish
@dp.message_handler()
async def handle_message(message: types.Message):
    selected_title = message.text
    # Workplace jadvalidan tanlangan malumotni o'chirish
    delete_workplace_from_db(selected_title)
    response = f"{selected_title} o'chirildi"
    await message.reply(response)
