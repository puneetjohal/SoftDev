#Team randomlyMerged (Roster: Ahnaf Hasan and Puneet Johal)
#SoftDev1 pd07
#K02 -- NO-body expects the Spanish Inquisition!
#2018-09-08

#import to use random functions
import random

#given data
KREWES = {
        'w': ['William Lu', 'Qian', 'Peter', 'Ahnaf', 'Kenny', 'Sophia', 'Sajed', 'Emily', 'Hasif', 'Brian ', 'Dennis', 'Jiayang', 'Shafali ', 'Isaac ', 'Tania', 'Derek', 'Shin', 'Vincent', 'Ricky', 'Puneet', 'Wei Wen', 'Tim', 'Jeffrey', 'Joyce ', 'Mohtasim', 'Simon', 'Thomas', 'Ray', 'Jack', 'Karen', 'Robin', 'Jabir', 'Johnny ', 'Matthew', 'Johnson Li', 'Angela', 'Crystal', 'Jiajie', 'Theodore (Dont really care)', 'Anton', 'Max', 'Bo', 'Andrew', 'Kendrick', 'Kevin', 'Kyle', 'Jamil', 'Mohammed', 'Ryan', 'Jason'],
        'm': ['Daniel', 'Aleksandra', 'Addison', 'Hui Min', 'Aaron', 'Rubin', 'Raunak', 'Stefan', 'Cheryl', 'Cathy', 'Mai', 'Claire ', 'Alex', 'Bill', 'Daniel', 'Jason'],
        'x': ['Derek', 'Britni', 'Joan', 'Vincent', 'Jared', 'Ivan', 'Thomas', 'Maggie', 'Damian', 'Tina', 'Fabiha', 'John', 'Susan ', 'Kaitlin', 'Michelle', 'Clara', 'Rachel', 'Amit', 'Jerry', 'Raymond', 'Zane', 'Soojin', 'Maryann', 'Adil', 'Josh', 'Imad']
}

"""Chooses the list randomly. This is based on the length of the
list. 
Returns a list"""
def randListChoose():
    #choose the number that will correspond to the key
    randListNum = random.randint(1, len(KREWES))
    #first key is the initial value to prevent errors
    chosenList = 'w'
    #counter set up for the following FOR loop
    counter = 1
    #FOR loop
    for key in KREWES:
        #if the FOR loop has stepped on the randomly chosen key
        if (counter == randListNum):
            #set the chosen key as curr key
            chosenList = key
            #avoid unneeded(?) looping for larger dictionaries
            break
        else:
            #key is not the chosen key, move on and keep the counter going
            counter += 1
    #debug reasons
    print(chosenList)
    return chosenList
"""Chooses a value from the dictionary key given. 
Returns a string"""
def randNameChoose(givenList):
    #placeholder to avoid errors
    theName = 'placeholder'
    #values that correspond to the key
    theList = KREWES[givenList]
    #empty key
    if (len(theList) == 0):
        print("Doesn't work, list does not exist")
        return 1
    else:
        #random.choice(seq) --- chooses random element from sequence
        theName = random.choice(theList)
    return theName
    
def randChoose():
    list = randListChoose()
    name = randNameChoose(list)
    print("The chosen one is from the " + list + " clan and was called into battle as " + name + " The Mighty")
    
randChoose()
