# the word doc explains what is happening
b = 1.0000000009436436 #b value
a = 100000 #a value
iyears = input("How many years") #take input in years from the console
years = float(iyears) #converts to float
bx = b**years #caculates b^years
lightyears = '%f' % (bx * a) #light years
print("The universe will be", lightyears,"lightyears in",years,"years") #prints universe diameter light years 2 console
inches = '%f' % (lightyears * 31039141970409450*12) #caculates size in inches
print("The universe will be", inches,"inches in d",years,"years") #prints universe diameter size in inches to console
