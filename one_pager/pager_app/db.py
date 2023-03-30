# This file is for reading data from the db/ directory
import sql


# parses text files (only) found in the db directory
def parse_text(filename):
    FILE_PATH = "data/" + filename
    with open(FILE_PATH,"r") as f:
        data = f.read()
        f.close()
    processed_data = data.split("\n\n\n")
    return processed_data

def connect():
    DB_FILE="tables.db"
    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
    c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events
    return (c, db)

def disconnect(db):
    db.commit() #save changes
    db.close()  #close database




