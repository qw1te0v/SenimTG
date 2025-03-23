import asyncio
from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
import datetime

import app.keyboards as kb


router = Router()

# Функция для записи сообщений в файл
async def log_message(message: Message):
    with open("messages_log.txt", "a", encoding="utf-8") as file:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{timestamp} @{message.from_user.username}: {message.text}\n")

@router.message(CommandStart())
async def start(message: Message):
    await log_message(message)  # Логируем сообщение
    await message.answer('Sigmo', reply_markup=kb.main)

#---------------------RU---------------------   

@router.message(F.text == 'Ru')
async def katalog(message: Message):
    await log_message(message)  # Логируем сообщение
    await message.answer('Выберите категорию', reply_markup=kb.rukatalog)

@router.message(F.text == 'Назад в Меню')
async def back_ru(message: Message):
    await log_message(message)
    await message.answer('Меню',reply_markup=kb.rukatalog)


@router.message(F.text == 'Цены')
async def price(message: Message):
    await log_message(message)
    await message.answer('Выберите категорию', reply_markup=kb.ruprice)

@router.message(F.text == 'Корпоративный сайт')
async def corporate(message: Message):
    await log_message(message)
    await message.answer('''Корпоративный сайт: 
                         
$790.0 
✔ Доступно на 1 год 
✔ Telegram BOT''')
    
@router.message(F.text == 'Премиум сайт')
async def corporate(message: Message):
    await log_message(message)
    await message.answer('''Премиум сайт: 
                         
$1000.0 
✔ Доступно на 2 год 
✔ Telegram BOT''')
    
@router.message(F.text == 'Интернет-магазин')
async def corporate(message: Message):
    await log_message(message)
    await message.answer('''Интернет-магазин: 
                         
$607.0 
✔ Доступно на 8 месяцев
✖ Telegram BOT''')
    
@router.message(F.text == 'О Нас')
async def about(message: Message):
    await log_message(message)
    await message.answer('''О нас:
    Разработчик: @Kuka0v, @a1tonmn
    Дизайнер: @Ser1k_kyzy_008, @thejetkiz9_en 
    Тестировщик: @Abylaihan_09 
    Специалист по безопасности: @munaitpas09
    Наставник: @zhasikk27''')

#---------------------ru---------------------

#---------------------EN---------------------

@router.message(F.text == 'En')
async def katalog(message: Message):
    await log_message(message)  # Логируем сообщение
    await message.answer('Choose a category', reply_markup=kb.enkatalog)

@router.message(F.text == 'Back to Menu')
async def back_en(message: Message):
    await log_message(message)
    await message.answer('Menu',reply_markup=kb.enkatalog)

@router.message(F.text == 'Prices')
async def price(message: Message):
    await log_message(message)
    await message.answer('Choose a category', reply_markup=kb.enprice)

@router.message(F.text == 'Corporate site')
async def corporate(message: Message):
    await log_message(message)
    await message.answer('''Corporate site:
$790.0
✔ Available for 1 year
✔ Telegram BOT''')
                         
@router.message(F.text == 'Premium site')
async def corporate(message: Message):
    await log_message(message)
    await message.answer('''Premium site:
$1000.0
✔ Available for 2 years
✔ Telegram BOT''')
                         
@router.message(F.text == 'Online store')
async def corporate(message: Message):
    await log_message(message)
    await message.answer('''Online store:
$607.0
✔ Available for 8 months
✖ Telegram BOT''')

@router.message(F.text == 'About Us')
async def about(message: Message):
    await log_message(message)
    await message.answer('''About us:
    Developer: @Kuka0v, @a1tonmn
    Designer: @Ser1k_kyzy_008, @thejetkiz9_en 
    Tester: @Abylaihan_09 
    Security Specialist: @munaitpas09
    Mentor: @zhasikk27''')



#---------------------en---------------------

#---------------------KZ---------------------
@router.message(F.text == 'Kz')
async def katalog(message: Message):
    await log_message(message)
    await message.answer('Категорияны таңдаңыз', reply_markup=kb.kzkatalog)

@router.message(F.text == 'Менюге қайту')
async def back_kz(message: Message):
    await log_message(message)
    await message.answer('Меню',reply_markup=kb.kzkatalog)

@router.message(F.text == 'Біз туралы')
async def about(message: Message):
    await log_message(message)
    await message.answer('''О нас:
    Разработчик: @Kuka0v, @a1tonmn
    Дизайнер: @Ser1k_kyzy_008, @thejetkiz9_en 
    Тестировщик: @Abylaihan_09 
    Специалист по безопасности: @munaitpas09
    Наставник: @zhasikk27''')

@router.message(F.text == 'Бағалар')
async def price(message: Message):
    await log_message(message)
    await message.answer('Категорияны таңдаңыз', reply_markup=kb.kzprice)

@router.message(F.text == 'Корпоративті сайт')
async def corporate(message: Message):
    await log_message(message)
    await message.answer('''Корпоративті сайт:
$790.0
✔ 1 - Жыл қол жетімді
✔ Telegram BOT''')
    
@router.message(F.text == 'премиум сайт')
async def prem(message: Message):
    await log_message(message)
    await message.answer('''Премиум сайт:
$1000.0
✔ 2 жыл қол жетімді
✔ Telegram BOT''')
    
@router.message(F.text == 'Интернет-дүкен')
async def store(message: Message):
    await log_message(message)
    await message.answer('''Интернет-дүкен:'
$607.0
✔ 8 ай қол жетімді
✖ Telegram BOT''')



# Логируем все остальные сообщения
@router.message()
async def log_all_messages(message: Message):
    await log_message(message)  # Логируем сообщение
