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
                "completed_distance" : ,
                "near_horizontal_body_position" : ,
                "kicking" : ,
                "kick_from_hip" : ,
                "legs_moving_up_down" : , 
            },
            "distance_swim_5m" : {
                "chooses_front_back" : ,
                "arm_leg_movement" : ,
                "body_position_flutter_kick" : ,
                "near_horizontal_body_position" : ,
                "exhales_underwater" : ,
                "completed_distance" : 
            }
        }, 
        "safety": {
            "facility_site_orientation" : {
                "listened_attentively" : ,
                "waits_for_instructor" : 
            },
            "supervision" : {
                "understands_adult_supervision" : 
            },
            "shallow_entries_exits" : {
                "waits_for_instructor" : ,
                "enters_exits_shallow_water" : ,
                "safe_exits" :
            },
            "submerge_head" : {
                "submerged_3_seconds" : ,
                "eyes_open_underwater" : 
            },
            "exhale_mouth_nose" : {
                "blows_bubbles" : ,
                "submerged_bubbles" : 
            }
        },
        "swimming" : {
            "rhythmic_breathing_5_times" : {
                "completed_3_times" : , 
                "exhale_mouth_nose" : ,
                "rhythmic_breathing" : ,
                "completed_5_reps" : 
            },
            "front_float_recovery_3_seconds" : {
                "completed_3_times" : , 
                "face_in_water" : ,
                "relaxed_front_float_3_seconds" : ,
                "unassisted_recovery" : 
            },
            "front_glide_5_seconds" : {
                "completed_3_times" : , 
                "completed_duration" : ,
                "streamlined_position" : ,
                "unassisted_recovery" : 
            },
            "front_glide_Kick_5m" : {
                "completed_3_times" : , 
                "front_kick_up_down" : ,
                "completed_distance" : ,
                "streamlined_position" : ,
                "exhales_underwater" :
            },
            "back_float_recovery_3_seconds" : {
                "completed_3_times" : , 
                "ears_in_water" : ,
                "completed_duration" : ,
                "unassisted_recovery" : 
            },
            "back_glide_5_seconds" : {
                "completed_3_times" : , 
                "completed_duration" : ,
                "streamlined_position" : ,
                "unassisted_recovery" : ,
            },
            "rollover_glide_5_seconds_assisted" : {
                "completed_3_times" : , 
                "completed_duration" : ,
                "front_glide_back_glide" : ,
                "exhales_underwater" : ,
                "back_glide_front_glide" : ,
                "streamlined_position" : ,
                "head_shoulder_roll" : ,
                "unassisted_recovery" : ,
            },
            "front_swim_5m" : {
                "completed_3_times" : , 
                "completed_distance" : ,
                "arm_leg_movement" : 
            },
        },
        "optional" : {

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

