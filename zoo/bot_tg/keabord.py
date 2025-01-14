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

begemot = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Расписание', callback_data='time_begemot'),
    InlineKeyboardButton(text='Место обитания', callback_data='gues_begemot')],
    [InlineKeyboardButton(text='Назад', callback_data='back_menu_begemot')]
]
)
begemot_back = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Назад', callback_data='begemot_back')]])


leniv = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Расписание', callback_data='time_leniv'),
    InlineKeyboardButton(text='Место обитания', callback_data='gues_leniv')],
    [InlineKeyboardButton(text='Назад', callback_data='back_menu_leniv')]
])
leniv_back = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Назад', callback_data='leniv_back')]])


giraffe = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Расписание', callback_data='time_giraffe'),
    InlineKeyboardButton(text='Место обитания', callback_data='gues_giraffe')],
    [InlineKeyboardButton(text='Назад', callback_data='back_menu_giraffe')]
])
giraffe_back = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Назад', callback_data='giraffe_back')]])


buy = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Покупка билетов')],
    [KeyboardButton(text='Мои билеты')]
],
resize_keyboard=True
)

type_ticket = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Только взрослый', callback_data='big'), InlineKeyboardButton(text='Только детский', callback_data='small')],
    [InlineKeyboardButton(text= 'Взрослый и детский', callback_data='big_and_small')]
])

type_my_ticket = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Последний', callback_data='last'), InlineKeyboardButton(text='Все',callback_data='all')]
])