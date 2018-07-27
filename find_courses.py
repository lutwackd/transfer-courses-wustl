import psycopg2
import sys, os
import json
import webbrowser as wb

def main():
    #connection string for a readonly user
    conn_string = "host='ec2-18-222-149-129.us-east-2.compute.amazonaws.com' dbname='transfer_courses' user='guest' password='guest'"
    
    # get a connection & cursor
    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor()
    
    is_running = True

    while is_running:
        print("\n\n--------WASHU TRANSFER COURSE FINDER--------")

        #retrieve zip, department ID, and course number from user
        zip = raw_input("\n\nTo find colleges offering courses near you, enter your zip code: ")
        cursor.execute("select lat, long from zip_coordinates_map where zip = (%s)", (zip,))
        coordinates = cursor.fetchone()
        user_lat = coordinates[0]
        user_long = coordinates[1]

        dept_code_wu = raw_input("\n\nEnter the WashU Department Code for the course you would like to receive credit for: ")
        course_number_wu = raw_input("\n\nEnter the WashU Course Number for the course you would like to receive credit for: ")

        #get closest 20 course matches
        cursor.execute('''select so.name_oth, co.dept_code_oth, co.course_num_oth from courses_oth co join schools_oth so on so.id =
                        co.school_id_oth where co.course_num_wu = (%s) and co.dept_code_wu = (%s) order by geodistance(lat, long, (%s)
                        ,(%s)) asc limit 10''', (course_number_wu, dept_code_wu, user_lat, user_long,))
        results = cursor.fetchall()
        

        if not results:
            print("\nNo courses were found that match your input.")
            try_again = raw_input("\nWould you like to try again? Enter Y to try again or any other key to leave. ")
            if try_again == "Y":
                is_running = True
            else:
                is_running = False
        else:
            col_width = max(len(item) for row in results for item in row) + 5  # padding
            i = 0
            print("\n")
            for row in results:
                print str(i)+ ". " + "".join(item.ljust(col_width) for item in row)
                i = i + 1
            is_running = False


if __name__ == "__main__":
    main() 
    
    
