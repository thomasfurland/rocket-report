import sqlite3
conn = sqlite3.connect('test.db')
c = conn.cursor()
c.execute('''CREATE TABLE skills
             (id integer not null primary key, level text, skill text, attribute text)''')

c.execute('''CREATE TABLE comments
             (id integer not null primary key, sentiment text, comment text)''')

c.execute('''CREATE TABLE directory
             (attr_id int, comment_id int, foreign key (attr_id) references skills(id), 
             foreign key (comment_id) references comments(id))''')

# c.execute("INSERT INTO skills(level, skill, attribute) VALUES ('level1','back_glide_5_seconds','completes_distance')")
# attr_id = c.lastrowid
# c.execute("INSERT INTO skills(level, skill, attribute) VALUES ('level2','back_glide_5_seconds','completes_distance')")
# c.execute("INSERT INTO skills(level, skill, attribute) VALUES ('salamander','back_glide_5_seconds','completes_distance')")
# c.execute("INSERT INTO comments(sentiment, comment) VALUES ('0', 'you suck kid!')")
# c.execute("INSERT INTO comments(sentiment, comment) VALUES ('0', 'you suck kid!')")
# comment_id = c.lastrowid

# c.execute("INSERT INTO skills_to_comments(attr_id, comment_id) VALUES (?, ?)", (attr_id, comment_id))

# for row in c.execute('SELECT * FROM skills'):
#     print(row)
# for row in c.execute('SELECT * FROM comments'):
#     print(row)
# for row in c.execute('SELECT * FROM skills_to_comments'):
#     print(row)

# conn.commit()
# conn.close()

def insert_comments(level, skill, attribute, sentiment, comment):
    c.execute("SELECT id FROM skills WHERE level = ? AND skill = ? AND attribute = ?", (level, skill, attribute))
    value = c.fetchone()
    if value == None:
        c.execute("INSERT INTO skills(level, skill, attribute) VALUES (?, ?, ?)", (level, skill, attribute))
        attr_id = c.lastrowid
    else:
        attr_id = value[0]
    c.execute("INSERT INTO comments(sentiment, comment) VALUES (?, ?)", (sentiment, comment))
    comment_id = c.lastrowid
    c.execute("INSERT INTO directory(attr_id, comment_id) VALUES (?, ?)", (attr_id, comment_id))
    conn.commit()
    return True


def select_comments(level, skill, attribute, sentiment):
    extraction = """SELECT skill, attribute, sentiment, comment 
        FROM skills INNER JOIN directory AS sc ON skills.id = sc.attr_id 
        INNER JOIN comments ON sc.comment_id = comments.id 
        WHERE level = ? AND skill = ? AND attribute = ? AND sentiment = ? """ 
    c.execute(extraction,[level, skill, attribute, sentiment])
    return c.fetchall()

insert_comments("level1", "back_glide", "streamlined_position", "0", "remember to keep your tummy up!")
insert_comments("level1", "back_glide", "streamlined_position", "1", "great work keeping your tummy up!")
insert_comments("level1", "back_glide", "streamlined_position", "0", "remember to keep your hips nice and high!")
insert_comments("level1", "front_glide", "streamlined_position", "1", "great work keeping your chin down and arms stretched!")

value = select_comments("level1", "back_glide", "streamlined_position", "0")
for val in value:
    print(val)

conn.close()