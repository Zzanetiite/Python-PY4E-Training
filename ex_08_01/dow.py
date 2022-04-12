han = open('mbox-short.txt')

for line in han :
    line = line.rstrip()
    #print('Line:', line)
    #if line == '' :
        #print("Skip Blank")
        #continue
    wds = line.split()
    #print('Words:', wds)
    #Guardian pattern and a compound statement (guardian comes before compound statement)
    if len(wds) < 3 or wds[0] != 'From' :
        #print("Ignore")
        continue
    print(wds[2])
