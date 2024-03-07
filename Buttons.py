from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

List_total_buttons = [[KeyboardButton(text="ДА🤝")], [KeyboardButton(text="НЕТ❌")]]
Total_buttons = ReplyKeyboardMarkup(keyboard=List_total_buttons, resize_keyboard=True, input_field_placeholder="")

list_TEXT_END = [[KeyboardButton(text="ДА, хочу, обсуждал/обсуждала с родителями🤩")], [KeyboardButton(text="ДА, но не обсуждал/обсуждала с родителями😎")], [KeyboardButton(text="Не знаю🤷‍♂️")], [KeyboardButton(text="НЕТ, не хотел/хотела бы😢")], [KeyboardButton(text="Что такое Singularity Hub?🧐")]]
One_buttons = ReplyKeyboardMarkup(keyboard=list_TEXT_END, resize_keyboard=True)

three_button = [[KeyboardButton(text="Да, хочу в образовательный центр 🏆")], [KeyboardButton(text="Да, хочу в IT-колледж 👨‍💻")], [KeyboardButton(text="Нет⛔️")]]
THREE_BUTTONS = ReplyKeyboardMarkup(keyboard=three_button, resize_keyboard=True)