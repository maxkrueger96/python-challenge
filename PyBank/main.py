import csv
import os

#Function opens the data file, writes it to a generator, and closes the file
def loadgen():
    datapath = '/Users/maxkrueger/Documents/NUBootcamp/03-Python/Homework/due_July14/Instructions/PyBank/Resources/budget_data.csv'
    with open(datapath) as datafile:
        reader = csv.reader(datafile)
        next(reader)
        for rows in reader:
            yield rows

#Function returns the number of months
def entrycount():
    gen = loadgen()
    entrycount = sum((1 for x in gen))
    return entrycount

#fnc will split the data generator into two generator
# returns either money or profits
def split_rows(generator,index):
    format_elems = lambda x: x.replace(' ','').replace('\'','')[1:-1].split(',') #Removes brackets and quotes from the rows, leaving the data
    l = [format_elems(str(rows)) for rows in generator]
    months = list(zip(*l))[0]
    profits = list(map(lambda x: int(x),list((zip(*l)))[1]))
    if index == "m":
        return months
    else:
        return profits

#net profits
def netprof():
    np = sum(split_rows(loadgen(),'p'))
    return np

#ch-ch-ch-ch-changes
def changes():
    deltalist = (split_rows(loadgen(),'p')[i+1]-split_rows(loadgen(),'p')[i] for i in range(entrycount()-1))
    return deltalist

# #format negative values correctly
def dollarform(amount):
    if amount >= 0:
        return "${:,.2f}".format(amount)
    else:
        return "-${:,.2f}".format(-amount)

#find average change
def floatavg():
    netchange = sum(changes())
    total = sum((1 for x in changes()))
    avg = netchange / total
    return dollarform(avg)

#find greatest increase
def maxinc():
    intinc = max(changes())
    dollarinc = dollarform(intinc)
    return dollarinc

#find greatest decrease
def maxdec():
    intdec = min(changes())
    dollardec = dollarform(intdec)
    return dollardec

#find corresponding months
def findmonth(extremum):
    l = list(changes())
    j = l.index(extremum(changes()))
    month = split_rows(loadgen(),'m')[j+1]
    return month

#print analysis
analysis = '\nFinancial Analysis\n' + \
'$' + '-'*50 + '$' + \
'\nTotal Months: ' + str(entrycount()) + \
'\nNet Total Profits: ' + str(netprof()) + \
'\nAverage Change Between Months: ' + str(floatavg()) + \
'\nGreatest Increase in Profits: ' + findmonth(max) + ' (' + str(maxinc()) + ') ' + \
'\nGreatest Decrease in Profits: ' + findmonth(min) + ' (' + str(maxdec()) + ')' + \
'\n '

#let's make it cool
def border(text):
    lines = text.splitlines()
    width = max(len(s) for s in lines)
    topbott = int((width + 5)/2) - 10
    newlines = []
    for i in range(len(lines)):
        cenline = lines[i].center(width)
        newlines.append(cenline)
    res = ['$ ' + ' $ '*topbott + ' $']
    for s in newlines:
        res.append('$    ' + s + '   $')
    res.append('$ ' + ' $ '*topbott + ' $')
    return '\n'.join(res)

#print analysis
print(border(analysis))

#now to export the analysis
txt = '/Users/maxkrueger/Documents/NUBootcamp/python-challenge/PyBank/Analysis/Analysis.txt'

#need the filesize for writing fnc
def filesize(p):
    return os.path.getsize(p)

#this function checks if the existing file is empty, fills it if it is
#if the file is written already, this fnc prompts the user to say whether they'd like to update the exisitng txt anyway

def checkwritefile(f):
    of = open(f,"r+")
    if filesize(f) == 0:
        of.write(border(analysis))
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
