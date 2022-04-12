import re

fname = input('Enter File: ')

if len(fname) < 1 : fname = 'regex_sum_42.txt'
fhand = open(fname)

numberlist = list()
count = 0

for line in fhand :
    line = line.rstrip()
    y = re.findall('[0-9]+',line)
    if len(y) < 1 :
        continue
    else :
        for number in y :
            numberlist.append(float(number))
            count = count +1
            #print(number, count)
print(sum(numberlist))
