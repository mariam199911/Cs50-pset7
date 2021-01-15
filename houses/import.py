# TODO
import cs50
import csv
import sys 
from sys import argv


if len(argv) != 2:
    print("Usage: python import.py characters.csv")
    exit(1)
open(f"students.db", "w").close()
db = cs50.SQL("sqlite:///students.db")
db.execute("CREATE TABLE students (first TEXT, middle TEXT, last TEXT, house TEXT, birth NUMERIC)")
with open(sys.argv[1], "r") as titles:
    # Create DictReader
    reader = csv.reader(titles)
    next(reader)
    # Iterate over TSV file
    for row in reader:
        name = []
        house = row[1]
        birth = row[2]
        name = row[0].split(" ")
        if len(name) == 3:
            first = name[0]
            middle = name[1] 
            last = name[2]
            db.execute("INSERT INTO students (first, middle, last, house, birth) VALUES(?, ?, ?, ?,?)",
                       first, middle, last, house, birth)  
        else:
            first = name[0]
            last = name[1]
            db.execute("INSERT INTO students (first, middle, last, house, birth) VALUES(?, ?, ?, ?,?)",
                       first, None, last, house, birth)