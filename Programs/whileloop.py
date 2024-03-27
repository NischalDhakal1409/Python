#Example of while loop
i=1
while i < 5:
    print("Hey")
    i +=1

#Break Statement
i = 1
while i<6:
    print("Continue")
    if i == 3:
        break
    i +=1

#Continue Statement
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

#Else statement
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")