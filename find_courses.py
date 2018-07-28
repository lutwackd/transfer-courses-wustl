
import psycopg2
import sys, os
sys.path.insert(0, './src/')
import json
import webbrowser as wb
import methods

def main():
    
    #consts
    conn_string = "host='ec2-18-222-149-129.us-east-2.compute.amazonaws.com' dbname='transfer_courses' user='guest' password='guest'"
    padding = 5
    limit = 10
    
    # get a connection & cursor
    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor()
    
    is_running = True

    while is_running:
        print("\n\n--------WASHU TRANSFER COURSE FINDER--------")

        #get zip code from user
        zip = raw_input("\n\nTo find colleges offering courses near you, enter your zip code: ")
    
        #get coordinates from zip code
        coordinates = methods.get_coordinates(cursor, zip)
       
        if coordinates == None:
            print("\nNo zip codes were found that match your input.")
            try_zip_again = raw_input("\nWould you like to try again? Enter Y to try again or any other key to leave. ")
            if try_zip_again == "Y":
                continue
            else:
                is_running = False
                break      
        else:
            user_lat = coordinates[0]
            user_long = coordinates[1]
            
        #get department code from user
        dept_code_wu = raw_input("\n\nEnter the WashU Department Code for the course you would like to receive"
                                "credit for. \nOr, enter 'L' to see a list of deparments:  " )
        
        #show all department codes (if requested)
        if dept_code_wu == 'L':
            dept_code_wu = methods.show_departments(cursor)
        
        
        #get course code from user
        course_number_wu = raw_input("\n\nEnter the WashU Course Number for the course you would like to"
                                    "\nreceive credit for: ")

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
            print("\nNo courses were found that match your input.")
            try_again = raw_input("\nWould you like to try again? Enter Y to try again or any other key to leave. ")
            if try_again != "Y":
                is_running = False


if __name__ == "__main__":
    main() 
    
    
