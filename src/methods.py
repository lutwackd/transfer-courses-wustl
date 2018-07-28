import psycopg2

#consts
padding = 5

def show_departments(cursor): #show the list of all department codes
    cursor.execute('''    
        SELECT
            dw.name,
            dw.code
        FROM departments_wu dw
        ORDER by 1 asc
    ''')
        
    results = cursor.fetchall()
    col_width = max(len(item) for row in results for item in row) + padding  # padding
    
    #show departments
    for row in results:
        print "".join(item.ljust(col_width) for item in row)
        
    return raw_input("\n\nEnter your department code:")

def get_courses(cursor, course_number_wu, dept_code_wu, user_lat, user_long, limit): #get the closest courses
    cursor.execute('''
        SELECT
            so.name_oth,
            co.dept_code_oth,
            co.course_num_oth
        FROM courses_oth co
        JOIN schools_oth so on
            so.id = co.school_id_oth
        WHERE
            co.course_num_wu = (%s) and
            co.dept_code_wu = (%s)
        ORDER by geodistance(lat, long, (%s) ,(%s)) asc
        LIMIT (%s)
    ''',(course_number_wu, dept_code_wu, user_lat, user_long, limit,))
    
    return cursor.fetchall()

def get_coordinates(cursor, zip):
    cursor.execute('''
        SELECT
            zcm.lat,
            zcm.long
        FROM zip_coordinates_map zcm
        WHERE zip = (%s)
    ''', (zip,))
    
    return cursor.fetchone()

def get_schools(cursor, user_lat, user_long):
    cursor.execute('''
        SELECT name_oth
        FROM schools_oth 
        ORDER by geodistance(lat,long, (%s), (%s)) ASC
        LIMIT 20'''
    , (user_lat, user_long,))
    
    return cursor.fetchall()
