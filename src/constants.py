#messages
TITLE_MESSAGE = '\n\n--------WASHU TRANSFER COURSE FINDER--------'
NO_COURSES_MESSAGE = "\nNo courses were found that match your input."
NO_ZIP_MATCH_MESSAGE = "\nNo zip codes were found that match your input."
#constants
HOST_STRING = "host='ec2-18-222-149-129.us-east-2.compute.amazonaws.com' dbname='transfer_courses' user='guest' password='guest'"
URL_STRING = "http://registrar.seas.wustl.edu/EVALS/evals.asp?school="
wu_url = URL_STRING
conn_string = HOST_STRING
SRC = './src/'
padding = 5
limit = 10

#instructions
TRY_AGAIN_MESSAGE = "\nWould you like to try again? Enter Y to try again or any other key to leave. "
DEPT_CODE_MESSAGE = "\n\nEnter the WashU Department Code for the course you would like to receive"
                                "credit for. \nOr, enter 'L' to see a list of deparments:  "
ZIP_MESSAGE = '\n\nTo find colleges offering courses near you, enter your zip code: '
COURSE_NUMBER_MESSAGE = "\n\nEnter the WashU Course Number for the course you would like to"
                                    "\nreceive credit for: "
PICK_SCHOOL_MESSAGE = "\nWhat school would you like to see courses for? Enter the number or enter Q to exit: "


#keys
TRY_AGAIN_NO_COURSES_KEY = "Y"
OPEN_LINK_KEY = "Q"
DEPT_CODE_WU_KEY = 'L'
