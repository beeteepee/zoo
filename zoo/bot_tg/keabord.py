from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

main = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='Тигр', callback_data='tiger'),
        InlineKeyboardButton(text='Слон', callback_data='slon')
    ],
    [
        InlineKeyboardButton(text='Бегемот', callback_data='begemot'),
        InlineKeyboardButton(text='Ленивец', callback_data='leniv'),
        InlineKeyboardButton(text='Жираф', callback_data='giraffe')
    ]
])


tiger = InlineKeyboardMarkup(inline_keyboard=[
    
    [InlineKeyboardButton(text='Расписание', callback_data='time'),
    InlineKeyboardButton(text='Место обитания', callback_data='gues')],
    [InlineKeyboardButton(text='Назад', callback_data='back_menu_tiger')]
])

tiger_back = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Назад', callback_data='back_tiger')]
])

slon = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Расписание', callback_data='time_slon'),
    InlineKeyboardButton(text='Место обитания', callback_data='gues_slon')],
    [InlineKeyboardButton(text='Назад', callback_data='back_menu_slon')]
])


slon_back = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Назад', callback_data='back_slon')]
])


buy = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Покупка билетов')]
],
resize_keyboard=True
)

type_ticket = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Только взрослый', callback_data='big'), InlineKeyboardButton(text='Только детский', callback_data='small')],
    [InlineKeyboardButton(text= 'Взрослый и детский', callback_data='big_and_small')]
])