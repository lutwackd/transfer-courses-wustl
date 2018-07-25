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
    
    #retrieve zip code from user and associated lat/long
    print("\n\n--------WASHU TRANSFER COURSE FINDER--------")
    zip = raw_input("\n\nTo find colleges offering courses near you, enter your zip code: ")
    cursor.execute("select lat, long from zip_coordinates_map where zip = (%s)", (zip,))
    coordinates = cursor.fetchone();
    user_lat = coordinates[0]
    user_long = coordinates[1]
    
    #get closest 20 schools
    cursor.execute("select name_oth from schools_oth order by geodistance(lat,long, (%s), (%s)) asc limit 20", (user_lat, user_long,))
    results = cursor.fetchall()
    
    results = list(sum(results, ())) #formatting tuple to not show commas
    
    i = 0
    print("\n")
    for school in results:
        print (str(i) +  '. ' + school)
        i = i + 1
    
    #prompt for school that user wants more info about + open page
    open_link = raw_input("\nWhat school would you like to see courses for? Enter the number: ")
    wb.open('http://registrar.seas.wustl.edu/EVALS/evals.asp?school=' + (results[int(open_link)]), new =2)


if __name__ == "__main__":
    main() 
    
    
