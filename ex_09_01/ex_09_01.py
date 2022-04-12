fname = input('Enter File: ')
if len(fname) < 1 : fname = 'clown.txt'
hand = open(fname)

di = dict()
for line in hand :
    line = line.rstrip()
    #print(line)
    wds = line.split()
    #print(wds)
    for w in wds :
        #An idiom : Retrieve/create/update class counter
        di[w] = di.get(w,0) + 1



#        #if the key is not there the count is 0
#        oldcount = di.get(w,0)
#        print(w,'old', oldcount)
        # since the key is not there add one to old count and add newcount to dictionary
#        newcount = oldcount + 1
#        di[w] = newcount
#        print(w,'new', newcount)



#        if w in di :
#            di[w] = di[w] + 1
            #print('**Existing**')
#        else :
#            di[w] = 1
            #print('**New**')
#        print(w, di[w])
        #print(w)

print(di)

#Now we want to find the most common word
largest = -1
theword = None
for key,value in di.items() :
    print(key,value)
    if value > largest :
        largest = value
        theword = key
print('Done', theword, largest)
