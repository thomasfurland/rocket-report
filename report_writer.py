"""Reads json and creates ReportCard Objects

Takes in a specific json tree-like dictionary structure and creates
a reportcard object based on its contents.

"""
import random
from databasing.database_connect import DatabaseConnect

class ReportCard:
    """ReportCard object used to create a reportcard comment"""
    def __init__(self, assessment, database):
        """__init__ method for ReportCard.
        
        Takes in a database param to connect to using DatabaseConnect
        instance and takes in a json object as the assessment.
        
        Parameters
        ----------
        assessment : dict of dict of dict of dict
            tree-like structure of swim skills and their evaluation
        database : DatabaseConnect object
            used to create connection with sql database
        """
        self.db = DatabaseConnect(database)
        self.level = assessment['level']
        self.completed = int(assessment['completed'])
        self.report = assessment
        self.comments = None

    def build(self):
        """Builds a reportcard from a template and comments

        creates list of comments (list -> tuple) and sorts the comments
        by sentiment. Checks level completion and creates appropriate 
        reportcard template. Returns the reportcard comment after a 
        prescreen

        Returns
        -------
        list of str
            returns the finalized comment used for a reportcard.
        """
        self.comments = self.db.multi_fetch_comments(self.report)
        comments = self._sentiment_sort(self.comments)
        if self.completed:
            report_card = self._positive_template(comments)
        else:
            report_card = self._negative_template(comments)
        return self.prescreen(report_card)

    def _positive_template(self, comments):
        """Creates a positively percieved reportcard template"""
        report_card = list()
        positive = self._random_comment(comments['positive'], cycles=1, omit=['swimming', 'fitness'])
        report_card.extend(positive)
        positive = self._random_comment(comments['positive'], cycles=1, omit=['safety', 'swimming'])
        report_card.extend(positive)
        neutral = self._random_comment(comments['neutral'], 1)
        report_card.extend(neutral)
        negative = self._random_comment(comments['negative'], 2)
        report_card.extend(negative)
        positive = self._random_comment(comments['positive'], 3, omit=['safety', 'fitness'])
        report_card.extend(positive)

        report_card.insert(0, f"Awesome Job {self.report['student']}!")
        report_card.append(f"Keep up the effort and good luck in level {int(self.level[-1])+1}.")
        return report_card

    def _negative_template(self, comments):
        """Creates a negatively percieved reportcard template"""
        report_card = list()
        negative = self._random_comment(comments['negative'], 4)
        positive = self._random_comment(comments['positive'], cycles=1, omit=['swimming'])
        report_card.extend(positive)
        report_card.extend(negative)
        neutral = self._random_comment(comments['neutral'], 1)
        report_card.extend(neutral)
        positive = self._random_comment(comments['positive'], 2, omit=['safety', 'fitness'])
        report_card.extend(positive)

        report_card.insert(0, f"Good effort {self.report['student']}!")
        report_card.append("Keep working hard to improve your swimming.")
        return report_card

    def _random_comment(self, comments, cycles, omit=None):
        """randomly selects comment tuple from comment list making new list"""
        comment = list()
        if omit:
            if isinstance(omit, str):
                omit = [omit]
            comments = [com for com in comments if com[0] not in omit]
        cycles = cycles + 1 if cycles > 1 else cycles
        for cycle in range(cycles):
            if comments:
                random.shuffle(comments)
                comment.append(comments.pop())
        comment = self._attribute_sort(self._stroke_sort(comment))
        return comment

    def _sentiment_sort(self, comments):
        """Sorts comments by sentiment and returns a new dict by sentient"""
        _dict = dict()
        _dict['positive'], _dict['negative'], _dict['neutral'] = list(), list(), list()
        for skill in comments:
            sentiment = skill[3]
            if sentiment == 'positive':
                _dict['positive'].append(skill)
            elif sentiment == 'negative':
                _dict['negative'].append(skill)
            elif sentiment == 'neutral':
                _dict['neutral'].append(skill)
            else:
                raise ValueError("you goofed mofo")
        return _dict

    def _stroke_sort(self, comments):
        """Sorts comments by stroke and returns a new list"""
        strokes = [stroke[1] for stroke in self.comments]
        stroke_directory = sorted(set(strokes), key=strokes.index)
        sorted_comments = list()
        for stroke in stroke_directory:
            i = 0
            while i < len(comments):
                if stroke == comments[i][1]:
                    sorted_comments.append(comments[i])
                i += 1
        return sorted_comments

    def _attribute_sort(self, comments):
        """Sorts comments by attribute and returns the same list"""
        changes = True
        while changes:
            changes = False
            for i in reversed(range(1, len(comments))):
                if comments[i][1] == comments[i-1][1]:
                    for attr in range(5, 12):
                        if comments[i][attr] < comments[i-1][attr]:
                            break
                        elif comments[i][attr] > comments[i-1][attr]:
                            comments[i], comments[i-1] = comments[i-1], comments[i]
                            changes = True
                            break
        return comments

    def prescreen(self, comments):
        """Prescreener for reportcard comment.

        Iterates through list of comments extracts comment and adds
        appropriate capitalization of words and punctuation. Also combines
        sentences of same strokes.

        Parameters
        ----------
        comments : list of tuple
            a list of comment tuples that are sorted fully.

        Returns
        -------
        list of str
            returns a finalized list of words as the comment to a reportcard.
        """
        i = 0
        while i < len(comments):
            if isinstance(comments[i], tuple):
                comments[i] = list(comments[i])
                if comments[i-1][-1] in ['!', '.']:
                    comments[i][4] = comments[i][4][0].upper() + comments[i][4][1:]
                if comments[i][1] == comments[i+1][1] and comments[i][3] == comments[i+1][3]:
                    comments.insert(i+1, "and")
                elif comments[i][3] == "positive":
                    comments.insert(i+1, "!")
                else:
                    comments.insert(i+1, ".")
            i += 1
        prescreened_comment = [com[4] if isinstance(com, list) else com for com in comments]
        return prescreened_comment

if __name__ == '__main__':
    ASSESSMENT = {
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
                    "rolls_back_to_front" : '1',
                    "streamlined_body_position" : '1',
                    "starts_roll_head_shoulders" : '1',
                    "vertical_recovery" : '1'
                },
                "front_swim_5m" : {
                    "arm_leg_movement" : '0',
                    "completed_distance" : '0'
                }
            }
        }
    }
    REPORTCARD = ReportCard(ASSESSMENT, 'test.db')
    print(REPORTCARD.build())
