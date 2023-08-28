import config
import const

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor


bot = Bot(config.TOKEN_BOT)
dp = Dispatcher(bot)


def main():
    executor.start_polling(dp, skip_updates=True)


# Начало, реагирование на команду start

@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.answer(f'Игра началась. Первый говорит {message.from_user.first_name}!')


# Проверка сколько городов уже было использовано

@dp.message_handler(commands='check')
async def check(message: types.Message):

    count = len(const.USED_CITIES)

    if count == 0:
        await message.answer('На данный момент нет ни одного города... Играйте уже!')
    elif count == 1:
        await message.answer(f'На данный момент назван {count} город.')
    elif count >= 5:
        await message.answer(f'На данный момент названо {count} городов.')
    elif count < 5:
        await message.answer(f'На данный момент названо {count} города.')


# Основная игра

@dp.message_handler()
async def game(message: types.Message):

    msg = message.text
    msg = msg.upper()

    # Проверка на использование ранее этого города
    if msg in const.USED_CITIES:
        await message.answer(f'Город {msg} уже был в этой игре.')
        
    elif msg not in const.USED_CITIES:

        const.USED_CITIES.append(msg)
        letter = list(msg)

        # Проверка на буквы, к которым невозможно подобрать город
        if letter[-1] in const.NO_CHANCE_LETTER:
            await message.answer(f'Следующему игроку город на букву: {letter[-2]}')
        else:
            await message.answer(f'Следующему игроку город на букву: {letter[-1]}')


if __name__ == '__main__':
    main()
