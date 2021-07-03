import csv
import decimal
from decimal import *
import gc
import os

with open('/Users/maxkrueger/Documents/NUBootcamp/python-challenge/PyPoll/Resources/election_data.csv','r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)

#we can do without the county values for this specific analysis
    readerlist = [(rows[0],rows[2]) for rows in reader]

#total # of votes
def votetotal():
    return len(readerlist)

#the set of candidates
def candis():
    candilist = list({readerlist[i][1] for i in range(votetotal())})
    return candilist

def idlist(candidate):
    lst = [readerlist[i][0] for i in range(votetotal()) if readerlist[i][1]==candidate]
    return lst

#vote totals for each candidate
def lenlist(candidate):
    return len(idlist(candidate))

def sortcandis():
    sorting = sorted(candis(),key=lenlist, reverse=True)
    return sorting

#total percentage of the vote per candidate
def votepercent(candidate):
    q = lenlist(candidate) / float(votetotal())
    p = round(q*100)
    return p

def sortperc(numstr):
    perc = [votepercent(x) for x in candis()]
    sort = sorted(perc, reverse=True)
    if numstr == str:
        return ["{:.2f}%".format(x) for x in sort]
    elif numstr == decimal:
        return sort

#determine the winner
def winner():
    winperc = max(sortperc(decimal))
    i = sortperc(decimal).index(winperc)
    return "Winner: " + sortcandis()[i]

#print analysis
def stars(n):
    return "*"*n

#totally unnecessary but fun to write
def breakdown():
    candiperc = {sortcandis()[n]:"{:.2f}%".format(votepercent(sortcandis()[n])) for n in range(4)}
    mapcp = map(": ".join,candiperc.items())
    quickslice = lambda x: int(x.split(": ")[1].split(".")[0])
    sortmap = sorted(mapcp,key=quickslice,reverse=True)
    addlist = {sortmap[n]:"({})".format(str(lenlist(sortcandis()[n]))) for n in range(4)}
    finalmap = map(" ".join,addlist.items())
    scndslice = lambda x: int(x.split(": ")[1].split(".")[0])
    breakdown = sorted(finalmap,key=scndslice,reverse=True)
    return '''\n'''.join(breakdown)

def analysis():
    return stars(25)+'''\nElection Results\n'''+stars(25)+ '''\nTotal Votes: '''+str(votetotal())+ '''\n'''+stars(25)+'''\n'''+breakdown()+'''\n'''+stars(25)+ '''\n'''+winner()+'''\n'''+stars(25)+'''\n'''

def border(text):
    lines = text.splitlines()
    width = max(len(s) for s in lines)
    topbott = int((width + 5)/2)-5
    newlines = []
    for i in range(len(lines)):
        cenline = lines[i].center(width)
        newlines.append(cenline)
    res = ['• ' + ' • '*topbott + ' •']
    for s in newlines:
        res.append('•    ' + s + '   •')
    res.append('• ' + ' • '*topbott + ' •')
    return '\n'.join(res)

gc.disable()
analysis = border(analysis())
print(analysis)

#write to txt file
txt = '/Users/maxkrueger/Documents/NUBootcamp/python-challenge/PyPoll/Analysis/Analysis.txt'
def filesize(p):
    return os.path.getsize(p)

def checkwritefile(f):
    of = open(f,"r+")
    if filesize(f) == 0:
        of.write(analysis)
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
                of.write(border(analysis))
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