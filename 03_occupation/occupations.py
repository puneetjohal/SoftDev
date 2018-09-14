#ASTROWORLD - Rubin P., Puneet J., Ryan A.
#K06 - Divine Your Destiny!
#Period 7
#2018-09-13

from random import choices

def parse_data(filename):
    file = open(filename, 'r')  #open the file in read mode
    raw = file.read()           #get the text
    list = raw.split("\n")      #split on new lines

    counter = 0
    while counter < len(list):  #loop thru it, splitting it on commas
        #remove unecessary quotes
        if '"' in list[counter]:        
            list[counter] = list[counter].replace('"', '')

        #splits on the last instance of a comma, once
        list[counter] = list[counter].rsplit(',', 1)
        counter += 1
    
    #make the empty dictionary and loop thru
    #the raw data of the file
    dict = {}
    counter = 1
    while counter < len(list) - 2:
        dict[list[counter][0]] = float(list[counter][1])
        counter += 1

    #print(dict) #diagnostic print statement
    return dict

def pick_job(dict):
    jobs = list(dict.keys()) #list of keys
    values = []              #empty list to be filled with values

    #loop thru the dict to get the weights/values
    for key in jobs:
        values.append(dict[key])

    #diagnostic print statements
    #print(values)
    #print(jobs)

    #uses the choices method in random which allows for one to pick from a list of items
    #and have it be weighted
    job = choices(jobs, values)
    return job[0]

print(pick_job( parse_data('occupations.csv') ))
