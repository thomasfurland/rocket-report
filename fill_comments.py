import DatabaseConnect

"""Program Execution

Read a json file (for now) organized in the skill tree format of red cross or in a single comment entry format.
Have comments on separate lines with their descriptors.

eg)
{	"entry" : "multi",
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

{	"entry" : "single",
	"level" : level1,
	"standard" : "fitness"
	"stroke" : "distance_swim_5m",
	"skill" : "completed_distance",
    "comment" : "keep working on swimming the full distance swim!",
    "sentiment" : "negative"
	},
{	"entry" : "single",
	"level" : level1,
	"standard" : "fitness",
	"stroke" : "distance_swim_5m",
	"skill" : null,
    "comment" : "Well done on your distance swim!",
    "sentiment" : "positive"
	},

comment: the comment to be displayed.
sentiment: whether the comment can be seen as positive, negative or neutral.

protect against repeat entries 
can handle multiple single entry or same level multi-entry.

"""
