from aiohttp import web
import asyncio
from aiogram import Bot, Dispatcher
from app.handlers import router

async def handle(request):
    return web.Response(text="Bot is running!")

async def main():
    bot = Bot(token='ТВОЙ_ТОКЕН')
    dp = Dispatcher()
    dp.include_router(router)

    # aiohttp server
    app = web.Application()
    app.router.add_get("/", handle)  # отвечает UptimeRobot
    
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, port=8080)
    await site.start()
    
    # запускаем бота
    loop = asyncio.get_running_loop()
    loop.create_task(dp.start_polling(bot))

    print("Bot and server started!")

    await asyncio.Event().wait()

if __name__ == '__main__':
    asyncio.run(main())