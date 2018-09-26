#Team Johalapenoccupations - William Lu and Puneet Johal
#K10 - Jinja Tuning
#Period 7
#2018-09-23

from flask import Flask, render_template
import random

app = Flask(__name__)

#parse through the csv file
def parse(inputfile):
    file = open(inputfile, 'r')  #open the file in read mode
    raw = file.read()           #get the text
    return raw.split("\n")      #split on new lines + return list of lines

#separate jobs from percentages
def separate(inputlist):
    index = 0
    while index < len(inputlist):
        if '"' in inputlist[index]:
            inputlist[index] = inputlist[index].replace('"', '') #remove extra quotes
        inputlist[index] = inputlist[index].rsplit(',', 1) #split at last comma in line (the one before the percetage)
        index += 1

#feed info into dictionary
def listToDict(inputlist):
    jobs = {}
    line = 1 #skips table header
    while line < (len(inputlist) - 2):
        jobs[inputlist[line][0]] = float(inputlist[line][1]) #Each even index element (job) becomes a key, and the odd index element right after it becomes the value
        line += 1
    return jobs

#random job selection
def randomJob(dictionary):
    keys = list(dictionary) #returns list of all keys in dict
    return random.choice(keys)


@app.route("/")
def redirect():
    return 'Add "/occupations" to url'

@app.route("/occupations")
def display():
  lines = parse('data/occupations.csv')
  separate(lines)
  jobs = listToDict(lines)
  return render_template("seed.html",
						 title = 'Random occupation generator',
						 head0 = 'Job Class',
                         head1 = 'Percentage',
						 dict = jobs,
						 val = randomJob(jobs))

if __name__ == "__main__":
    app.debug == True
    app.run()
