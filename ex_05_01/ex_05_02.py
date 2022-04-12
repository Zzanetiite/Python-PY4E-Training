sval = input('Please enter a value or "done":')
largest = None
smallest = None

while True:
    sval = input('Please enter a value or "done":')
    if sval == "done" :
        break
    try:
        fval = float(sval)
    except:
        print("Invalid input")
        continue
    if smallest is None :
        smallest = fval
    elif smallest > fval :
        smallest = fval
    elif largest is None :
        largest = fval
    elif largest < fval :
        largest = fval
print("Maximum is", int(largest))
print("Minimum is", int(smallest))
