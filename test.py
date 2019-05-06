assessment = {
    "level" : "level1",
    "date": 123,
    "instructor": 123,
    "classNumber": 123,
    "student": 123, 
    "completed": "0",
    "skills" : {    
        "fit": {
            "distance_swim_5m" : {
                "completed_distance" : "0",
                "unassisted" : "0"
            },
            "flutter_kick_5m_assisted" : {
                "completed_distance" : "2"
            }
        }, 
        "safety": {
            "ems_911" : {
                "listened_attentively" : "1",
                "remembered_lesson": "1"
            },
            "surface_support_20sec" : {
                "completed_duration" : "0",
                "unassisted" : "1",
                "completed_3_times" : "0"
            }
        },
        "swim" : {
            "back_glide" : {
                "completed_3_times" : "1",
                "completed_duration" : "0",
                "kick_from_hip" : "0",
                "streamlined_position" : "0"
            }
        },
        "optional" : {
            "completed_options" : "1"
        }
    }
}

comments = {
    "level" : "level1",
    "date": 123,
    "instructor": 123,
    "classNumber": 123,
    "student": 123, 
    "completed": "0",
    "skills" : {    
        "fit": {
            "distance_swim_5m" : {
                "completed_distance" : [
                ("0", "keep working on swimming a full 5 meters!"),
                ("0", "remember to not touch the wall for distance swim!"),
                ("1", "awesome job on your distance swim!"),
                ("1", "great distance swimming!")
                ]
            }
        }
    }
}
import sqlite3

class Database():
    """docstring for database"""
    def __init__(self, db_name):
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
        
    def fill_comments(self, ticket):
            level = ticket["level"]
            skill = None
            def recursive_insert(ticket):
                global skill
                for key, value in ticket.items(): 
                    if isinstance(value, dict):
                        skill = key
                        recursive_insert(value)
                    else:
                        self.insert_comments(level, skill, key, value)
                return True
            return recursive_insert(ticket["skills"])

    def insert_comments(self, level, skill, attribute, comments):
        with sqlite3.connect(self.db_name) as conn:
            c = conn.cursor()
            value = self._get_skills_id(c, level, skill, attribute)
            if value == None:
                attr_id = self._insert_skill(c, level, skill, attribute)
            else:
                attr_id = value[0]
            for comment in comments:
                sentiment = comment[0]
                comment = comment[1]
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

if __name__ == "__main__":
    db = Database("test.db")

    db.fill_comments(comments)
    comments = db.fetch_comments(assessment)
    print(comments)