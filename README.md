# rocket-report
Report Card Writer demo for automated report card comments for swim kids level one.

## Installation
Requires:
PyQT5
SQLite3

Clone repository and hopefully it will run with little to no trouble!

## Usage

```bash
to run rocket-report version alpha:

python rocket-report.py

To create level one database:

python db_setup.py
python fill_skills.py
python fill_comments.py
    >>>Enter comment file for reading...
    File: swimkids.db
    >>>Enter database for writing...
    Database: comments_rc1.txt
    >>>Writing complete!
```
Running rocket-report.py pulls up PyQt UI. 
1) Checkbox if level complete and write in the students name. 
2) Checkbox completed skills and leave incomplete or completed but needs more improvement skills blank. 
3) Press continue.

Presto! You've written a reportcard that would likely have taken 5-10 minutes to write out by hand.

## License
No license, but all skill definitions and skill progressions used are property of The Canadian Red Cross and its Swim Kids program. 

## Project Status

Currently still a work in progress.
Expanding upon the number of levels that can be automatically written.
User interface will hopefully find its way as a front end react application or standard HTML web page.
