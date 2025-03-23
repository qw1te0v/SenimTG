import aiosqlite

DB_NAME = "users.db"

async def init_db():
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                username TEXT
            )
        ''')
        await db.execute('''
            CREATE TABLE IF NOT EXISTS messages (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                text TEXT,
                timestamp TEXT
            )
        ''')
        await db.commit()

async def add_user(user_id, username):
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute('INSERT OR IGNORE INTO users (id, username) VALUES (?, ?)', (user_id, username))
        await db.commit()

async def log_message(user_id, text, timestamp):
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute('INSERT INTO messages (user_id, text, timestamp) VALUES (?, ?, ?)', (user_id, text, timestamp))
        await db.commit()

async def get_users():
    async with aiosqlite.connect(DB_NAME) as db:
        async with db.execute('SELECT id, username FROM users') as cursor:
            return await cursor.fetchall()

async def get_messages():
    async with aiosqlite.connect(DB_NAME) as db:
        async with db.execute('SELECT user_id, text, timestamp FROM messages') as cursor:
            return await cursor.fetchall()
