from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from loader import dp, db, bot
from aiogram import types

# Malumotlar bazasidan kelgan malumotlardan InlineKeyboardButtonlar ro'yxatini yaratish
def create_inline_keyboard(buttons):
    keyboard = InlineKeyboardMarkup(row_width=2)
    for button in buttons:
        name = button[0]  # name nomli ustun qiymati
        callback_data = name  # callback_data nomi ham name nomiga teng
        keyboard.add(InlineKeyboardButton(name, callback_data=callback_data))
    return keyboard


@dp.message_handler(text='🆓 Bo\'sh ish o\'rinlari')
async def edit_work(message: Message):
    data = db.read_work()
    keyboard = create_inline_keyboard(data)
    await message.reply("Tugmalardan birini tanlang:", reply_markup=keyboard)



@dp.callback_query_handler()
async def callback_handler(callback_query: CallbackQuery):
    callback_data = callback_query.data
    chat_id = callback_query.from_user.id
    data = db.read_work_all()
    work = db.read_work()
    keyboard = create_inline_keyboard(work)
    for row in data:
        work_id, work_title, image, salary, description = row
        if callback_data == work_title:
            # Rasmni yuborish
            caption = f"{work_title}\n"
            caption += f"{salary}\n"
            caption += f"{description}\n"
            await callback_query.message.edit_reply_markup()
            await bot.send_photo(chat_id=chat_id, photo=image, caption=caption, reply_markup=keyboard)
            return
    await bot.send_message(chat_id=chat_id, text="Malumot topilmadi.")


