
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
import random
import qrcode
from dotenv import load_dotenv

load_dotenv()

bot = Bot(os.getenv('TOKEN'))

 




import keabord as kb
import database_two as db_code
# Создаем объект бота

# Создаем диспетчер
dp = Dispatcher()

db = sqlite3.connect('animals.db', timeout=2)
c = db.cursor()





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
    await callback.message.delete()
    await Tiger(callback)
                                  
@dp.callback_query(F.data == 'back_menu_tiger')#возвращает в меню
async def Tiger_back_to_menu(callback: CallbackQuery):
    await callback.message.delete()
    await callback.answer('Вы ыернулись в меню')
    await start(callback.message)





@dp.callback_query(F.data == 'slon')#описание слона
async def Slon(callback: CallbackQuery):
    await callback.message.delete()
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
    await callback.message.delete()
    await Slon(callback)

@dp.callback_query(F.data == 'back_menu_slon')#возвращение в меню
async def Slon_back_to_menu(callback: CallbackQuery):
    await callback.message.delete()
    await callback.answer('Вы вернулись в меню')
    await start(callback.message)


@dp.callback_query(F.data == 'begemot')
async def Begemot(callback: CallbackQuery):
    await callback.message.delete()
    photo_path = animal[7]
    await callback.answer()
    await callback.message.answer_photo(photo=types.FSInputFile(
        path=photo_path), caption="*" + animal[2] + "*", parse_mode="Markdown", reply_markup=kb.begemot)

@dp.callback_query(F.data == 'gues_begemot')#вальер слона
async def Begemot_gues(callback: CallbackQuery):
    await callback.message.delete()
    photo_path = animal[20]
    await callback.answer()
    await callback.message.answer_photo(photo=types.FSInputFile(
        path=photo_path), caption="*" + animal[16] + "*", parse_mode="Markdown", reply_markup=kb.begemot_back)

@dp.callback_query(F.data == 'time_begemot')#время нахождения слона
async def Begemot_time(callback: CallbackQuery):
    await callback.message.delete()
    photo_path = animal[10]
    await callback.answer()
    await callback.message.answer_photo(photo=types.FSInputFile(
        path=photo_path), caption="*" + animal[13] + "*", parse_mode="Markdown", reply_markup=kb.begemot_back)
    
@dp.callback_query(F.data == 'begemot_back')#возвращение к слону
async def Begemot_back(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.delete()
    await Begemot(callback)

@dp.callback_query(F.data == 'back_menu_begemot')#возвращение в меню
async def Begemot_back_to_menu(callback: CallbackQuery):
    await callback.message.delete()
    await callback.answer('Вы вернулись в меню')
    await start(callback.message)



    
@dp.callback_query(F.data == 'leniv')
async def Leniv(callback: CallbackQuery):
    await callback.message.delete()
    photo_path = animal[8]
    await callback.answer()
    await callback.message.answer_photo(photo=types.FSInputFile(
        path=photo_path
    ))
    await callback.message.answer("*" + animal[3] + "*", parse_mode="Markdown", reply_markup=kb.leniv)

@dp.callback_query(F.data == 'gues_leniv')#вальер слона
async def leniv_gues(callback: CallbackQuery):
    await callback.message.delete()
    await callback.answer()
    await callback.message.answer("*" + animal[17] + "*", parse_mode="Markdown", reply_markup=kb.leniv_back)

@dp.callback_query(F.data == 'time_leniv')#время нахождения ленивца
async def leniv_time(callback: CallbackQuery):
    await callback.message.delete()
    photo_path = animal[10]
    await callback.answer()
    await callback.message.answer_photo(photo=types.FSInputFile(
        path=photo_path), caption="*" + animal[13] + "*", parse_mode="Markdown", reply_markup=kb.leniv_back)
    
@dp.callback_query(F.data == 'leniv_back')#возвращение к ленивцу
async def leniv_back(callback: CallbackQuery):
    await callback.message.delete()
    await Leniv(callback)

@dp.callback_query(F.data == 'back_menu_leniv')#возвращение в меню
async def leniv_back_to_menu(callback: CallbackQuery):
    await callback.message.delete()
    await callback.answer('Вы вернулись в меню')
    await start(callback.message)



@dp.callback_query(F.data == 'giraffe')
async def Giraffe(callback: CallbackQuery):
    await callback.message.delete()
    photo_path= animal[9]
    await callback.answer()
    await callback.message.answer_photo(photo=types.FSInputFile(
        path=photo_path
    ))
    await callback.message.answer("*" + animal[4] + "*", parse_mode="Markdown", reply_markup=kb.giraffe)

@dp.callback_query(F.data == 'gues_giraffe')#вальер жирафа
async def giraffe_gues(callback: CallbackQuery):
    await callback.message.delete()
    await callback.answer()
    photo_path = animal[19]
    await callback.message.answer_photo(photo=types.FSInputFile(
        path=photo_path), caption="*" + animal[18] + "*", parse_mode="Markdown", reply_markup=kb.giraffe_back)
    

@dp.callback_query(F.data == 'time_giraffe')#время нахождения жирафа
async def giraffe_time(callback: CallbackQuery):
    await callback.message.delete()
    photo_path = animal[10]
    await callback.answer()
    await callback.message.answer_photo(photo=types.FSInputFile(
        path=photo_path), caption="*" + animal[13] + "*", parse_mode="Markdown", reply_markup=kb.giraffe_back)
    
@dp.callback_query(F.data == 'giraffe_back')#возвращение к жирафа   
async def giraffe_back(callback: CallbackQuery):
    await callback.message.delete()
    await Giraffe(callback)

@dp.callback_query(F.data == 'back_menu_giraffe')#возвращение в меню
async def giraffe_back_to_menu(callback: CallbackQuery):
    await callback.message.delete()
    await callback.answer('Вы вернулись в меню')
    await start(callback.message)


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




async def create_and_send_qr(answer: str, types_ticket: str, message: types.Message):
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    now = datetime.now()
    folder_path = r'\vscode rep\zoo\zoo\photo_qrode'
    timestamp = now.strftime("%Y%m%d_%H%M%S")
    filename = f"qr_{timestamp}.jpg"
    qr.add_data(answer)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    file_path = os.path.join(folder_path, filename)
    img.save(file_path, 'JPEG')
    await message.answer(answer)
    await message.answer_photo(photo=types.FSInputFile(file_path))
    user_id = message.from_user.id
    await db_code.update_user_qr_code(user_id, file_path, answer)
    
       


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
    
    await create_and_send_qr(answer, 'взрослый', message)
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
    
    await create_and_send_qr(answer, 'детский', message)
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
    
    await create_and_send_qr(answer, 'детский', message)
    await state.clear()

@dp.message(F.text == 'Мои билеты')
async def my_ticket(message: Message):
    await message.answer('Вы хотите получить последний билет или все сразу?', reply_markup=kb.type_my_ticket)




@dp.callback_query(F.data == 'all')#получение всех билетов
async def get_qr_all(callback: CallbackQuery):
    await callback.answer()
    db = sqlite3.connect('qr.db')
    c = db.cursor()
    tg_id = callback.from_user.id
    c.execute('SELECT qr_code, qr_code_info FROM qrcode WHERE tg_id = ?', (tg_id,))
    results = c.fetchall()  

    if not results:
        await callback.message.answer("У вас нет билетов.")
        return

    for qr_code, qr_code_info in results:
        photo_path = os.path.join(os.getcwd(), r'vscode repzoozoophoto_qrode', qr_code) 
        
        print(f"Проверяем файл: {photo_path}") 
        
        if os.path.exists(photo_path):
            await callback.message.answer_photo(photo=types.FSInputFile(photo_path), caption=qr_code_info)  
        else:
            await callback.message.answer(f"Ошибка: файл {photo_path} не найден.")


@dp.callback_query(F.data == 'last')#получение последнего билета
async def get_qr_last(callback: CallbackQuery):
    await callback.answer()
    db = sqlite3.connect('qr.db', timeout=2)
    c = db.cursor()
    tg_id = callback.from_user.id
    
    query = """
    SELECT qr_code, qr_code_info FROM qrcode
    WHERE tg_id = ? 
    ORDER BY id DESC 
    LIMIT 1
    """
    
    c.execute(query, (tg_id,))
    result = c.fetchone()  #

    if result: 
        qr_code, qr_code_info = result   
        photo_path = os.path.join(os.getcwd(), r'vscode repzoozoophoto_qrode', qr_code) 
        
        print(f"Проверяем файл: {photo_path}")

        await callback.message.answer_photo(photo=types.FSInputFile(photo_path), caption=qr_code_info)
    else:
        await callback.message.answer("QR код не найден.")


    






    
    
if __name__ == '__main__':
    asyncio.run(dp.start_polling(bot))