assessment = {
    "level" : "level1",
    "date": 123,
    "instructor": 123,
    "classNumber": 123,
    "student": 123, 
    "completed": "0",
    "skills" : {    
        "fitness": {
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
        "swimming" : {
            "back_glide" : {
                "completed_3_times" : "1",
                "completed_duration" : "0",
                "kick_from_hip" : "0",
                "streamlined_position" : "0"
            }
        }
    }
}
import sqlite3

class Database():
    """docstring for database"""
    def __init__(self, db_name):
        self.db_name = db_name
        
    def fetch_comments(self, level, standard, stroke, skill, sentiment):
        extraction = """
            SELECT standard, stroke, skill, sentiment, comment, stamina, focus, confidence, head, body, legs, arms
            FROM skills INNER JOIN directory ON skills.id = directory.attr_id 
            INNER JOIN comments ON directory.comment_id = comments.id 
            WHERE level = ? AND standard = ? AND stroke = ? AND skill = ? AND sentiment = ? 
            """ 
        with sqlite3.connect(self.db_name) as conn:
            c = conn.cursor()
            c.execute(extraction,[level, standard, stroke, skill, sentiment])
            return c.fetchall()

    def multi_fetch_comments(self, card):
        comments = list()
        level, skills = card["level"], card["skills"]
        for standard in skills:
            for stroke in skills[standard]:
                for skill, sentiment in skills[standard][stroke].items():
                    comments.append(self.fetch_comments(level, standard, stroke, skill, sentiment))
        return comments


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
            c = conn.cursor()
            if not self._get_skill(c, level, standard, stroke, skill):
                c.execute(insertion, [level, standard, stroke, skill, stamina, focus, confidence, head, body, legs, arms])
            else:
                raise RuntimeError("Skill already exists")
            return c.lastrowid

    def multifill_comments(self, card):
        level, standard, strokes = card['level'], card['standard'], card['strokes']
        for stroke in strokes:
            for skill in strokes[stroke]:
                for comments in strokes[stroke][skill]:
                    comment, sentiment = comments["comment"], comments["sentiment"]
                    self.insert_comment(level, standard, stroke, skill, comment, sentiment)


    def insert_comment(self, level, standard, stroke, skill, comment, sentiment):
        with sqlite3.connect(self.db_name) as conn:
            c = conn.cursor()
            value = self._get_skill(c, level, standard, stroke, skill)
            if value:
                skill_id = value['id']
            else:
                raise RuntimeError("Attribute of comment doesn't exist")
            comment_id = self._insert_comment(c, sentiment, comment)
            self._insert_relationship(c, skill_id, comment_id)
            conn.commit()
        return True

    def _get_skill(self, cursor, level, standard, stroke, skill):
            cursor.execute("SELECT id, skill FROM skills WHERE level = ? AND standard = ? AND stroke = ? AND skill = ?", (level, standard, stroke, skill))
            value = cursor.fetchone()
            if value:
                skill = dict()
                skill['id'], skill['name'] = value[0], value[1]
                return skill
            else:
                return False

    def _insert_comment(self, cursor, sentiment, comment):
        cursor.execute("INSERT INTO comments(sentiment, comment) VALUES (?, ?)", (sentiment, comment))
        return cursor.lastrowid

    def _insert_relationship(self, cursor, attr_id, comment_id):
        cursor.execute("INSERT INTO directory(attr_id, comment_id) VALUES (?, ?)", (attr_id, comment_id))
        return cursor.lastrowid

if __name__ == "__main__":
    db = Database("test.db")

    # conn = sqlite3.connect('test.db')
    # c = conn.cursor()

    # c.execute("SELECT * from skills")
    # result = c.fetchall()
    # for i in result:
    #     print(i)
    # exit()
    comment_list = {
    "entry" : "multi",
    "level" : "level1",
    "standard" : "fitness",
    "strokes" : {    
        "distance_swim_2m" : {
            "completed_distance" : [
                {
                "comment" : "make sure to swim the full distance!",
                "sentiment" : "negative",
                },
                {
                "comment" : "Well done meeting your distance swim requirement!",
                "sentiment" : "positive",
                }
                ]
            }
        }   
    }

    assess_list = {
    "entry" : "multi",
    "level" : "level1",
    "skills" : {
        "fitness" : {
            "distance_swim_5m" : {
                "completed_distance" : "positive",
                },
            "distance_swim_2m" : {
                "completed_distance" : "negative",
                }
            }
        }   
    }

    skills_list = {
        "level" : "level1",
        "standard" : "fitness",
        "strokes" : {
            "distance_swim_2m" : [
                {
                    "skill" : "completed_distance",
                    "attribute" : [1,1,0,0,0,0,0]
                },
                {
                    "skill" : "arm_leg_combo",
                    "attribute" : [0,1,0,0,0,1,1]
                },
            ]
        }
    }
    db.multifill_comments(comment_list)
    print(db.multi_fetch_comments(assess_list))