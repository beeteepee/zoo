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
    first = State()

class reg_two(StatesGroup):
    first_small = State()
    
class reg_three(StatesGroup):
    first_big_small = State()
    second = State()
    
    
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)


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




@dp.callback_query(F.data == 'big')
async def big_ticket(callback:CallbackQuery, state: FSMContext):
    await state.set_state(reg.first)
    await callback.answer()
    await callback.message.answer('Сколько билетов вы хотите взять?')

@dp.message(reg.first)
async def reg_ticket_big(message: Message, state: FSMContext):
        await state.update_data(first = message.text)
        now = datetime.now()
        day = now.day
        month = now.month
        current_time = now.strftime("%H:%M:%S")
        data = await state.get_data()
        number = data['first']
        answer = (f'Билет куплен {day}.{month} в {current_time}.\n'
                f'Кол-во билетов {number}, тип: взрослый')
        qr.add_data(answer)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        timestamp = now.strftime("%Y%m%d_%H%M%S")
        filename = f"qr_{timestamp}.jpg"
        img.save(filename, 'JPEG')
        
        cd.execute('''INSERT INTO qrcode (filename) VALUES (?)''', (filename,))


        await message.answer(answer)
        await message.answer_photo(photo=types.FSInputFile(filename))
        
        os.remove(filename)

        await state.clear()
        
        
@dp.callback_query(F.data == 'small')
async def small_ticket(callback:CallbackQuery, state: FSMContext):
    await state.set_state(reg_two.first_small)
    await callback.answer()
    await callback.message.answer('Сколько билетов вы хотите взять?')

@dp.message(reg_two.first_small)
async def reg_ticket_small(message: Message, state: FSMContext):
        await state.update_data(first = message.text)
        now = datetime.now()
        day = now.day
        month = now.month
        current_time = now.strftime("%H:%M:%S")
        data = await state.get_data()
        number = data['first']
        answer_2 = (f'Билет куплен {day}.{month} в {current_time}.\n'
                f'Кол-во билетов {number}, тип: детский')
        qr.add_data(answer_2)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        timestamp = now.strftime("%Y%m%d_%H%M%S")
        filename = f"qr_{timestamp}.jpg"
        img.save(filename, 'JPEG')
        
        cd.execute('''INSERT INTO qrcode (filename) VALUES (?)''', (filename,))


        await message.answer(answer_2)
        await message.answer_photo(photo=types.FSInputFile(filename))
        
        os.remove(filename)
        await state.clear()
    
    
@dp.callback_query(F.data == 'big_and_small')
async def big_small_ticket(callback:CallbackQuery, state: FSMContext):
    await state.set_state(reg_three.first_big_small)
    await callback.answer()
    await callback.message.answer(f"Сколько билетов типа 'взрослый' вы хотите взять?")
    
@dp.message(reg_three.first_big_small)
async def big_small_ticket_reg(message: Message, state: FSMContext):
    await state.set_state(reg_three.second)
    await state.update_data(first_big_small = message.text)
    await message.answer(f"Сколько билетов типа 'детский' вы хотите взять?")
    
    
    

@dp.message(reg_three.second)
async def reg_ticket(message: Message, state: FSMContext):
        await state.update_data(first = message.text)
        await state.update_data(second=message.text)
        now = datetime.now()
        day = now.day
        month = now.month
        current_time = now.strftime("%H:%M:%S")
        data = await state.get_data()
        number = data['first_big_small']
        number_2 = data['second']
        answer_3 = (f'Билет куплен {day}.{month} в {current_time}.\n'
                f'Кол-во билетов {number}, тип: взрослый; {number_2}, тип: детский')
        qr.add_data(answer_3)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        timestamp = now.strftime("%Y%m%d_%H%M%S")
        filename_3 = f"qr_{timestamp}.jpg"
        img.save(filename_3, 'JPEG')
        
        cd.execute('''INSERT INTO qrcode (filename) VALUES (?)''', (filename_3,))

        await message.answer(answer_3)
        await message.answer_photo(photo=types.FSInputFile(filename_3))
        await state.clear()
        
        os.remove(filename_3)

        
    






    
    
if __name__ == '__main__':
    asyncio.run(dp.start_polling(bot))