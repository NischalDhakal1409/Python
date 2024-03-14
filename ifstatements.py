a = 20
b = 30

#Use of If statement

if b > a:
   print("b is greater than a")

#Use of elif statement

if b > a:
   print("b is greater than a")
elif b == a:
   print("They both are equal")

# Use of else statement
a=200
b=20

if b > a:
   print("b is greater than a")
elif b == a:
   print("They both are equal")
else:
   print("a is greater than b")

#Shorthand methods
   
if a > b: print("a is greater than b")   # For if statements
print (a) if a > b else print (b)        # For If-else statements

# Use of Logical Operator in Python

#Use of and
a = 30
b = 40
c = 10
if a > b and c > a:
   print("Both conditions are True")

#Use of Or
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True") 


#Use of Not
a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")