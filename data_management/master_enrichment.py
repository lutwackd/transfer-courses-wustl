import psycopg2
import sys, os
import pprint
import requests, json


def main():
    conn_string = "host='ec2-18-222-149-129.us-east-2.compute.amazonaws.com' dbname='transfer_courses' user=(%s) password=(%s)" % ((os.getenv("SU_LOGIN")),(os.getenv("SU_PASSWORD")),)
    
    # print the connection string we will use to connect
    print "Connecting to database\n	->%s" % (conn_string)
    
    # get a connection, if a connect cannot be made an exception will be raised here
    conn = psycopg2.connect(conn_string)
    
    
    # conn.cursor will return a cursor object, you can use this cursor to perform queries
    cursor = conn.cursor()
    print "Connected!\n"
    
    cursor.execute("select id from schools_oth where lat is null")
    empty = cursor.fetchall();
    for i in empty:
        cursor.execute("select name_oth from schools_oth where id = (%s)",(i,))
        
        try:
            result_school_name = cursor.fetchall()[0]
            
            response = requests.get(
            "https://maps.googleapis.com/maps/api/geocode/json?"
            "address=" + str(result_school_name) +
            "&key=" + os.getenv("GOOGLE_API_KEY")
            )
        
            school_lat = (response.json()["results"][0]["geometry"]["location"]["lat"])
            school_long = (response.json()["results"][0]["geometry"]["location"]["lng"])    
            
        
            cursor.execute("update schools_oth SET lat = (%s), long = (%s)  WHERE id = (%s)",(school_lat,school_long,i,))
            conn.commit()
            
            
            print(i)
        except:
            print(i)


if __name__ == "__main__":
    main()