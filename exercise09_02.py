#Exercise 2: Write a program that categorizes each mail message by which day of the week the commit was done. To do this look for lines that start with “From”, then look for the third word and keep a running count of each of the days of the week. At the end of the program print out the contents of your dictionary (order does not matter).

# Use the file name mbox-short.txt as the file name
fname = input('Enter file name: ')
try:
    fh = open(fname)
except:
    print('File does not exist:', fname)
    quit()
#create dictionary
counts = dict()
#go through lines
for line in fh:
    line = line.rstrip()
    if len(line) < 1:
        continue
    if line.startswith('From '):
        linesplit = line.split()
        day = linesplit[2:3]
#fill in dictionary
    for d in day :
        counts[d] = counts.get(d,0) + 1
print(counts)