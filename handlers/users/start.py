import sqlite3
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import Message
from aiogram.dispatcher.filters.builtin import CommandStart
from data.config import ADMINS
from loader import dp, db, bot
from utils.misc.get_distance import choose_shortest
from keyboards.default.menu import location_key
from keyboards.default.menu import main_menu



@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    name = message.from_user.full_name
    # Foydalanuvchini bazaga qo'shamiz
    try:
        db.add_user(id=message.from_user.id,
                    name=name)
    except sqlite3.IntegrityError as err:
        await bot.send_message(chat_id=ADMINS[0], text=err)

    await message.answer("Xush kelibsiz!", reply_markup=main_menu)
    # Adminga xabar beramiz
    count = db.count_users()[0]
    msg = f"{message.from_user.full_name} bazaga qo'shildi.\nBazada {count} ta foydalanuvchi bor."
    await bot.send_message(chat_id=ADMINS[0], text=msg)

@dp.message_handler(text='📍️️️️️️ Location')
async def process_balance(message: Message, state: FSMContext):
    await message.answer('<b>Siz joylashuvingizni yuborish orqali bizning\nmarkazimiz joylashuvi va sizda qancha masofada joylashgani\n haqida ma`lumot olishingiz mumkin !</b>', reply_markup=location_key)


@dp.message_handler(content_types='location')
async def get_contact(message: Message):
    location = message.location
    closest_shops = choose_shortest(location)

    text = "\n\n".join([f"<a href='{url}'>{shop_name}</a>\n Masofa: {distance:.1f} km."
                        for shop_name, distance, url, shop_location in closest_shops])

    await message.answer(f"Manzilgacha bo`lgan masofa 👇\n\n\n"
                         f"{text}", disable_web_page_preview=True, reply_markup=main_menu)

    for shop_name, distance, url, shop_location in closest_shops:
        await message.answer_location(latitude=shop_location["lat"],
                                      longitude=shop_location["lon"])

@dp.message_handler(text='🌐 Ma\'lumot')
async def about(message: Message):
    text = "<b>Tel: +998911431100</b>\n"
    text += "<b>Admin: @europrint_hrm</b>\n"
    text += "<b>Kanal: https://t.me/vakansiya_europrint</b>\n"
    await message.answer(text)
