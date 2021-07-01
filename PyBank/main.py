import csv
import os

# load in the data
csvfile = open('/Users/maxkrueger/Documents/NUBootcamp/python-challenge/PyBank/Resources/budget_data.csv','r')
reader = csv.reader(csvfile)

#make into list, delete header
readerlist = list(reader)
header = readerlist.pop(0)
entrynum = len(readerlist)

#split the data into two lists
months = []
profits = []

for i in range(entrynum):
    month = readerlist[i][0]
    profit = int(readerlist[i][1])
    
    months.append(month)
    profits.append(profit)

#number of months
monthnum = len(months)

#net profits
netprof = sum(profits)

#ch-ch-ch-ch-changes
changes = []

for i in range(entrynum-1):
    change = profits[i+1] - profits[i]

    changes.append(change)

#find average change
floatavg = sum(changes) / len(changes)

#format negative values correctly
def dollarform(amount):
    if amount >= 0:
        return "${:,.2f}".format(amount)
    else:
        return "-${:,.2f}".format(-amount)

#convert float to dollar
avgchange = dollarform(floatavg)

#find greatest increase
intinc = max(changes)
maxinc = dollarform(intinc)

#find greatest decrease
intdec = min(changes)
maxdec = dollarform(intdec)

#find corresponding months
incindex = changes.index(intinc)
decindex = changes.index(intdec)
incmonth = months[incindex+1]
decmonth = months[decindex+1]

#print analysis
analysis = '\nFinancial Analysis\n' + \
'$' + '-'*50 + '$' + \
'\nTotal Months: ' + str(monthnum) + \
'\nNet Total Profits: ' + str(netprof) + \
'\nAverage Change Between Months: ' + str(avgchange) + \
'\nGreatest Increase in Profits: ' + incmonth + ' (' + str(maxinc) + ') ' + \
'\nGreatest Decrease in Profits: ' + decmonth + ' (' + str(maxdec) + ')' + \
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

#append to txt file
txt = open('/Users/maxkrueger/Documents/NUBootcamp/python-challenge/PyBank/Analysis/Analysis.txt','a')
filesize = os.path.getsize('/Users/maxkrueger/Documents/NUBootcamp/python-challenge/PyBank/Analysis/Analysis.txt')
if filesize == 0:
    txt.write(border(analysis)) and txt.close()
    print('File Written')
else:
    print('File Already Written')


    
