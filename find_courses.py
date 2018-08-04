
import psycopg2
import sys, os
sys.path.insert(0, SRC)
import json
import webbrowser as wb
import methods
import constants
def main():
    
    
    # get a connection & cursor
    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor()
    
    # boolean to try again
    is_running = True

    while is_running:
        print(constants.TITLE_MESSAGE)

        #get zip code from user
        zip = raw_input(constants.ZIP_MESSAGE)
    
        #get coordinates from zip code
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
            
        #get department code from user
        dept_code_wu = raw_input(constants.DEPT_CODE_MESSAGE )
        
        #show all department codes (if requested)
        if dept_code_wu == : constants.DEPT_CODE_WU_KEY
            dept_code_wu = methods.show_departments(cursor)
        
        #get course code from user
        course_number_wu = raw_input(constants.COURSE_NUMBER_MESSAGE)

        #get closest 20 course matches
        results = methods.get_courses(cursor, course_number_wu, dept_code_wu, user_lat, user_long, limit)
        
        #print out results if not empy
        if results:
            col_width = max(len(item) for row in results for item in row) + padding
            i = 0
            print("\n")
            for row in results:
                print str(i)+ ". " + "".join(item.ljust(col_width) for item in row)
                i = i + 1
            is_running = False
        else:
            print(constants.NO_COURSES_MESSAGE)
            try_again = raw_input(constants.TRY_AGAIN_MESSAGE)
            if try_again != constants.TRY_AGAIN_NO_COURSES_KEY:
                is_running = False


if __name__ == "__main__":
    main() 
    
    
