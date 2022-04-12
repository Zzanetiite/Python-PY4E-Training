filename = input('Enter File: ')
if len(filename) < 1 : filename = 'mbox-short.txt'
filehandle = open(filename)


dictionary = dict()
for line in filehandle :
    line = line.rstrip()
    if line == '' :
        #print("Skipped")
        continue
    words = line.split()
    if len(words) < 3 or words[0] != 'From' :
        continue
    thetime = words[5]
    #print(thetime)
    thehour = thetime[0:2]
    #print(thehour)
    dictionary[thehour] = dictionary.get(thehour,0) + 1

sorteddictionary = (sorted(dictionary.items()))

for key, value in sorteddictionary :
    print(key, value)
