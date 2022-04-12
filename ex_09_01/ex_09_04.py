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
    theemail = words[1]
    #print(theemail)
    dictionary[theemail] = dictionary.get(theemail,0) + 1
#print(dictionary)

largest = 0
thesender = None

for key, value in dictionary.items() :
    if value > largest :
        largest = value
        thesender = key
print(thesender, largest)
