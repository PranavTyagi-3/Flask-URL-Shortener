import sqlite3
conn=sqlite3.connect('urlbase.db')
conn.executescript('''drop table if exists urls;
create table urls(
    id integer primary key autoincrement,
    original_url text not null,
    short_url text not null,
    clicks integer not null default 0
);''')
conn.commit()
conn.close()
