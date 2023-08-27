import config
import random

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot(config.TOKEN_BOT)
dp = Dispatcher(bot)
entry_city = random.choice(config.START_CITIES)

def main():
    executor.start_polling(dp, skip_updates=True)


@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.answer(f'Добро пожаловать к нам, {message.from_user.first_name}'),
                        ('Здесь мы играем в города! Я начинаю!'),
                        (f'Первый город это {entry_city}', )


@dp.message_handler(commands='start_game')
async def start_game(message: types.Message):
    pass


@dp.message_handler()
def game(message: types.Message):
    msg = message.text
    list(msg)
    list(entry_city)

    if msg[0] == entry_city[-1]:
        return message.answer('Молодец! Дальше Вы сами!')
    else:
        return message.answer('Давай.. заново что ли?')


if __name__ == '__main__':
    main()
