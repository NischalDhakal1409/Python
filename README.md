# Python Learning
I will be learning python programming from the basics and will be uploading everything that I have learned in this repository.
# Resources
I am learning python currently following the tutorial from youtube alongside W3schools. Beside that, any further resources that I will follow up in the future, I will upload over here.

<a href="https://youtu.be/XKHEtdqhLK8?si=pwxzVEKWyC3vqEFV)https://youtu.be/XKHEtdqhLK8?si=pwxzVEKWyC3vqEFV">Youtube</a> <br>
<a href = "https://www.w3schools.com/python/default.asp"> W3schools</a>
# Chapters
## Introduction to Python 
Python is a popular high level programming language. It is used in different fields like web development, data science, software development and system scripting. It is also used to connect with the database system and read and modify the files. It is popular because of it's simple syntax. In addition to this, it works on different platforms like Windows, Mac, Linux, etc. Also, it can be treated in procedural way or object oriented way or functional way.

Below is the simple example of python programming.

```
print ("Hello World!")
```
## Comments
Comments is used to explain what the code is about. It makes the code more readable. It can be done by using #.
```
#This is comment
print("Checking Comment")
```
## Variables
Variables are the containers that hold a value or data. It is essential for storing and manipulating data in programming. In python, a variable is created the moment you first assign a value to it.
```
a = "Smith"
b = 20
print(a)
print(b)
```
We can assign multiple variables in a single line of code thus reducing the code length and making it efficient.
```
name, age, height = "Kevin", 21, 5
print(name)
print(age)
print(height)
```
Variables are of two type based on the place where they are defined. They are
1. Global Variable
   
Variables that are created outside of a function (as in all of the examples above) are known as global variables. Global variables can be used by everyone, both inside of functions and outside.
```
x = "programming language."

def myfunc():
  print("Python is " + x)

myfunc()
```
Global variable can also be created inside a function by using global keyword.
```
def myfunc():
  global x
  x = "high level programming language"

myfunc()
print("Python is " + x)
```
2. Local Variable
   
Local variables in Python are those which are initialized inside a function and belong only to that particular function. It cannot be accessed anywhere outside the function.
```
def f():
    s = "I love python"
    print(s)

f()
```
## Data Types in Python
In Python, Basically we have 4 different types of data types. They are:
  1. String
     
  String in python are denoted in either single quotation marks or double quotation marks. To assign a variable with string, we can write a variable name followed by equals to sign and string written in    quotation.
  ```
name = "Ram"
print(name)
```

  We can concat string in the python by using "+" symbol.
  ```
first_name = "John"
last_name = "Smith"
full_name = first_name + last_name
print(last_name)
```

  2. Integer

Integer are the whole number, negative or positive without a decimal. To assign a variable with integer, we can write a variable name followed by equals to sign and integer.
```
age = 20
print(age)
```
We can combine integer and string in python by converting the integer in string form as shown below.
```
age = 21
print("Your age is: " + str(age))
```

  3.Float
  
Float, "Floating Point Number" is a number, positive or negative, containing one or more decimals. To assign a variable with float, we can write a variable name followed by equals to sign and float. 
```
height = 55.6
print(height)
```
We can combine float and string in python by converting the float in string form as shown below.
```
height = 55.6
print("Your height is : " + str(height))
```

  4.Boolean

Boolean represents either one of these values, true or false. It is often used to compare the two values. To assign a variable with boolean, we can write a variable name followed by equals to sign and boolean. 
```
ans = True
print(ans)
```
We can combine boolean and string in python by converting the bolean in string form as shown below.
```
ans = True
print("Your ans is " + str(panda))
```
To know the type of the variable, we can find by using the "type"
```
name = "Kevin"
height = 55.5
print(type(name))
print(type(height))
```
## Multiple Assignment 
This features allows us to assign mutliple variables at the same time in one line of code 

## String Methods
Python has a set of built in methods that we can use on strings.

| Method        | Description |
| ------------- | ------------- |
| len()  | helps to find the length of string |
| find()  | helps to find the specified alphabet in the string  |
| capitalize()  | converts the first charatcer to capital |
| upper()  | converts the string into uppercase  |
| lower()  | converts the string into lowecase  |
| isalpha()  | returns True if all characters in the string are in the alphabet  |
| isalnum()  | returns True if all characters in the string are in the alphanumeric  |
| count()  | ounts and displays how many times is the specified alphabet is used in string.  |
| replace()  | replaces the target alphabet with the another alphabet in the string  |

Below is the example demonstrating the use of all above string methods.
```
name = "Smith"

print(len(name))
print(name.find("i"))
print(name.capitalize())
print(name.upper())
print(name.lower())
print(name.isalnum())
print(name.isalpha())
print(name.count("i"))
print(name.replace("i","z"))
```




















