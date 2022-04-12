score = input("Enter Score: ")
sc = float(score)

if sc > 0.0 :
  #print("Yes1")
  ch = 1.0
if sc <= 1.0 :
  #print("Yes2")
  ch = 1.0
if sc < 0.0 :
  #print("Yes3")
  ch = -1.0
if sc > 1.0 :
  #print("Yes4")
  ch = -1.0
if ch != 1.0 :
  print("Value out of range.")
  quit()
if ch == 1.0 :
  if sc >= 0.9 :
    print("A")
  elif sc >= 0.8 :
    print("B")
  elif sc >= 0.7 :
    print("C")
  elif sc >= 0.6 :
    print("D")
  elif sc < 0.6 :
    print("F")
