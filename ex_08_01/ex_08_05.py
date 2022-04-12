filename = input("Enter the file name: ")
filehandle = open(filename)

count = 0

for line in filehandle :
    line = line.rstrip()
    #print(line)
    if line == '' :
        #print("Skipped")
        continue
    words = line.split()
    if len(words) < 3 or words[0] != 'From' :
        continue
    count = count + 1
    print(words[1])

print("There were ", count, " lines in the file with From as the first word")
