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
            report_card.append(self._randomize_comment(comments[0]))
        for i in range(2):
            report_card.append(self._randomize_comment(comments[1]))
        report_card.append(f"Keep up the excellent effort and good luck in level {int(self.level[-1])+1}")
        return report_card

    def _randomize_comment(self, comments):
        comment = random.choice(comments)[4]
        return comment

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
    "entry" : "multi",
    "level" : "level1",
    "student" : "Demarkus",
    "completed" : "1",
    "skills" : {
        "fitness" : {
            "distance_swim_5m" : {
                "completed_distance" : "positive",
                "front_or_back_swim" : "negative"
                },
            "flutter_kick_5m_assisted" : {
                "completed_distance" : "negative",
                }
            }
        }   
    }
    report_card = ReportCard(assessment, 'test.db')
    print(report_card.build())