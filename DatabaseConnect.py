import sqlite3

class DatabaseConnect():
    """docstring for database"""
    def __init__(self, arg):
        self.db_name = db_name
        
    def select_comments(self, level, skill, attribute, sentiment):
        extraction = """
            SELECT skill, attribute, sentiment, comment 
            FROM skills INNER JOIN directory ON skills.id = directory.attr_id 
            INNER JOIN comments ON directory.comment_id = comments.id 
            WHERE level = ? AND skill = ? AND attribute = ? AND sentiment = ? 
            """ 
        with sqlite3.connect(self.db_name) as conn:
            c = conn.cursor()
            c.execute(extraction,[level, skill, attribute, sentiment])
            return c.fetchall()

    def fetch_comments(self, ticket):
        comments = []
        level = ticket["level"]
        skill = None
        def recursive_select(ticket):
            global skill
            for key, value in ticket.items(): 
                if isinstance(value, dict):
                    skill = key
                    recursive_select(value)
                else:
                    comments.append(self.select_comments(level, skill, key, value))
            return comments
        return recursive_select(ticket["skills"])

    def insert_comment(self, level, skill, attribute, sentiment, comment):
        with sqlite3.connect(self.db_name) as conn:
            c = conn.cursor()
            value = self._get_skills_id(c, level, skills, attribute)
            if value == None:
                attr_id = self._insert_skill(c, level, skills, attribute)
            else:
                attr_id = value[0]
            comment_id = self._insert_comment(c, sentiment, comment)
            self._insert_relationship(c, attr_id, comment_id)
            conn.commit()
        return True

    def _get_skills_id(self, cursor, level, skills, attribute):
        cursor.execute("SELECT id FROM skills WHERE level = ? AND skill = ? AND attribute = ?", (level, skill, attribute))
        value = cursor.fetchone()
        return value

    def _insert_skill(self, cursor, level, skill, attribute):
        cursor.execute("INSERT INTO skills(level, skill, attribute) VALUES (?, ?, ?)", (level, skill, attribute))
        return cursor.lastrowid

    def _insert_comment(self, cursor, sentiment, comment):
        cursor.execute("INSERT INTO comments(sentiment, comment) VALUES (?, ?)", (sentiment, comment))
        return cursor.lastrowid

    def _insert_relationship(self, cursor, attr_id, comment_id):
        cursor.execute("INSERT INTO directory(attr_id, comment_id) VALUES (?, ?)", (attr_id, comment_id))
        return cursor.lastrowid
