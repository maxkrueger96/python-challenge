import csv
import decimal
from decimal import *
import gc
import os

#fnc to loads data into generator as needed
#we really don't need to carry around the data for the counties
#converts csv reader to generator of tuples
def loadgen():
    datapath = '/Users/maxkrueger/Documents/NUBootcamp/python-challenge/PyPoll/Resources/election_data.csv'
    with open(datapath) as datafile:
        reader = csv.reader(datafile)
        next(reader)
        for rows in reader:
            yield (rows[0], rows[2])                                 

#fnc totals # of votes
def votetotal():
    counter = (1 for x in loadgen())
    return sum(counter)

#the set of candidates
def candis():
    toset = {rows[1] for rows in loadgen()}
    candilist = list(toset)
    return candilist

#fnc to filter ids by candidate
def quickid(candidate):
    condition = lambda element: candidate in element
    return condition

#runs said filter
def idfilter(candidate):
    idfilter = filter(quickid(candidate),loadgen())
    return idfilter

#count votes in the filtered generator
def indivotes(candidate):
    filter = idfilter(candidate)
    counter = (1 for x in filter)
    return sum(counter)

#sort candidates numerically by total vote count
def sortcandis():
    sorting = sorted(candis(), key = indivotes, reverse=True)
    return sorting

#total percentage of the vote per candidate
#returns percentage as string
def votepercent(candidate):
    q = indivotes(candidate) / float(votetotal())
    p = round(q*100)
    return "{:.2f}%".format(p)
    
#determine the winner
def winner():
    return sortcandis()[0]

#fnc to return the breakdown of individual candidate performance
def breakdown():
    candiperc = (f"{x}: {votepercent(x)} ({str(indivotes(x))})" for x in sortcandis())
    joinedlist = '''\n'''.join(candiperc)
    return joinedlist

#fnc to return final analysis
def analysis():
    return \
    '*'*25 + \
    '''\nElection Results\n''' + \
    '*'*25 + \
    '''\nTotal Votes: ''' + str(votetotal()) + \
    '''\n''' + '*'*25 + \
    '''\n''' + breakdown() + \
    '''\n''' + '*'*25 + \
    '''\n''' + winner() + \
    '''\n''' + '*'*25 + \
    '''\n'''

#fnc adds a fun border with dynamic sizing around text
def border(text):
    lines = text.splitlines()
    width = max(len(s) for s in lines)
    topbott = int((width + 5)/2)-5
    newlines = []
    for i in range(len(lines)):
        cenline = lines[i].center(width)
        newlines.append(cenline)
    res = ['* ' + ' * '*topbott + ' *']
    for s in newlines:
        res.append('*    ' + s + '   *')
    res.append('* ' + ' * '*topbott + ' *')
    return '\n'.join(res)

print(border(analysis()))

#write to txt file
txt = '/Users/maxkrueger/Documents/NUBootcamp/python-challenge/PyPoll/Analysis/Analysis.txt'
def filesize(p):
    return os.path.getsize(p)

def checkwritefile(f):
    of = open(f,"r+")
    if filesize(f) == 0:
        of.write(border(analysis()))
        of.close()
        print('File Written')
    else:
        while True:
            dirs = of.name.split("/")
            ind = len(dirs)-1
            fname = dirs[ind]
            update = input("Would you like to update "+fname+"? (y/n): ")
            update
            if update.lower() == 'yes' or update.lower() == 'y':
                of.truncate(0)
                of.write(border(analysis()))
                of.close()
                print("File Updated")
                break
            elif update.lower() == "no" or update.lower() == "n":
                of.close()
                print("File Closed")
                break
            else:
                print("Invalid Response")

checkwritefile(txt)