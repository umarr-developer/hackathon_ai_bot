from aiogram import Router, types
from aiogram.filters import Command
from src.service.openai import get_completetions

router = Router()


@router.message(Command(commands=['start']))
async def on_start(message: types.Message):
    text = f"""
    Привет, {message.from_user.full_name} Я здесь, чтобы помочь тебе получить всю необходимую информацию о хакатоне Latoken и самой компании. Я могу ответить на твои вопросы, касающиеся хакатона, рассказать о его целях и задачах, а также о том, как Latoken использует технологии и ИИ для демократизации рынков капитала. Если ты хочешь узнать больше о культуре компании или о том, как присоединиться к нашей команде, я тоже с радостью помогу!

<i>Если ознокомился всей информацией, советую пройти тест, которую можно запустить по команде /test или нажать кнопку ниже</i>
    """
    keyboard = types.ReplyKeyboardMarkup(
        resize_keyboard=True,
        keyboard=[[
            types.KeyboardButton(text='📒 Начать тест')]
        ]
    )
    await message.answer(text, reply_markup=keyboard)
