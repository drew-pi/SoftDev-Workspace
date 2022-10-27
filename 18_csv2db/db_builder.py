import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O
import os

# os.system('rm -rf discobandit.db') # this is to delete the dataframe file as to not encounter any errors during testing


def populate_table(file_name,table_name,elements,keys):

    db = sqlite3.connect(file_name) #open if file exists, otherwise create
    c = db.cursor() # creates cursor object to pass commands to the database

    c.execute(f'''create table if not exists {table_name}('{keys[0]}' text, {keys[1]} int, {keys[2]} text);''') # creates the table
    for row in elements:

        # iterate through the elements and add them to the table ( row by row )
        c.execute(f'''insert into {table_name} values('{row[keys[0]]}',{row[keys[1]]},'{row[keys[2]]}');''') 

    c.execute(f'''select * from {table_name}''') # for some reason need this execute statment to get fetchall
    return_msg = c.fetchall() # returns a list of tuples that are rows

    db.commit() #save changes
    db.close()  #close database
        
    return (return_msg)

filename = 'students.csv'
with open(filename,newline='') as csvfile:
    student_reader = csv.DictReader(csvfile)
    student_csv_list = list(student_reader)
    student_keys = list((student_csv_list[0]).keys())


DB_FILE="discobandit.db"
student_info = populate_table(DB_FILE,'students',student_csv_list,student_keys)
print(student_info)


filename = 'courses.csv'
with open(filename,newline='') as csvfile:
    course_reader = csv.DictReader(csvfile)
    course_csv_list = list(course_reader)
    course_keys = list((course_csv_list[0]).keys())


course_info = populate_table(DB_FILE,'courses',course_csv_list,course_keys) # open up the same database, and then make a new table
print(course_info)




