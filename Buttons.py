from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

List_total_buttons = [[KeyboardButton(text="ДА🤝")],
                      [KeyboardButton(text="НЕТ❌")]]
Total_buttons = ReplyKeyboardMarkup(keyboard=List_total_buttons, resize_keyboard=True, input_field_placeholder="")

list_TEXT_END = [[KeyboardButton(text="ДА, хочу, обсуждал/обсуждала с родителями🤩")],
                 [KeyboardButton(text="ДА, но не обсуждал/обсуждала с родителями😎")],
                 [KeyboardButton(text="Не знаю🤷‍♂️")],
                 [KeyboardButton(text="НЕТ, не хотел/хотела бы😢")],
                 [KeyboardButton(text="Что такое Singularity Hub?🧐")]]
One_buttons = ReplyKeyboardMarkup(keyboard=list_TEXT_END, resize_keyboard=True)

three_button = [[KeyboardButton(text="Да, хочу в образовательный центр 🏆")],
                [KeyboardButton(text="Да, хочу в IT-колледж 👨‍💻")],
                [KeyboardButton(text="Нет⛔️")]]
THREE_BUTTONS = ReplyKeyboardMarkup(keyboard=three_button, resize_keyboard=True)

Feedback_buttons = [[KeyboardButton(text="1️⃣- очень плохо ")],
                    [KeyboardButton(text="2️⃣- плохо")],
                    [KeyboardButton(text="3️⃣- неплохо, но есть над чем поработать")],
                    [KeyboardButton(text="4️⃣- все супер")],
                    [KeyboardButton(text="5️⃣- великолепно и лучше некуда")]]
FEEDBACK_BUTTONS = ReplyKeyboardMarkup(keyboard=Feedback_buttons, resize_keyboard=True)

button_for_feedback = [[KeyboardButton(text="Оставить обратную связь")]]
FEEDBACK_BUTTON = ReplyKeyboardMarkup(keyboard=button_for_feedback, resize_keyboard=True)
