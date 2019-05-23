import sqlite3
conn = sqlite3.connect('swimkids.db')
c = conn.cursor()

c.execute('''CREATE TABLE skills
             (id integer not null primary key, level text, standard text, stroke text, skill text, 
             stamina boolean, focus boolean, confidence boolean, head boolean, body boolean, legs boolean, arms boolean)''')

c.execute('''CREATE TABLE comments
             (id integer not null primary key, sentiment text, comment text)''')

c.execute('''CREATE TABLE directory
             (attr_id int, comment_id int, foreign key (attr_id) references skills(id), 
             foreign key (comment_id) references comments(id))''')

conn.close()