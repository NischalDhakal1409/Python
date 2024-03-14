#Defining variable
a = "Smith"
b = 20
print(a)
print(b)

#Assigning multiple variables in single line
name, age, height = "Kevin", 21, 5

print(name)
print(age)
print(height)

#Global Variable
x = "programming language."

def myfunc():
  print("Python is " + x)

myfunc()

#Global Keyword
def myfunc():
  global x
  x = "high level programming language"

myfunc()
print("Python is " + x)

#Local Variable   
def f():
    s = "I love python"
    print(s)

f()