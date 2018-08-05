#general messages
TITLE_MESSAGE = "\n\n--------WASHU TRANSFER COURSE FINDER--------"
NO_COURSES_MESSAGE = "\nNo courses were found that match your input."
NO_ZIP_MATCH_MESSAGE = "\nNo zip codes were found that match your input."

#postgres connection
CONN_STRING = '''
    host='ec2-18-222-149-129.us-east-2.compute.amazonaws.com'
    dbname='transfer_courses' user='guest' password='guest'
'''
#external links
WU_URL = "http://registrar.seas.wustl.edu/EVALS/evals.asp?school="

#query limits/formatting
PADDING = 5
SCHOOL_LIMIT = 20
COURSE_LIMIT = 20

#keys
TRY_AGAIN_NO_COURSES_KEY = "Y"
OPEN_LINK_KEY = "Q"
DEPT_CODE_WU_KEY = "L"

#instructions
ZIP_MESSAGE = '''
\nTo find colleges offering courses near you, enter your zip code:
'''
DEPT_CODE_MESSAGE = '''
\nEnter the WashU Department Code for the course you would like
to receive credit for.
Or, enter %s to see a list of deparments:
''' % (DEPT_CODE_WU_KEY)
DEPT_CODE_AFTER_LIST_MESSGAGE = '''
\nEnter your department code:
'''
COURSE_NUMBER_MESSAGE = '''
\nEnter the WashU Course Number for the course you would like to
receive credit for:
'''
PICK_SCHOOL_MESSAGE = '''
\nWhat school would you like to see courses for?
Enter the number or enter %s to exit:
''' % (OPEN_LINK_KEY,)

TRY_AGAIN_MESSAGE = '''
\nWould you like to try again?
Enter %s to try again or any other key to leave.
''' % (TRY_AGAIN_NO_COURSES_KEY,)
