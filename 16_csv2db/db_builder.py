#Team FLIPS_TABLES (Roster: Puneet Johal and Ahnaf Hasan)
#SoftDev1 pd07
#K16: No Trouble
#2018-10-04

import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

#==========================================================
#INSERT YOUR POPULATE CODE IN THIS ZONE


command = "CREATE TABLE courses ( code TEXT, mark INTEGER, id INTEGER )" #build SQL stmt, save as string
c.execute(command) #run SQL statement
with open("./data/courses.csv") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        code = row['code']
        mark = row['mark']
        id = row['id']
        command = 'INSERT INTO courses VALUES(\"' + code + '\", \"' + mark + '\", \"' + id + '\")'
        c.execute(command)
        print(row['code'], row['mark'], row['id'])

command = "CREATE TABLE occupations ( Job Class TEXT, Percentage TEXT )"
c.execute(command)
with open("./data/occupations.csv") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        tmpRow = row['Job Class']
        percent = row['Percentage']
        command = 'INSERT INTO occupations VALUES(\"' + tmpRow + '\", \"' + percent + '\")'
        c.execute(command)
        print(tmpRow, percent)

command = "CREATE TABLE peeps ( name TEXT, age INTEGER, id INTEGER )"
c.execute(command)
with open("./data/peeps.csv") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        name = row['name']
        age = row['age']
        iD = row['id']
        command = 'INSERT INTO peeps VALUES(\"' + name + '\", \"' + age + '\", \"' + iD + '\")'
        c.execute(command)
        print(row['name'], row['age'], row['id'])


#==========================================================

db.commit() #save changes
db.close()  #close database
