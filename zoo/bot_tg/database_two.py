import sqlite3

db = sqlite3.connect('qr.db')


c = db.cursor()

c.execute('''
          CREATE TABLE IF NOT EXISTS qrcode (
              filename TEXT NOT NULL 
              
)
''')

db.commit()

c.close()



print('Данные загружены')