import asyncio
from aiogram import Bot, Dispatcher
from aiohttp import web

from app.handlers import router

# Telegram Bot токен
API_TOKEN = '8062754523:AAFD-voY39Qmo9450AqeAJWLyNO0X9z6A34'

# Создание aiohttp веб-сервера
async def handle(request):
    return web.Response(text="Bot is alive!")

async def main():
    bot = Bot(token=API_TOKEN)
    dp = Dispatcher()
    dp.include_router(router)

    # Создание aiohttp приложения
    app = web.Application()
    app.router.add_get('/', handle)  # Для проверки UptimeRobot
    
    # Запускаем Telegram Bot в отдельной задаче
    loop = asyncio.get_running_loop()
    loop.create_task(dp.start_polling(bot))

    # Запускаем веб-сервер
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, port=8080)
    await site.start()
    
    print("Bot and web server started...")

    # Чтобы приложение не завершалось
    await asyncio.Event().wait()

if __name__ == '__main__':
    asyncio.run(main())
