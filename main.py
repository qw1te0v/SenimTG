from app import database
import asyncio
from aiogram import Bot, Dispatcher
from app.handlers import router
import os
from aiohttp import web

TOKEN = os.getenv("BOT_TOKEN") 

async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()
    dp.include_router(router)

    await database.init_db()

    asyncio.create_task(dp.start_polling(bot))

    async def handle(request):
        return web.Response(text="Bot is running!")

    app = web.Application()
    app.router.add_get("/", handle)

    runner = web.AppRunner(app)
    await runner.setup()
    port = int(os.environ.get("PORT", 8080))
    site = web.TCPSite(runner, port=port)
    await site.start()

    print(f"Bot and web server started on port {port}")
    while True:
        await asyncio.sleep(3600)

if __name__ == '__main__':
    asyncio.run(main())
