import sqlite3

con = sqlite3.connect("file.db")
cur = con.cursor()
d = {}
m = []

cur.execute('''
CREATE TABLE IF NOT EXISTS Songs (
id INTEGER PRIMARY KEY,
name TEXT NOT NULL,
link TEXT NOT NULL
)
''')
con.commit()


async def add_song(song_name, idx):
    if song_name in m:
        return
    m.append(song_name)
    d[song_name]=idx
    cur.execute('INSERT INTO Songs (name, link) VALUES (?, ?)',
                   (song_name, idx))
    con.commit()


async def get_songs():
    global m, d
    cur.execute('SELECT * FROM Songs')
    a = cur.fetchall()
    print(a)
    for i in range(len(a)):
        d[a[i][1]]=a[i][2]
        m.append(a[i][1])
    print(d,m)

