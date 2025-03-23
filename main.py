import asyncio
import os
from aiogram import Bot, Dispatcher
from app.handlers import router

# Получаем токен из переменной окружения для безопасности (советую для Render)
TOKEN = os.getenv('BOT_TOKEN', '8062754523:AAFD-voY39Qmo9450AqeAJWLyNO0X9z6A34')  # Для локального запуска можешь временно вставить токен сюда

async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()
    dp.include_router(router)
    print("Bot is starting...")  # Для проверки в логах Render
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
