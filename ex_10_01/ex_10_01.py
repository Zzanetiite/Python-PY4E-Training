fname = input('Enter File: ')
if len(fname) < 1 : fname = 'clown.txt'
hand = open(fname)

di = dict()
for line in hand :
    line = line.rstrip()
    wds = line.split()
    for w in wds :
        di[w] = di.get(w,0) + 1
#print(di)

x = sorted([(v,k) for k,v in di.items()], reverse=True)
print(x[:5])
