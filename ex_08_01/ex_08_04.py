filename = input("Enter the file name: ")
filehandle = open(filename)

thelist = list()

for line in filehandle :
    line = line.rstrip()
    words = line.split()
    for word in words :
        if word == word in thelist :
            continue
        thelist.append(word)
thelist.sort()
print(thelist)
