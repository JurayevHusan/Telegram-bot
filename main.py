import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from tools import search
from data import m, d, get_songs, add_song

bot = Bot(token="7580839075:AAFJztELLaaJSk88EWdZSqDXuYz6UX_5NL0")
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("Assalomu Aleykum!")

@dp.message(F.text)
async def search_song(message: types.Message):
    res = search(message.text)
    if len(res) != 0 and message.text in d[res[0][0]]:
        await message.answer_audio(d[res[0][0]])
    msg = ""
    buttons = [[],[]]
    for i in range(len(res)):
        percent = res[i][1]
        if percent < 30:
            break
        buttons[i//5].append(types.InlineKeyboardButton(
            text=str(i+1),
            callback_data=str(m.index(res[i][0]))
        ))
        msg += f"{i+1}. {res[i][0]}\n"
    if msg=="":
        msg="Hech narsa topilmadi :("
    builder = InlineKeyboardMarkup(inline_keyboard=[*buttons])
    await message.answer(msg, reply_markup=builder)

@dp.message(F.audio)
async def add_new_song(message: types.Message):
    name = message.audio.title
    idx = message.audio.file_id
    if message.audio.performer:
        name = message.audio.performer + " - " + name
    await add_song(name, idx)
    print(name, idx)

    @dp.message(F.voice)
    async def greetings(message: types.Message):
        await message.answer("Yashang Hofiz !")

@dp.message()
async def greetings(message: types.Message):
    await message.answer("O'zbekcha gapir")

@dp.callback_query()
async def callbacks_num(callback: types.CallbackQuery):
    await callback.answer("Hey")
    await callback.message.answer_audio(d[m[int(callback.data)]])

async def main():
    await get_songs()
    await dp.start_polling(bot)

asyncio.run(main())