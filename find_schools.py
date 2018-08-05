import sys
import os
import json
import webbrowser as wb

import psycopg2

sys.path.insert(0, "./src/")
import methods
import constants

def main():

    # get a connection & cursor to postgres
    conn = psycopg2.connect(constants.CONN_STRING)
    cursor = conn.cursor()

    is_running = True

    while is_running:
        print(constants.TITLE_MESSAGE)

        #get coordinates from user zip code
        zip = raw_input(constants.ZIP_MESSAGE)
        coordinates = methods.get_coordinates(cursor, zip)

        if coordinates == None:
            print(constants.NO_ZIP_MATCH_MESSAGE)

            try_zip_again = raw_input(constants.TRY_AGAIN_MESSAGE)
            if try_zip_again == constants.TRY_AGAIN_NO_COURSES_KEY:
                continue
            else:
                is_running = False
                break
        else:
            user_lat = coordinates[0]
            user_long = coordinates[1]

        #get closest 20 schools
        results = methods.get_schools(cursor, user_lat, user_long)

        #formatting tuple to not show commas
        results = list(sum(results, ()))

        print #newline
        for i, school in enumerate(results):
            print (str(i) +  '. ' + school)

        #prompt for school that user wants more info about + open page
        open_link = raw_input(constants.PICK_SCHOOL_MESSAGE)
        if open_link == constants.OPEN_LINK_KEY:
            is_running = False
        else:
            wb.open(constants.WU_URL + (results[int(open_link)]), new = 2)
            is_running = False

if __name__ == "__main__":
    main()
