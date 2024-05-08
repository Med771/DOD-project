from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.types import FSInputFile

from data import *
from Buttons import *
from functions import *

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

class value_Feedback(StatesGroup):
    f_one, f_two, f_three, f_four, f_five, f_end = [State() for _ in range(6)]  # f - feedback

class report(StatesGroup):
    ...

@dp.message(Command(commands="start"), F.text)
async def start_bot(message: Message, state: FSMContext) -> None:
    if check_regist(str(message.chat.id)):
        await message.answer(text=TEXT_START, reply_markup=ReplyKeyboardRemove())
        await message.answer(text=TEXT_NAME)
        await state.clear()
        await state.set_state(Form.name)
    else:
        await message.answer(text=TEXT_RST)

    print(message.chat.id)

@dp.message(Command(commands="file"), F.text)
async def command_file(msg: Message):
    table = FSInputFile("Data.xlsx", filename="Data.xlsx")

    await msg.answer_document(document=table)

'''@dp.message(Command(commands="feedback"), F.text)
async def command_feedback(msg: Message):'''

@dp.message(Form.name, F.text)
async def query_name(msg: Message, state: FSMContext) -> None:
    if check_name(msg.text):
        await state.update_data(name=msg.text)
        await state.set_state(Form.mail)

        await msg.answer(text=TEXT_EMAIL)
    else:
        await msg.answer(text=TEXT_ANSWER)

@dp.message(Form.mail, F.text)
async def query_mail(message: Message, state: FSMContext) -> None:
    await state.update_data(mail=message.text)
    await state.set_state(Form.number_phone)

    await message.answer(text=TEXT_NUMBER)

@dp.message(Form.number_phone, F.text)
async def query_num_phone(msg: Message, state: FSMContext) -> None:
    if check_num_phone(msg.text):
        await state.update_data(number_phone=msg.text)
        await state.set_state(Form.school)

        await msg.answer(text=TEXT_SCHOOL)
    else:
        await msg.answer(text=TEXT_ANSWER)

@dp.message(Form.school, F.text)
async def query_school(msg: Message, state: FSMContext) -> None:
    if check_school(msg.text):
        await state.update_data(school=msg.text)
        await state.set_state(Form.class_school)

        await msg.answer(text=TEXT_CLASS)
    else:
        await msg.answer(text=TEXT_ANSWER)

@dp.message(Form.class_school, F.text)
async def query_class(msg: Message, state: FSMContext) -> None:
    if check_class(msg.text):
        await state.update_data(class_school=msg.text)
        await state.set_state(Form.parent_name)

        await msg.answer(text=TEXT_NAME_PARENTS)
    else:
        await msg.answer(text=TEXT_ANSWER)

@dp.message(Form.parent_name, F.text)
async def query_parent_name(msg: Message, state: FSMContext) -> None:
    if check_name(msg.text):
        await state.update_data(parent_name=msg.text)
        await state.set_state(Form.number_parents)

        await msg.answer(text=TEXT_NUMBER_PARENTS)
    else:
        await msg.answer(text=TEXT_ANSWER)

@dp.message(Form.number_parents, F.text)
async def query_number_parents(msg: Message, state: FSMContext) -> None:
    if check_num_phone(msg.text):
        await state.update_data(number_parents=msg.text)
        await state.set_state(Form.one_issue)

        await msg.answer(text=TEXT_NEXT, reply_markup=Total_buttons)
    else:
        await msg.answer(text=TEXT_ANSWER)

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
async def registration(message: Message, state: FSMContext):
    data = await state.update_data(regestration="OK")
    arr = [data["name"], data["mail"], message.from_user.username, data["number_phone"], data["school"], data["class_school"], data["parent_name"], data["number_parents"], data["one_issue"], data["two_issue"], data["three_issue"]]

    append_id_number(message.chat.id)
    append_full_info_in_xlsx(arr)

    await state.clear()
    await state.set_state(value_Feedback.f_one)
    await message.answer(text=TEXT_MAIN_FEEEDBACK, reply_markup=FEEDBACK_BUTTON, parse_mode="HTML")

@dp.message(Form.registration, F.text == "НЕТ❌")
async def not_registration(message: Message, state: FSMContext) -> None:
    await state.clear()
    await state.set_state(Form.name)

    await message.answer(text=TEXT_REST, reply_markup=ReplyKeyboardRemove())
    await message.answer(text=TEXT_NAME)

@dp.message(value_Feedback.f_one, F.text == "Оставить обратную связь")
async def one_feedback(msg: Message, state: FSMContext) -> None:
    await state.set_state(value_Feedback.f_two)

    await msg.answer(text=TEXT_ANSWER_FEEDBACK)
    await msg.answer(text=TEXT_FEEDBACK_ONE, reply_markup=FEEDBACK_BUTTONS)

@dp.message(value_Feedback.f_two, F.text)
async def two_feedback(msg: Message, state: FSMContext) -> None:
    await state.update_data(Feedback_one=msg.text)
    await state.set_state(value_Feedback.f_three)

    await msg.answer(text=TEXT_FEEDBACK_TWO)

@dp.message(value_Feedback.f_three, F.text)
async def three_feedback(msg: Message, state: FSMContext) -> None:
    await state.update_data(Feedback_two=msg.text)
    await state.set_state(value_Feedback.f_four)

    await msg.answer(text=TEXT_FEEDBACK_THREE)

@dp.message(value_Feedback.f_four, F.text)
async def four_feedback(msg: Message, state: FSMContext) -> None:
    await state.update_data(Feedback_three=msg.text)
    await state.set_state(value_Feedback.f_five)

    await msg.answer(text=TEXT_FEEDBACK_FOUR)

@dp.message(value_Feedback.f_five, F.text)
async def five_feedback(msg: Message, state: FSMContext) -> None:
    await state.update_data(Feedback_four=msg.text)
    await state.set_state(value_Feedback.f_end)

    await msg.answer(text=TEXT_FEEDBACK_FIVE, reply_markup=ReplyKeyboardRemove())

@dp.message(value_Feedback.f_end, F.text)
async def end_feedback(msg: Message, state: FSMContext) -> None:
    data = await state.update_data(Feedback_five=msg.text)

    arr = [data["Feedback_one"],
           data["Feedback_two"],
           data["Feedback_three"],
           data["Feedback_four"],
           data["Feedback_five"]]

    append_in_Feedback_file(arr)

    await state.clear()
    await msg.answer(text=TEXT_END_FEEDBACK, reply_markup=ReplyKeyboardRemove())

if __name__ == '__main__':
    dp.run_polling(bot)
