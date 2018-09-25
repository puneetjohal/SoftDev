#Team Johalapenoccupations - William Lu and Puneet Johal
#K10 - Jinja Tuning
#Period 7
#2018-09-23

from flask import Flask, render_template
import random

app = Flask(__name__)

#parse through the file
def parse(inputfile):
    file = open(inputfile, 'r')  #open the file in read mode
    raw = file.read()           #get the text
    return raw.split("\n")      #split on new lines

#separate jobs from percentages
def separate(inputlist):
    cnt = 0 #counter
    while cnt < len(inputlist):
        if '"' in inputlist[cnt]:
            inputlist[cnt] = inputlist[cnt].replace('"', '')
            inputlist[cnt] = inputlist[cnt].rsplit(',', 1)
            cnt += 1

#feed info into dictionary
def listToDict(inputlist)
    jobs = {}
    cnt = 1 #counter
    while cnt < len(inputlist) - 2:
        jobs[inputlist[cnt][0]] = float(inputlist[cnt][1]) #Each even index element (job) becomes a key, 
        #and the odd index element right after it becomes the value
        cnt += 1
    return jobs

#random job selection
def randomJob(dictionary):
    keys = list(dictionary) #returns list of all keys in dict
    return random.choice(keys)

@app.route("/occupations")
def display():
  return render_template("seed.html",
						 title = 'random occupation generator',
						 head0 = 'Job Class',
                         head1 = 'Percentage',
						 dict = dict,
						 val = randomJob())

if __name__ == "__main__":
    app.debug == True
    app.run()
