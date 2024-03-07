from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

from data import *
from Buttons import Total_buttons, One_buttons, THREE_BUTTONS
from functions import check_regist, append_id_number, append_full_info_in_xlsx

bot = Bot("6257332824:AAFF7VtktI21y_Cj0hSKcRbYHrrxfG5kC-I")
dp = Dispatcher()
class Form(StatesGroup):
    name = State()
    mail = State()
    number_phone = State()
    school = State()
    class_school = State()
    parent_name = State()
    number_parents = State()
    one_issue = State()
    two_issue = State()
    three_issue = State()

    registration = State()

@dp.message(Command(commands="start"), F.text)
async def start_bot(message: Message, state: FSMContext) -> None:
    if check_regist(str(message.chat.id)):
        await message.answer(text=TEXT_START, reply_markup=ReplyKeyboardRemove())
        await message.answer(text=TEXT_NAME)
        await state.clear()
        await state.set_state(Form.name)
    else:
        await message.answer(text=TEXT_RST)

@dp.message(Form.name, F.text)
async def name_query(message: Message, state: FSMContext) -> None:
    await state.update_data(name=message.text)
    await state.set_state(Form.mail)

    await message.answer(text=TEXT_EMAIL)

@dp.message(Form.mail, F.text)
async def name_query(message: Message, state: FSMContext) -> None:
    await state.update_data(mail=message.text)
    await state.set_state(Form.number_phone)

    await message.answer(text=TEXT_NUMBER)

@dp.message(Form.number_phone, F.text)
async def name_query(message: Message, state: FSMContext) -> None:
    await state.update_data(number_phone=message.text)
    await state.set_state(Form.school)

    await message.answer(text=TEXT_SCHOOL)

@dp.message(Form.school, F.text)
async def name_query(message: Message, state: FSMContext) -> None:
    await state.update_data(school=message.text)
    await state.set_state(Form.class_school)

    await message.answer(text=TEXT_CLASS)

@dp.message(Form.class_school, F.text)
async def name_query(message: Message, state: FSMContext) -> None:
    await state.update_data(class_school=message.text)
    await state.set_state(Form.parent_name)

    await message.answer(text=TEXT_NAME_PARENTS)

@dp.message(Form.parent_name, F.text)
async def name_query(message: Message, state: FSMContext) -> None:
    await state.update_data(parent_name=message.text)
    await state.set_state(Form.number_parents)

    await message.answer(text=TEXT_NUMBER_PARENTS)

@dp.message(Form.number_parents, F.text)
async def name_query(message: Message, state: FSMContext) -> None:
    await state.update_data(number_parents=message.text)
    await state.set_state(Form.one_issue)

    await message.answer(text=TEXT_NEXT, reply_markup=Total_buttons)

@dp.message(Form.one_issue, F.text)
async def one_issue(message: Message, state: FSMContext) -> None:
    await state.update_data(one_issue=message.text)
    await state.set_state(Form.two_issue)

    await message.answer(text=TEXT_END, reply_markup=One_buttons)

@dp.message(Form.two_issue, F.text)
async def two_issue(message: Message, state: FSMContext) -> None:
    await state.update_data(two_issue=message.text)
    await state.set_state(Form.three_issue)

    await message.answer(text=TEXT_TOTAL, reply_markup=THREE_BUTTONS)

@dp.message(Form.three_issue, F.text)
async def three_issue(message: Message, state: FSMContext) -> None:
    data = await state.update_data(three_issue=message.text)
    await state.set_state(Form.registration)

    await message.answer(text=TEXT_LIST.format(data["name"], data["mail"], data["number_phone"], data["school"], data["class_school"], data["parent_name"], data["number_parents"]), reply_markup=Total_buttons)

@dp.message(Form.registration, F.text == "ДА🤝")
async def regestration(message: Message, state: FSMContext):
    data = await state.update_data(regestration="OK")
    arr = [data["name"], data["mail"], message.from_user.username, data["number_phone"], data["school"], data["class_school"], data["parent_name"], data["number_parents"], data["one_issue"], data["two_issue"], data["three_issue"]]

    append_id_number(message.chat.id)
    append_full_info_in_xlsx(arr)

    await state.clear()
    await message.answer(text=TEXT_REGIST, reply_markup=ReplyKeyboardRemove())

@dp.message(Form.registration, F.text == "НЕТ❌")
async def not_registration(message: Message, state: FSMContext) -> None:
    await state.clear()
    await state.set_state(Form.name)

    await message.answer(text=TEXT_REST, reply_markup=ReplyKeyboardRemove())
    await message.answer(text=TEXT_NAME)

if __name__ == '__main__':
    dp.run_polling(bot)