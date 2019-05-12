"""create a report card writing program in python.
using web interface to connect to python code and database.
Written using React and Django.

code will analyze "punchcard" and orient report layout.
Calls appropriate words from database to fill-in the layout.
iterates over many "punchcards" and returns a list of reportCard objects.
code will push to web interface the returned list.

web interface will pop up view capable of control to make edits to phrases.
save edited reports to database.
allow for downloading of pass or fail in pdf format, displayed on a comment sheet.
***connect to writing unit to write on pre-existing report cards*** 
save confirmed reports to database.
continue? or return home.

database will house phrases categorized as positive, negative, neutral.
will be further categorized by comment id, rc level, fit or safety or swim.
then by swimstrokes and the evaluated comment.
database will also store compiled reports that have been edited or confirmed.

stored reports can then be broken down to better structure layout and phrases.
also used for future prescreen on reportCard objects for readability via machine learning.
"""

# array received from web comprised of punchCards:

assessment = {
    "level" : "1",
    "date": "2019-04-08",
    "instructor": "Thomas",
    "classNumber": "4485362",
    "student": "Demarkus", 
    "completed": "0",
    "skills" : {    
        "fitness": {
            "flutter_kick_5m_assisted" : {
                "horizontal_body_position" : ,
                "front_or_back_kick" : ,
                "kick_from_hip" : ,
                "vertical_leg_motion" : ,
                "completed_distance" : , 
            },
            "distance_swim_5m" : {
                "front_or_back_swim" : ,
                "arm_leg_movement" : ,
                "body_position_w_flutter_kick" : ,
                "horizontal_body_position" : ,
                "exhale_underwater" : ,
                "completed_distance" : 
            }
        }, 
        "safety": {
            "facility_site_orientation" : {
                "identifies_safety_and_hazards" : ,
                "waits_for_instructor" : 
            },
            "supervision" : {
                "explains_supervision" : 
            },
            "shallow_entries_exits" : {
                "waits_for_instructor" : ,
                "performs_safe_entries_exits" : ,
                "performs_safe_exits" :
            },
            "submerge_head" : {
                "head_underwater_3sec" : ,
                "eyes_open_underwater" : 
            },
            "exhale_through_mouth_nose" : {
                "exhale_below_surface" : ,
                "exhale_w_head_underwater" : 
            }
        },
        "swimming" : {
            "rhythmic_breathing_5_times" : {
                "exhale_underwater_inhale_air" : , 
                "rhythmic_relaxed" : ,
                "5_repetitions" : 
            },
            "front_float_recovery_3sec" : {
                "stable_face_in_water" : , 
                "float_3sec_relaxed" : ,
                "vertical_recovery" : 
            },
            "front_glide_5sec" : {
                "glide_5sec_relaxed" : , 
                "streamlined_body_position" : ,
                "vertical_recovery" : 
            },
            "front_glide_kick_5m" : {
                "vertical_leg_motion" : , 
                "kicks_5m_horizontal_body" : ,
                "streamlined_body_position" : ,
                "exhale_underwater" : 
            },
            "back_float_recovery_3sec" : {
                "stable_back_float" : , 
                "float_3sec_relaxed" : ,
                "vertical_recovery" : 
            },
            "back_glide_5sec" : {
                "glide_5sec_relaxed" : , 
                "streamlined_body_position" : ,
                "vertical_recovery" : 
            },
            "rollover_glide_5sec_assisted" : {
                "rolls_front_to_back" : , 
                "exhale_underwater_inhale_air" : ,
                "rolls_back_to_front" : ,
                "streamlined_body_position" : ,
                "starts_roll_head_shoulders" : ,
                "vertical_recovery" : 
            },
            "front_swim_5m" : {
                "arm_leg_movement" : , 
                "completed_distance" :  
            }
        }
    }
}

# iterator logic:

reportCards = list()
report_card = object()

for ticket in assessments:
    db = Database('test.db')
    report_card = reportCard(ticket["level"], ticket["completed"], ticket["student"])
    comments = db.fetch_comments(ticket)
    reportCard.build(comments)
    while not report_card.prescreen():
        report_card.build(comments)
    else:
        reportcards.append(report_card)

# database procedures

class Database():
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

# reportCard Class

class ReportCard:
    def __init__(self, level, student, completed):
        self.level = level
        self.student = student
        self.completed = int(completed)
        self.date = None
        self.classNumber = None
        self.instructor = None 

    def build(self, comments):
        posi_max, negi_max = 4, 2
        posi_min, negi_min = 2, 1 
        if not self.completed:
            posi_max, negi_max = negi_max, posi_max
            posi_min, negi_min = negi_min, posi_min

    def prescreen(self):
        

# convert reportCard objects to json

