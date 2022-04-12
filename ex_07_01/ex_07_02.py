filename = input("Enter file name: ")
filehandle = open(filename)

count = 0
valuesss = 0

for line in filehandle :
    if not line.startswith("X-DSPAM-Confidence:") :
        continue
    count = count + 1
    valuestarts = line.find(":")
    meanvalue = line[valuestarts+1:]
    value = float(meanvalue.strip())
    valuesss = valuesss + value
    #print(value, valuesum)

print("Average spam confidence:", valuesss/count)
