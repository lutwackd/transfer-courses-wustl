import psycopg2
import sys, os
sys.path.insert(0, './src/')
import json
import webbrowser as wb
import methods

def main():

    #consts
    conn_string = "host='ec2-18-222-149-129.us-east-2.compute.amazonaws.com' dbname='transfer_courses' user='guest' password='guest'"
    wu_url = "http://registrar.seas.wustl.edu/EVALS/evals.asp?school="
    
    # get a connection & cursor
    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor()

    is_running = True
    
    while is_running:
        print("\n\n--------WASHU TRANSFER COURSE FINDER--------")

        #retrieve zip code from user and associated lat/long
        zip = raw_input("\n\nTo find colleges offering courses near you, enter your zip code: ")
        
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
        
        #get closest 20 schools
        results = methods.get_schools(cursor, user_lat, user_long)
        
        #formatting tuple to not show commas
        results = list(sum(results, ())) 
        
        i = 0
        print("\n")
        for school in results:
            print (str(i) +  '. ' + school)
            i = i + 1
        
        #prompt for school that user wants more info about + open page
        open_link = raw_input("\nWhat school would you like to see courses for? Enter the number or enter Q to exit: ")
        if open_link == "Q":
            is_running = False
        else:
            wb.open(wu_url + (results[int(open_link)]), new = 2)
            is_running = False

if __name__ == "__main__":
    main() 
    
    
