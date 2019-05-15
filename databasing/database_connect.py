import sqlite3

class DatabaseConnect():
    """docstring for database"""
    def __init__(self, db_name):
        self.db_name = db_name

    def multi_fetch_comments(self, card):
        comments = list()
        level, skills = card["level"], card["skills"]
        for standard in skills:
            for stroke in skills[standard]:
                for skill, sentiment in skills[standard][stroke].items():
                    if sentiment == '1':
                        neutral = '2'
                        comments.extend(self.fetch_comments(level, standard, stroke, skill, neutral))
                    comments.extend(self.fetch_comments(level, standard, stroke, skill, sentiment))
                # comments.extend(self.fetch_comments(level, standard, stroke, 'Null', sentiment))
        return comments

    def fetch_comments(self, level, standard, stroke, skill, sentiment):
        extraction = """
            SELECT standard, stroke, skill, sentiment, comment, stamina, focus, confidence, head, body, legs, arms
            FROM skills INNER JOIN directory ON skills.id = directory.attr_id 
            INNER JOIN comments ON directory.comment_id = comments.id 
            WHERE level = ? AND standard = ? AND stroke = ? AND skill = ? AND sentiment = ? 
            """
        if sentiment == '1':
            sentiment = 'positive'
        elif sentiment == '0':
            sentiment = 'negative'
        elif sentiment == '2':
            sentiment = 'neutral'
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(extraction, [level, standard, stroke, skill, sentiment])
            return cursor.fetchall()

    def multifill_skills(self, card):
        level, standard, strokes = card['level'], card['standard'], card['strokes']
        for stroke in strokes:
            for skills in strokes[stroke]:
                skill, attribute = skills['skill'], skills['attribute']
                self.insert_skill(level, standard, stroke, skill, attribute)

    def insert_skill(self, level, standard, stroke, skill, attributes):
        stamina, focus, confidence, head, body, legs, arms = attributes
        insertion = """
            INSERT INTO skills(level, standard, stroke, skill, 
            stamina, focus, confidence, head, body, legs, arms)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            if not self._get_skill(cursor, level, standard, stroke, skill):
                cursor.execute(insertion, [level, standard, stroke, skill, stamina, focus, confidence, head, body, legs, arms])
            else:
                raise RuntimeError("Skill already exists")
            return cursor.lastrowid

    def multifill_comments(self, card):
        level, standard, strokes = card['level'], card['standard'], card['strokes']
        for stroke in strokes:
            for skill in strokes[stroke]:
                for comments in strokes[stroke][skill]:
                    comment, sentiment = comments["comment"], comments["sentiment"]
                    self.insert_comment(level, standard, stroke, skill, comment, sentiment)


    def insert_comment(self, level, standard, stroke, skill, comment, sentiment):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            value = self._get_skill(cursor, level, standard, stroke, skill)
            if value:
                skill_id = value['id']
            else:
                raise RuntimeError("Attribute of comment doesn't exist")
            if not self._comment_exists(cursor, level, standard, stroke, skill, comment, sentiment):
                comment_id = self._insert_comment(cursor, sentiment, comment)
                self._insert_relationship(cursor, skill_id, comment_id)
            else:
                print(comment)
                raise RuntimeError("Comment already exists")
            conn.commit()
        return True

    def _get_skill(self, cursor, level, standard, stroke, skill):
        cursor.execute("SELECT id, skill FROM skills WHERE level = ? AND standard = ? AND stroke = ? AND skill = ?", (level, standard, stroke, skill))
        value = cursor.fetchone()
        if value:
            skill = dict()
            skill['id'], skill['name'] = value[0], value[1]
            return skill
        return False
    def _comment_exists(self, cursor, level, standard, stroke, skill, comment, sentiment):
        extraction = """
            SELECT comment_id
            FROM skills INNER JOIN directory ON skills.id = directory.attr_id 
            INNER JOIN comments ON directory.comment_id = comments.id 
            WHERE level = ? AND standard = ? AND stroke = ? 
            AND skill = ? AND sentiment = ? AND comment = ?
            """
        cursor.execute(extraction, [level, standard, stroke, skill, sentiment, comment])
        comment_id = cursor.fetchone()
        if comment_id:
            return comment_id
        return False
    def _insert_comment(self, cursor, sentiment, comment):
        cursor.execute("INSERT INTO comments(sentiment, comment) VALUES (?, ?)", (sentiment, comment))
        return cursor.lastrowid
    def _insert_relationship(self, cursor, attr_id, comment_id):
        cursor.execute("INSERT INTO directory(attr_id, comment_id) VALUES (?, ?)", (attr_id, comment_id))
        return cursor.lastrowid

if __name__ == '__main__':
    pass
