# TODO
import sqlite3
import cs50
import csv
import sys 
from sys import argv


if len(argv) != 2:
    print("Usage: python roster.py Gryffindor")
    exit(1)
    
open(f"students.db", "r").close()
db = cs50.SQL("sqlite:///students.db")
results = db.execute('SELECT first, middle, last, birth FROM students WHERE house = %s ORDER BY last, first', argv[1])
for students in results:
    if students['middle'] == None:
        print(f"{students['first']}", end=' ')
        print(f"{students['last']}", end=' ')
        print(', born in', end=' ')
        print(f"{students['birth']}")
    else:
        print(f"{students['first']}", end=' ')
        print(f"{students['middle']}", end=' ')
        print(f"{students['last']}", end=' ')
        print(', born in', end=' ')
        print(f"{students['birth']}")
