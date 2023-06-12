import sqlite3
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher.filters import Text
import logging
from data.config import ADMINS
from keyboards.inline.confirm import confirmation_keyboard, post_callback
from loader import dp, db, bot
from states.personal import PersonalState
from states.newpost import NewPost
from keyboards.default.anketa_key import back_key,phone_key,region_key,degree_key,work_key,addition_key
from keyboards.default.menu import main_menu
conn = sqlite3.connect('data/main.db')
cursor = conn.cursor()


@dp.message_handler(text='📇️️️️️️ Anketa', state=None)
async def anketa_pass(message: Message):
    await message.answer("<b>🖋 F.I.SH kiriting</b>", reply_markup=back_key)
    await PersonalState.name.set()

@dp.message_handler(state='*', text='🚫️️️️️️ Bekor qilish')
@dp.message_handler(Text(equals='🚫️️️️️️ Bekor qilish', ignore_case=True), state='*')
async def cancel_handler(message: types.Message, state: FSMContext):
    """
    Allow user to cancel any action
    """
    current_state = await state.get_state()
    if current_state is None:
        return

    logging.info('Cancelling state %r', current_state)
    await state.finish()
    await message.reply('Siz buyruqlarni bekor qildingiz', reply_markup=main_menu)


@dp.message_handler(state=PersonalState.name)
async def answer_name(message: types.Message, state: FSMContext):
    name = message.text
    await state.update_data(
        {"name": name}
    )
    await message.answer("<b>📆 Tug\'ilgan sana kiriting.Misol uchun (13.12.1997)</b>", reply_markup=back_key)
    await PersonalState.next()


@dp.message_handler(state=PersonalState.b_date)
async def answer_bdate(message: Message, state: FSMContext):
    b_date = message.text
    await state.update_data(
        {"b_date":b_date}
    )
    await message.answer("<b>📱 Tel raqamingizni quyidagi tugma orqali yuboring</b>", reply_markup=phone_key)
    await PersonalState.next()


@dp.message_handler(lambda message: not message.text.isdigit(), state=PersonalState.phone)
async def process_phone_invalid(message: types.Message):
    return await message.reply("<b>⬇️ Qulaylik uchun quyidagi tugmani bosing!</b>")


@dp.message_handler(state=PersonalState.phone, content_types='contact')
async def answer_phone(message: Message, state: FSMContext):
    phone = message.contact.phone_number
    async with state.proxy() as data:
        data["phone"] = phone
    await message.answer("<b>🌎 Hududni tanlang</b>", reply_markup=region_key) #hududlar key
    await PersonalState.next()



@dp.message_handler(state=PersonalState.region)
async def answer_region(message: Message, state: FSMContext):
    region = message.text
    await state.update_data(
        {'region':region}
    )
    await message.answer("<b>🏢 Manzilni to\'liq kiriting (MFY va Ko\'ch nomi)</b>", reply_markup=back_key)
    await PersonalState.next()


@dp.message_handler(state=PersonalState.address)
async def answer_address(message: Message, state:FSMContext):
    address = message.text
    await state.update_data(
        {
            "address":address
        }
    )
    await message.answer("<b>👨‍🎓 Ma'lumotingizni tanlang</b>", reply_markup=degree_key) #malumot key keladi
    await PersonalState.next()


@dp.message_handler(state=PersonalState.degree)
async def answer_degree(message: Message, state: FSMContext):
    degree = message.text
    await state.update_data(
        {
            "degree":degree
        }
    )
    await message.answer("<b>💼 Eski ish joyingiz haqida</b>", reply_markup=work_key) # keyboard keladi
    await PersonalState.next()


def create_keyboard(buttons):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    for button in buttons:
        name = button[0]  # name nomli ustun qiymati
        keyboard.add(types.KeyboardButton(name))
    return keyboard


# Komandalar ro'yxati
@dp.message_handler(state=PersonalState.old_work)
async def answer_work(message: Message, state: FSMContext):
    work = message.text
    data = db.read_work()
    keyboard = create_keyboard(data)
    await state.update_data(
        {
            'work': work
        }
    )
    await message.answer("🔀 Siz qaysi ishda ishlamoqchisiz", reply_markup=keyboard)
    await PersonalState.next()


@dp.message_handler(state=PersonalState.position)
async def answer_position(message: Message, state: FSMContext):
    position = message.text
    await state.update_data(
        {
            "position":position
        }
    )
    await message.answer("<b>🔅 Qo\'shimcha ma\'lumot</b>", reply_markup=addition_key)
    await PersonalState.next()

@dp.message_handler(state=PersonalState.additions)
async def answer_add(message: Message, state: FSMContext):
    addition = message.text
    mention = message.from_user.mention
    await state.update_data(
        {
            "addition":addition
        }
    )
    await message.answer("<b>🧾 Ma\'lumotlar to\'g\'riligiga e\'tibor bering</b>", reply_markup=main_menu)
    await PersonalState.next()

    data = await state.get_data()
    name = data.get("name")
    b_date = data.get('b_date')
    phone = data.get('phone')
    region = data.get('region')
    address = data.get('address')
    degree = data.get('degree')
    work = data.get('work')
    position = data.get('position')
    addition = data.get('addition')
    db.add_worker(name=name, b_date=b_date, phone=phone, region=region, address=address, degree=degree, work=work, position=position, addition=addition)
    text = "<b>Quyidagi ma\'lumotlar qabul qilindi 👇</b>\n\n"
    if mention:
        text += f"<b>🙎‍♂ F.I.SH: {name} - {mention}\n\n</b>"
    else:
        text += f"<b>🙎‍♂ F.I.SH: {name}\n\n</b>"
    text += f"<b>🗓 Tug\'ilgan vaqti: {b_date}\n\n</b>"
    text += f"<b>📱 Telefon raqami: {phone}\n\n</b>"
    text += f"<b>🌍 Hudud:  {region}\n\n</b>"
    text += f"<b>🏢 Manzil: {address}\n\n</b>"
    text += f"<b>👨‍🎓 Ma\'lumoti: {degree}\n\n</b>"
    text += f"<b>💼 Eski ish joyi: {work}\n\n</b>"
    text += f"<b>🔀 Positsiyasi: {position}\n\n</b>"
    if addition != '⏭ O\'tkazib yuborish':
        text += f"<b>🔅 Qoshimcha: {addition}\n\n</b>"
    await message.answer(text, reply_markup=confirmation_keyboard)
    await PersonalState.next()


@dp.callback_query_handler(post_callback.filter(action="post"))
async def approve_post(call: CallbackQuery, state: FSMContext):
    await call.answer("Habaringiz yuborildi!", show_alert=True)
    message = await call.message.edit_reply_markup()
    await message.send_copy(-1001966008238)



@dp.callback_query_handler(post_callback.filter(action="cancel"))
async def cancel_post(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.answer("Habaringiz rad etildi!", show_alert=True)
    await call.message.edit_reply_markup()
    await call.message.answer("Habaringiz rad etildi!")



@dp.message_handler(state=NewPost.Confirm)
async def post_unknown(message: Message):
    await message.answer("Chop etish yoki rad etishni tanlang")


@dp.callback_query_handler(post_callback.filter(action="cancel"), user_id=ADMINS)
async def decline_post(call: CallbackQuery):
    await call.answer("Post rad etildi.", show_alert=True)
    await call.message.edit_reply_markup()