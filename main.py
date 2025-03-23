import asyncio
from aiogram import Bot, Dispatcher

from app.handlers import router

async def main():
    bot = Bot(token='8062754523:AAFD-voY39Qmo9450AqeAJWLyNO0X9z6A34')
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
