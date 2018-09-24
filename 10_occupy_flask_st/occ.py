#Team Johalapenoccupations - William Lu and Puneet Johal
#K10 - Jinja Tuning
#Period 7
#2018-09-23

from flask import Flask, render_template
import random

app = Flask(__name__)

#parse through the file
file = open('occupations.csv', 'r')  #open the file in read mode
raw = file.read()           #get the text
lst = raw.split("\n")      #split on new lines

#separate jobs from percentages
cnt = 0
while cnt < len(lst):
    if '"' in lst[cnt]:
        lst[cnt] = lst[cnt].replace('"', '')
    lst[cnt] = lst[cnt].rsplit(',', 1)
    cnt += 1

#feed info into dictionary
dict = {}
cnt = 1
while cnt < len(lst) - 2:
    dict[lst[cnt][0]] = float(lst[cnt][1])
    cnt += 1

#random job selection
def randomJob():
    keys = list(dict)
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
