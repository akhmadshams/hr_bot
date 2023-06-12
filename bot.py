# import sqlite3
#
# # O'chirish uchun funksiya
# def delete_data_from_db(workplace_id):
#     conn = sqlite3.connect("data/main.db")  # Ma'lumotlar bazasiga ulanish
#     cursor = conn.cursor()
#     cursor.execute("DELETE FROM Workplace WHERE id=?", (workplace_id,))
#     conn.commit()
#     conn.close()
#
# # workplace_id ni o'chirish funksiyasiga uzatish
# workplace_id = 10 # O'chirishni istagan malumotning ID-si
# delete_data_from_db(workplace_id)

import sqlite3
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Botni yaratish
bot = Bot(token="5857577753:AAFuhaL5tDBWZgZnBsinktVy_J7ffn6Y4F8")
dp = Dispatcher(bot)

# Malumotlar bazasidan "title" ustunidagi malumotlarni olish
def get_titles_from_db():
    conn = sqlite3.connect("data/main.db")
    cursor = conn.cursor()
    cursor.execute("SELECT work_title FROM Workplace")
    rows = cursor.fetchall()
    titles = [row[0] for row in rows]
    conn.close()
    return titles


# Workplace jadvalidan tanlangan malumotni o'chirish
def delete_workplace_from_db(title):
    conn = sqlite3.connect("data/main.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Workplace WHERE work_title=?", (title,))
    conn.commit()
    conn.close()


# /start buyrug'i uchun handler
@dp.message_handler(commands=['start'])
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

# Botni ishga tushirish
if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)


