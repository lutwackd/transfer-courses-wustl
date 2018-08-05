# transfer-courses-wustl
A redesign of Washington University in St. Louis's delivery of transfer-course information using Python & PostgreSQL

Collaborators: Ali Axelrod, Davis Lutwack, Kristen Wilder

### Purpose
* Originally, when looking for a summer course, students had to search through hundreds of unorganized schools and thousands of unorganized courses that would be accepted for credit at WashU
* With this project, students can now easily find schools and course offerings near them

### Summary
* Data cleanup + enrichment using Python scripting and SQL techniques: 
  * Identify and remove duplicates, fix inconsistent naming and mappings
  * Use api service to retrieve location information for schools
* Find schools feature:
  * Retrieves closest schools to user's location that are offering wustl-accepted courses 
  * Opens information about all course offerings for selected school in web browser
* Find courses feature:
  * Retrieves closest course offerings to a user's location for a specific wustl course
  * Displays a list of all department codes on request and reprompts on incorrect entry 
  
### Getting started
* clone this repository
* `cd transfer-courses-wustl `
* `pip install psycopg2`
* To find schools near you: `python find_schools.py`
* To find courses near you: `python find_courses.py`
