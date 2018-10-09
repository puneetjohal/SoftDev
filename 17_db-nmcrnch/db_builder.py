#Team Where's Perry? -- Puneet Johal and Rachel Ng
#SoftDev1 pd07
#K17 -- Average
#2018-10-09

import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O
import os

DB_FILE="discobandit.db"

if os.path.isfile(DB_FILE):
    os.remove(DB_FILE)

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

#==========================================================
#INSERT YOUR POPULATE CODE IN THIS ZONE

#CREATION OF TABLES
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
        #print(row['code'], row['mark'], row['id'])

command = "CREATE TABLE occupations ( Job Class TEXT, Percentage TEXT )"
c.execute(command)
with open("./data/occupations.csv") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        tmpRow = row['Job Class']
        percent = row['Percentage']
        command = 'INSERT INTO occupations VALUES(\"' + tmpRow + '\", \"' + percent + '\")'
        c.execute(command)
        #print(tmpRow, percent)

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
        #print(row['name'], row['age'], row['id'])

#SEARCHING THROUGH TABLES
command = "SELECT id, mark FROM courses WHERE id > 0"
cur = c.execute(command)
all = cur.fetchall()
gradebook = {}
itr = 0 #iterator
for elements in all: #constructs a dictionary where the student ids are keys and the values are a list of their grades
    if all[itr][0] in gradebook:
        gradebook[all[itr][0]].append(all[itr][1])
    else:
        gradebook[all[itr][0]] = [all[itr][1]]
    itr+=1
#print(gradebook) #diagnostic print statement

def avg(nums):
    sum = 0
    numofnums = 0
    for num in nums:
        sum += num
        numofnums += 1
    return sum/numofnums

command = "SELECT id, name FROM peeps WHERE id > 0"
cur = c.execute(command)
all = cur.fetchall()
alldata = []
ids = gradebook.keys()
for id in ids: #makes a list of lists, sublists contain ids and averages
    alldata.append([id,avg(gradebook[id])])
for element in all: #appends name to sublists
    itr = 0 #iterator
    while element[0] != alldata[itr][0]:
        itr += 1
    alldata[itr].append(element[1])
#display each student's name, id, and average
for element in alldata:
    print (element[2], element[0], element[1])

#CREATE TABLE PEEPS_AVG
command = "CREATE TABLE peeps_avg (ID INTEGER, average REAL)"
c.execute(command)
for element in alldata:
    ID = element[0]
    average = element[1]
    command = 'INSERT INTO peeps_avg VALUES(\"' + str(ID) + '\", \"' + str(average) + '\")'
    c.execute(command)

#==========================================================

db.commit() #save changes
db.close()  #close database
