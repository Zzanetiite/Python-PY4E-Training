num = 0
tot = 0
while True :
    sval = input('Enter a number or done: ')
    if sval == 'done' :
        break
    try:
        fval = float(sval)
    except:
        print('Invalid Iput')
        continue
    #print(fval)
    num = num + 1
    tot = tot + fval

#print('All Done')
print(tot, num, tot/num)
