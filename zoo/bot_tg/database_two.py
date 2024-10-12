import sqlite3

db = sqlite3.connect('qr.db')


c = db.cursor()

c.execute('''
        CREATE TABLE IF NOT EXISTS qrcode (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        tg_id INTEGER,
        qr_code TEXT
              
)
''')



async def update_user_qr_code(user_id: int, qr_code_path: str):
    c.execute('INSERT INTO qrcode (tg_id, qr_code) VALUES (?, ?)', (user_id, qr_code_path))
    db.commit()




print('База данных qrcode подключена')