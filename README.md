# python-challenge
Repository for HW #3 Python Challenges: PyBank and PyPoll

I found this challenge useful in expanding my basic python jargon and techniques.
I learned basic python in 2014, for a few months, during college. Now, I feel as though I 
understand OOP as a concept more fully, and certainly feel more comfortable writing the code 
on the fly without needing to reference outside sources. Specifically, in an attempt to manage 
the large csv file we were given to work with in PyPoll, I played around extensively with the 
built-in data structures. Eventually, I ended up using generator functions and generator 
comprehensions to store most of the data and analysis, as their use of lazy evaluation speeds 
up the code as opposed to the way a list, for example, takes up memory. Such techniques 
weren't needed in the PyBank challege, as the data set was magnitudes smaller, but I thought 
it was good practice in Pythonic code to implement the same strategy as in PyPoll. My first 
goal was to move away from list.append, for loops, and global variables, and move towards list 
comprenshions, while loops, and using local variables inside functions. Then, I tried to 
replace as many lists as possible with generators. While the PyPoll code still takes longer 
than I'd like to run, I believe it would be even slower had I stuck to my original use of 
global variables and list.append.
