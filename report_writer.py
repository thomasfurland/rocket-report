from databasing.DatabaseConnect import DatabaseConnect
import random


class ReportCard:
    def __init__(self, assessment, database):
        self.level = assessment['level']
        self.completed = int(assessment['completed'])
        self.report = assessment
        self.db = DatabaseConnect(database)
        self.comments = None 

    def build(self):
        self.comments = self.db.multi_fetch_comments(self.report)
        self.comments = self._comments_by_sentiment(self.comments)
        if self.completed:
            report_card = self._positive_template(self.comments)
        else:
            report_card = self._negative_template(self.comments)
        return report_card

    def _positive_template(self, comments):
        report_card = list()
        report_card.append(f"Great work {self.report['student']}!")
        for i in range(4):
            comment, comments[0] = self._randomize_comment(comments[0])
            report_card.append(comment)
        for i in range(2):
            comment, comments[1] = self._randomize_comment(comments[1])
            report_card.append(comment)
        report_card.append(f"Keep up the excellent effort and good luck in level {int(self.level[-1])+1}")
        return report_card

    def _negative_template(self, comments):
        report_card = list()
        report_card.append(f"Great effort {self.report['student']}!")
        for i in range(4):
            comment, comments[1] = self._randomize_comment(comments[1])
            report_card.append(comment)
        for i in range(2):
            comment, comments[0] = self._randomize_comment(comments[0])
            report_card.append(comment)
        report_card.append(f"Keep working hard to improve your swimming")
        return report_card

    def _randomize_comment(self, comments):
        comment = str()
        if comments:
            random.shuffle(comments)
            comment = comments.pop()[4]
        return comment, comments

    def _comments_by_sentiment(self, comments):
        pos, neg, neut = list(), list(), list()
        for comment in comments:
            for skill in comment:
                sentiment = skill[3]
                if sentiment == 'positive':
                    pos.append(skill)
                elif sentiment == 'negative':
                    neg.append(skill)
                elif sentiment == 'neutral':
                    neut.append(skill)
                else:
                    raise ValueError("you goofed mofo")
        return [pos]+[neg]+[neut]

    def prescreen(self):
        pass

if __name__ == '__main__':
    assessment = {
    "level" : "level1",
    "date": "2019-04-08",
    "instructor": "Thomas",
    "classNumber": "4485362",
    "student": "Demarkus", 
    "completed": "1",
    "skills" : {    
        "fitness": {
            "flutter_kick_5m_assisted" : {
                "horizontal_body_position" : '1',
                "front_or_back_kick" : '1',
                "kick_from_hip" : '1',
                "vertical_leg_motion" : '1',
                "completed_distance" : '1' 
            },
            "distance_swim_5m" : {
                "front_or_back_swim" : '1',
                "arm_leg_movement" : '1',
                "body_position_w_flutter_kick" : '1',
                "horizontal_body_position" : '1',
                "exhale_underwater" : '1',
                "completed_distance" : '1'
            }
        }, 
        "safety": {
            "facility_site_orientation" : {
                "identifies_safety_and_hazards" : '1',
                "waits_for_instructor" : '1'
            },
            "supervision" : {
                "explains_supervision" : '1'
            },
            "shallow_entries_exits" : {
                "waits_for_instructor" : '1',
                "performs_safe_entries_exits" : '1',
                "performs_safe_exits" :'1'
            },
            "submerge_head" : {
                "head_underwater_3sec" : '1',
                "eyes_open_underwater" : '1'
            },
            "exhale_through_mouth_nose" : {
                "exhale_below_surface" : '1',
                "exhale_w_head_underwater" : '1'
            }
        },
        "swimming" : {
            "rhythmic_breathing_5_times" : {
                "exhale_underwater_inhale_air" : '1', 
                "rhythmic_relaxed" : '1',
                "5_repetitions" : '1'
            },
            "front_float_recovery_3sec" : {
                "stable_face_in_water" : '1', 
                "float_3sec_relaxed" : '1',
                "vertical_recovery" : '1'
            },
            "front_glide_5sec" : {
                "glide_5sec_relaxed" : '1', 
                "streamlined_body_position" : '1',
                "vertical_recovery" : '1'
            },
            "front_glide_kick_5m" : {
                "vertical_leg_motion" : '1', 
                "kicks_5m_horizontal_body" : '1',
                "streamlined_body_position" : '1',
                "exhale_underwater" :'1' 
            },
            "back_float_recovery_3sec" : {
                "stable_back_float" : '1', 
                "float_3sec_relaxed" : '1',
                "vertical_recovery" : '1'
            },
            "back_glide_5sec" : {
                "glide_5sec_relaxed" : '1', 
                "streamlined_body_position" : '1',
                "vertical_recovery" : '1'
            },
            "rollover_glide_5sec_assisted" : {
                "rolls_front_to_back" : '1', 
                "exhale_underwater_inhale_air" : '1',
                "rolls_back_to_front" : '1' ,
                "streamlined_body_position" : '1',
                "starts_roll_head_shoulders" : '1',
                "vertical_recovery" : '1'
            },
            "front_swim_5m" : {
                "arm_leg_movement" : '1', 
                "completed_distance" : '0' 
            }
        }
    }
}
    report_card = ReportCard(assessment, 'test.db')
    print(report_card.build())