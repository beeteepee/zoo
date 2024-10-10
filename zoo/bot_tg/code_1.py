import os
import asyncio
import sqlite3
from aiogram import types
from aiogram import F, Bot, Dispatcher
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.types import InputFile
from aiogram.enums import ParseMode
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram import types
from aiogram.types import CallbackQuery
from datetime import datetime
from datetime import time
import qrcode
import random

API_TOKEN = '7308111652:AAGFNTaxBFebMaW5YnljR44Ph3aaS2jw0Wg'

import keabord as kb
# Создаем объект бота
bot = Bot(token=API_TOKEN)

# Создаем диспетчер
dp = Dispatcher()

db = sqlite3.connect('animals.db')
db_2 = sqlite3.connect('qr.db')

c = db.cursor()
cd = db_2.cursor()



c.execute('SELECT * FROM animals')
animal = c.fetchone()


class reg(StatesGroup):
    first_big = State()
    first_small = State()
    first_big_and_small = State()
    second_big_and_small = State()

    


# Функция для получения данных о животном по id 
@dp.message(Command(commands=['start', 'menu']))
async def start (message: Message):
    await message.answer(text='Привет! Выбери животное.', reply_markup=kb.main)
    await message.answer(text='Так же вы можете купить билеты.', reply_markup=kb.buy)




@dp.callback_query(F.data == 'tiger')#описание тигра
async def Tiger(callback: CallbackQuery):
    await callback.message.delete()
    photo_path = animal[5]
    await callback.answer()
    await callback.message.answer_photo(photo=types.FSInputFile(
        path=photo_path), caption=f"*{animal[0]}*", parse_mode="Markdown", reply_markup=kb.tiger )
    
@dp.callback_query(F.data == 'gues')#вальер тигра
async def Tiger_gues(callback: CallbackQuery):
    await callback.message.delete()
    photo_path = animal[11]
    await callback.answer()
    await callback.message.answer_photo(photo=types.FSInputFile(
        path=photo_path), caption="*" + animal[12] + "*", parse_mode="Markdown", reply_markup=kb.tiger_back )

@dp.callback_query(F.data == 'time')#время нахождния тигра
async def Tiger_time(callback: CallbackQuery):
    photo_path = animal[10]
    await callback.message.delete()
    await callback.answer()
    await callback.message.answer_photo(photo=types.FSInputFile(
        path=photo_path), caption="*" + animal[13] + "*", parse_mode="Markdown",reply_markup=kb.tiger_back)

@dp.callback_query(F.data == 'back_tiger')# возвращает описание о тигре 
async def Tiger_back(callback: CallbackQuery):
    await Tiger(callback)
                                  
@dp.callback_query(F.data == 'back_menu_tiger')#возвращает в меню
async def Tiger_back_to_menu(callback: CallbackQuery):
    await callback.answer('Вы ыернулись в меню')
    await start(callback.message)





@dp.callback_query(F.data == 'slon')#описание слона
async def Slon(callback: CallbackQuery):
    photo_path = animal[6]
    await callback.answer()
    await callback.message.answer_photo(photo=types.FSInputFile(
        path=photo_path), caption="*" + animal[1] + "*", parse_mode="Markdown", reply_markup=kb.slon)

@dp.callback_query(F.data == 'gues_slon')#вальер слона
async def Slon_gues(callback: CallbackQuery):
    await callback.message.delete()
    photo_path = animal[14]
    await callback.answer()
    await callback.message.answer_photo(photo=types.FSInputFile(
        path=photo_path), caption="*" + animal[15] + "*", parse_mode="Markdown", reply_markup=kb.slon_back)

@dp.callback_query(F.data == 'time_slon')#время нахождения слона
async def Slon_time(callback: CallbackQuery):
    await callback.message.delete()
    photo_path = animal[10]
    await callback.answer()
    await callback.message.answer_photo(photo=types.FSInputFile(
        path=photo_path), caption="*" + animal[13] + "*", parse_mode="Markdown", reply_markup=kb.slon_back)
    
@dp.callback_query(F.data == 'back_slon')#возвращение к слону
async def Slon_back(callback: CallbackQuery):
    await Slon(callback)

@dp.callback_query(F.data == 'back_menu_slon')#возвращение в меню
async def Slon_back_to_menu(callback: CallbackQuery):
    await callback.answer('Вы вернулись в меню')
    await start(callback.message)


@dp.callback_query(F.data == 'begemot')
async def Begemot(callback: CallbackQuery):
    photo_path = animal[7]
    await callback.answer()
    await callback.message.answer_photo(photo=types.FSInputFile(
        path=photo_path
    ))
    await callback.message.answer("*" + animal[2] + "*", parse_mode="Markdown")
    
@dp.callback_query(F.data == 'leniv')
async def Leniv(callback: CallbackQuery):
    photo_path = animal[8]
    await callback.answer()
    await callback.message.answer_photo(photo=types.FSInputFile(
        path=photo_path
    ))
    await callback.message.answer("*" + animal[3] + "*", parse_mode="Markdown")

@dp.callback_query(F.data == 'giraffe')
async def Giraffe(callback: CallbackQuery):
    photo_path= animal[9]
    await callback.answer()
    await callback.message.answer_photo(photo=types.FSInputFile(
        path=photo_path
    ))
    await callback.message.answer("*" + animal[4] + "*", parse_mode="Markdown")


@dp.message(F.text == 'Покупка билетов')
async def buy_1(message: Message):
    today = datetime.now()
    day_of_week = today.weekday()
    days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
    if day_of_week == 6:
        await message.answer(f'Cегодня воскресенье, скидка на билеты 30% !')
    elif day_of_week == 3:
        await message.answer(f'Сегодня четверг, скидка на билеты 15% !')
    else:
        await message.answer('По четвергам и воскресеньям действуют скидки!')
    
    await message.answer(text='Пожалуйста, выберите тип билетов.', reply_markup=kb.type_ticket)





async def create_and_send_qr(answer: str, code_number: str, message: types.Message):
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    now = datetime.now()
    timestamp = now.strftime("%Y%m%d_%H%M%S")
    filename = f"qr_{timestamp}.jpg"
    qr.add_data(answer, code_number)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename, 'JPEG')
    await message.answer(answer)
    await message.answer_photo(photo=types.FSInputFile(filename))
    if os.path.exists(filename):
        os.remove(filename)


@dp.callback_query(F.data == 'big')
async def ticket(callback:CallbackQuery, state: FSMContext):
    await state.set_state(reg.first_big)
    await callback.answer()
    await callback.message.answer('Сколько билетов вы хотите взять?')

@dp.message(reg.first_big)
async def reg_ticket(message: Message, state: FSMContext):
    await state.update_data(first=message.text)
    data = await state.get_data()
    one = data['first']
    now = datetime.now()
    day, month, current_time = now.day, now.month, now.strftime("%H:%M:%S")
    answer = (f'Билет куплен {day}.{month} в {current_time}.\n'
              f'Кол-во билетов {one}, тип: взрослый')
    
    await create_and_send_qr(answer, 'взрослый', code_number, message)
    await state.clear()


@dp.callback_query(F.data == 'small')
async def ticket(callback: CallbackQuery, state: FSMContext):
    await state.set_state(reg.first_small)
    await callback.answer()
    await callback.message.answer('Сколько билетов вы хотите взять?')

@dp.message(reg.first_small)
async def reg_ticket(message: Message, state: FSMContext):
    await state.update_data(first=message.text)
    data = await state.get_data()
    one = data['first']
    now = datetime.now()
    day, month, current_time = now.day, now.month, now.strftime("%H:%M:%S")

    answer = (f'Билет куплен {day}.{month} в {current_time}.\n'
              f'Кол-во билетов {one}, тип: детский')
    
    await create_and_send_qr(answer, 'детский', code_number, message)
    await state.clear()


@dp.callback_query(F.data == 'big_and_small')
async def ticket(callback: CallbackQuery, state: FSMContext):
    await state.set_state(reg.first_big_and_small)
    await callback.answer()
    await callback.message.answer("Сколько билетов типа 'взрослый' вы хотите взять?.")

@dp.message(reg.first_big_and_small)
async def reg_ticket(message: Message, state: FSMContext):
    await state.update_data(first=message.text)
    await state.set_state(reg.second_big_and_small)
    await message.answer("Сколько билетов типа 'детский' вы хотите взять?.")

@dp.message(reg.second_big_and_small)
async def reg_ticket_second(message: Message, state: FSMContext):
    await state.update_data(second=message.text)
    data = await state.get_data()
    one = data['first']
    two = data['second']
    now = datetime.now()
    day, month, current_time = now.day, now.month, now.strftime("%H:%M:%S")

    answer = (f'Билет куплен {day}.{month} в {current_time}.\n'
              f'Кол-во билетов {one}, тип: взрослый; кол-во {two}, тип: детский')
    
    await create_and_send_qr(answer, 'детский', code_number, message)
    await state.clear()
        
    






    
    
if __name__ == '__main__':
    asyncio.run(dp.start_polling(bot))