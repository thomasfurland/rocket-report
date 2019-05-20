"""Used to connect to an sql database

A class that takes in database (db_name) as a parameter and accesses
and returns data from the database depending on the method selected.

"""
import sqlite3

class DatabaseConnect():
    """Class that connects to a database"""
    def __init__(self, db_name):
        """__init__ method for creating DatabaseConnect object

        Takes in a database name as a param and returns a DatabaseConnect
        object. This database needs to be pre-existing and must have skills,
        comments and directory tables in order for methods to work.

        Parameters
        ----------
        db_name : str
            name of an existing database with skills, comments and directory tables
        """
        self.db_name = db_name

    def multi_fetch_comments(self, card):
        """fetch comments from nodes of a tree structure

        Traverses through a tree-like dictionary structure
        dict -> dict -> dict -> dict and calls fetch_comments()
        function using values collected during traversal

        Parameters
        ----------
        card : dict of dict of dict of dict
            a datastructure used to house the skills of various
            swim strokes in a specific order

        Returns
        -------
        list of tuple
            returns a relevant list of comments from database as tuples
            with a specific format.
            see fetch_comments for tuple formatting.

        """
        comments = list()
        level, skills = card["level"], card["skills"]
        for standard in skills:
            for stroke in skills[standard]:
                for skill, sentiment in skills[standard][stroke].items():
                    if sentiment == '1':
                        neutral = '2'
                        comments.extend(self.fetch_comments(level, standard, stroke, skill, neutral))
                    comments.extend(self.fetch_comments(level, standard, stroke, skill, sentiment))
        return comments

    def fetch_comments(self, level, standard, stroke, skill, sentiment):
        """Select specific comment from the database

        Using sql query commands selects and returns a comment tuple
        from the database.

        Parameters
        ----------
        level : str
            a string labeling the level of the skill
        standard : str
            a string labeling the standard of the skill
        stroke : str
            a string labeling the stroke of the skill
        skill : str
            a string labeling the skill
        sentiment : str
            a string to label the sentiment

        Returns
        -------
        tuple
            returns a tuple for the specific skill that was passed.
            (category -> str, stroke -> str, skill -> str,
            sentiment -> str, comment -> str, stamina -> bool,
            confidence -> bool, head -> bool, body -> bool, legs -> bool,
            arms -> bool)
            eg.
            ('fitness', 'flutter_kick_5m_assisted', 'horizontal_body_position',
            'neutral', 'you managed to keep your body straight and flat for flutter kick',
             0, 0, 0, 0, 1, 0, 0)
        """
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
        """Inserts multiple skills into the database

        Inserts skills into database using insert_skill method.
        Iterates through tree-like dictionary structure.
        dict -> dict -> list -> dict

        Parameters
        ----------
        card : dict of dict of list of dict
            a dictionary used to store a list of skills categorically.

        Returns
        -------
        None-type
            Does not return anything and only relies on python and sql
            internal error handling system.
        """
        level, standard, strokes = card['level'], card['standard'], card['strokes']
        for stroke in strokes:
            for skills in strokes[stroke]:
                skill, attribute = skills['skill'], skills['attribute']
                self.insert_skill(level, standard, stroke, skill, attribute)

    def insert_skill(self, level, standard, stroke, skill, attributes):
        """Inserts the skill passed through into skills table.

        Takes in parameters used to correctly insert skill into
        skills table if skill doesn't already exist.
        Raises a runtime error if the skill already exists.

        Parameters
        ----------
        level : str
            a string used to describe a skill
        standard : str
            a string used to describe a skill
        stroke : str
            a string used to describe a skill
        skill : str
            a string used to describe a skill
        sentiment : str
            a string used to describe a skill

        Returns
        -------
        int
            returns the id of the executed query
        """
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
        """Insert multiple comments into the database.

        Iterates through a tree-like dictionary data structure and
        inserts each comment by calling the insert_comment method.

        Parameters
        ----------
        card : dict of dict of dict of list
            a dictionary used to store comments categorically.

        Returns
        -------
        None-type
            relies on python and sql internal error handling system.
        """
        level, standard, strokes = card['level'], card['standard'], card['strokes']
        for stroke in strokes:
            for skill in strokes[stroke]:
                for comments in strokes[stroke][skill]:
                    comment, sentiment = comments["comment"], comments["sentiment"]
                    self.insert_comment(level, standard, stroke, skill, comment, sentiment)


    def insert_comment(self, level, standard, stroke, skill, comment, sentiment):
        """Inserts comment into comments table and registers in directory.

        Inserts a comment into the comments table if the appropriate skill
        exists and it doesn't already exist in the database. Proceeds
        to register skill and comment relationship into the directory
        table.

        Parameters
        ----------
        level : str
            a string used to describe a skill
        standard : str
            a string used to describe a skill
        stroke : str
            a string used to describe a skill
        skill : str
            a string used to describe a skill
        sentiment : str
            a string used to describe a skill

        Returns
        -------
        bool
            returns True if there are no runtime errors and no
            python internal errors.

        Raises
        ------
        RuntimeError
            raised if skill or attribute of comment doesnt exist or
            if the exact comment already exists in the database.

        """
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
        """Get skill_id if exists in database or return false"""

        cursor.execute("SELECT id, skill FROM skills WHERE level = ? AND standard = ? AND stroke = ? AND skill = ?", (level, standard, stroke, skill))
        value = cursor.fetchone()
        if value:
            skill = dict()
            skill['id'], skill['name'] = value[0], value[1]
            return skill
        return False
    def _comment_exists(self, cursor, level, standard, stroke, skill, comment, sentiment):
        """Check if comment already exists in database"""

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
        """Insert comment into comment table"""

        cursor.execute("INSERT INTO comments(sentiment, comment) VALUES (?, ?)", (sentiment, comment))
        return cursor.lastrowid
    def _insert_relationship(self, cursor, attr_id, comment_id):
        """Insert relationship into directory table"""

        cursor.execute("INSERT INTO directory(attr_id, comment_id) VALUES (?, ?)", (attr_id, comment_id))
        return cursor.lastrowid

if __name__ == '__main__':
    pass
