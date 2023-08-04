import logging
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery
from data.config import ADMINS
from keyboards.inline.confirm import confirmation_keyboard, post_callback
from loader import db, dp
from keyboards.default.anketa_key import  back_key1
from keyboards.default.admin_key import work_edit, admin_menu
from states.work import WorkState


@dp.message_handler(text='🆓 Ish o\'rinlarini tahrirlash', user_id=ADMINS)
async def work(message: Message):
    await message.answer('<b>Siz ish o\'rinlarini tahrirlashingiz mumkin</b>',  reply_markup=work_edit)


@dp.message_handler(text="➕ Ish qo'shish", user_id=ADMINS, state=None)
async def addwork(message: Message):
    await message.answer("<b>💼 Ish nomini kiriting</b>", reply_markup=back_key1)
    await WorkState.title.set()

@dp.message_handler(state='*', text='🚫️️️️️️ To\'xtatish')
@dp.message_handler(Text(equals='🚫️️️️️️ To\'xtatish', ignore_case=True), state='*')
async def cancel_handler(message: Message, state: FSMContext):
    """
    Allow user to cancel any action
    """
    current_state = await state.get_state()
    if current_state is None:
        return

    logging.info('Cancelling state %r', current_state)
    # Cancel state and inform user about it
    await state.finish()
    # And remove keyboard (just in case)
    await message.reply('Siz buyruqlarni bekor qildingiz', reply_markup=admin_menu)

@dp.message_handler(state=WorkState.title, user_id=ADMINS)
async def title_answer(message: Message, state: FSMContext):
    title = message.text
    await state.update_data(
        {
            'title':title
        }
    )
    await message.answer("<b>📝 Ish haqida batafsil ma\'lumot kiriting</b>", reply_markup=back_key1)
    await WorkState.next()



@dp.message_handler(state=WorkState.body, user_id=ADMINS)
async def body_answer(message: Message, state: FSMContext):
    body = message.text
    await state.update_data(
        {
            'body':body
        }
    )
    await message.answer("<b>🖼 Rasm yuboring</b>", reply_markup=back_key1)
    await WorkState.next()


@dp.message_handler(state=WorkState.image, content_types='photo', user_id=ADMINS)
async def image_answer(message: Message, state: FSMContext):
    image = message.photo[-1].file_id
    await state.update_data(
        {
            'image':image
        }
    )
    await message.answer("<b>💴 Ish uchun qancha haq to\'lanadi</b>", reply_markup=back_key1)
    await WorkState.next()

@dp.message_handler(state=WorkState.salary)
async def salary_answer(message: Message, state: FSMContext):
    salary = message.text
    await state.update_data(
        {
            'salary': salary
        }
    )
    await message.answer("<b>🧾 Barcha ma\'lumotlar to\'g\'riligiga e\'tibor bering</b>", reply_markup=work_edit)
    await WorkState.next()

    data = await state.get_data()
    title = data.get("title")
    body = data.get('body')
    image = data.get('image')
    # salary = data.get('salary')
    await db.add_work(work_title=title, image=image, description=body)
    caption = f"<b>{title}\n</b>"
    caption += f"{body}\n\n"
    # caption += f"<b>Ish haqqi: {salary}\n\n</b>"
    caption += f"Ko\'proq ma\'lumot: @hrfmasmaldgroup"
    await message.answer_photo(photo=image, caption=caption, reply_markup=confirmation_keyboard)
    await WorkState.next()



@dp.callback_query_handler(post_callback.filter(action="post"))
async def work_add(call: CallbackQuery, state: FSMContext):
    await call.answer("Habaringiz yuborildi!", show_alert=True)
    message = await call.message.edit_reply_markup()
    await message.answer('Ish joylandi')

@dp.callback_query_handler(post_callback.filter(action="cancel"))
async def cancel_post(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.answer("Habaringiz rad etildi!", show_alert=True)
    await call.message.edit_reply_markup()
    await call.message.answer("Habaringiz rad etildi!")


@dp.callback_query_handler(post_callback.filter(action="cancel"), user_id=ADMINS)
async def decline_post(call: CallbackQuery):
    await call.answer("Post rad etildi.", show_alert=True)
    await call.message.edit_reply_markup()



@dp.message_handler(text="🔙 Ortga", user_id=ADMINS)
async def back_work(message: Message):
    await message.answer("Admin menu", reply_markup=admin_menu)

