# transfer-courses-wustl
A redesign of Washington University in St. Louis's delivery of transfer-course information<br>
Using PostgreSQL & Python 

### Summary
* Used Python scripts and SQL to clean up a large unmaintained data set of transfer courses
* Enriched school data with api service for location
* __This allows students to now find courses near them as opposed to looking through hundreds of unorganized schools__

### How To Use
* The script will first prompt for a zip code
* The 20 closest schools offering transferrable WUSTL Engineering courses are displayed 
* User can choose to see courses at those schools

### Setup
* clone this repository
* `cd transfer-courses-wustl `
* `pip install pyscopg2`
* `python find_schools.py`

