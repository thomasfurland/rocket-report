from DatabaseConnect import DatabaseConnect
import json
"""Program Execution

Read a json file (for now) organized in the skill tree format of red cross or in a single comment entry format.
Have comments on separate lines with their descriptors.

eg)
{   "entry" : "multi",
    "level" : "level1",
    "standard" : "fitness",
    "strokes" : {    
        "distance_swim_5m" : {
            "completed_distance" : [
            {
                "comment" : "keep working on swimming the full distance swim!",
                "sentiment" : "negative",
            },
            {
                "comment" : "Well done on your distance swim!",
                "sentiment" : "positive",
            }
            ]
        }
    }
}

or 

[{   "entry" : "single",
    "level" : level1,
    "standard" : "fitness",
    "stroke" : "distance_swim_5m",
    "skill" : "completed_distance",
    "comment" : "keep working on swimming the full distance swim!",
    "sentiment" : "negative"
},
{   "entry" : "single",
    "level" : level1,
    "standard" : "fitness",
    "stroke" : "distance_swim_5m",
    "skill" : null,
    "comment" : "Well done on your distance swim!",
    "sentiment" : "positive"
]}

comment: the comment to be displayed.
sentiment: whether the comment can be seen as positive, negative or neutral.

protect against repeat entries 
can handle multiple single entry or same level multi-entry.

"""
def read_comments(file):
    with open(file) as json_file:  
        comments = json.load(json_file)
    return comments

def write_to_db(comments, database_connect):
    if isinstance(comments, list):
        for card in comments:
            write_to_db(card, database_connect)
    elif isinstance(comments, dict):
        if comments['entry'] == 'multi':
            database_connect.multifill_comments(comments)
        elif comments['entry'] == 'single':
            co = comments
            db = database_connect
            db.insert_comment(co['level'], co['standard'], co['stroke'], co['skill'], co['comment'], co['sentiment'])
    else:
        raise ValueError("Comment type must be list or dictionary")
        
if __name__ == '__main__':
    print("Enter comment file for reading...")
    comment_file = input("File: ")
    print("\nEnter database for writing...")
    db_name = input("Database: ")
    comments = read_comments(comment_file)
    db = DatabaseConnect(db_name)
    write_to_db(comments, db)
    print("Writing complete!")
