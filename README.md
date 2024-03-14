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
### Types of Variables
Variables are of two type based on the place where they are defined. They are
#### 1. Global Variable
   
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
#### 2. Local Variable
   
Local variables in Python are those which are initialized inside a function and belong only to that particular function. It cannot be accessed anywhere outside the function.
```
def f():
    s = "I love python"
    print(s)

f()
```
## Data Types in Python

Python has different data types built-in by default in these categories
| Types        | Categories |
| ------------- | ------------- |
| Text | str |
| Numeric | int, float, complex |
| Sequence | list, tuple, range |
| Mapping | dict |
| Set | set, frozenset |
| Boolean | bool |
| Binary | bytes, bytearray, memoryview |
| None | NoneType |

## Strings
Strings in python are surrounded by either single quotation marks or double quotation marks.
"Hello" is same as 'hello'
```
print("Hello World!")
```
### Assigning String to the variable
We can also assign string to the variable. It is done done with the variable name followed by an equal sign and the string.
```
name = "Smith"
print(name)
```
### Multiline Strings
We can assign multiline strings by using 3 quotes.
```
random = """Lorem ipsum dolor sit amet,
        consectetur adipiscing elit,
        sed do eiusmod tempor incididunt
        ut labore et dolore magna aliqua."""
print(random)
```
### String Slicing
### Escape Characters
### String Methods
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

## Numbers
### Types of Numeric Data Types
In Python, Basically we have 3 different types of numeric data types. They are:
 #### 1. Integer

Integer are the whole number, negative or positive without a decimal. To assign a variable with integer, we can write a variable name followed by equals to sign and integer.
```
a = 21
b = -10
print(a)
print(b)
```
  #### 2. Float
Float, "Floating Point Number" is a number, positive or negative, containing one or more decimals. To assign a variable with float, we can write a variable name followed by equals to sign and float. 
```
x = 55.6
y = -20.3
print(x)
print(y)
```
#### 3. Complex
Complex numbers are written with a "j" as the imaginary part.
```
c = 5j
d = 3+2j
print(c)
print(d)
```
## Math in Python
In Python, we have built-in math functions, including math module that allows us to perform mathematical tasks on numbers. There are different types of functions. Some are given below.
| Functions | Use |
| ------------- | ------------- |
| round() | str |
| ceil() | int, float, complex |
| floor() | list, tuple, range |
| abs | dict |
| Set | set, frozenset |
| Boolean | bool |
| Binary | bytes, bytearray, memoryview |
| None | NoneType |

```
import math
x = -2
pi = 3.14
a=3
b=4
c=1
print(round(pi))
print(math.ceil(pi))
print(math.floor(pi))
print(abs(x))
print(pow(x,2))
print(math.sqrt(5))
print(max(a,b,c))
print(min(a,b,c))

```

## If-else
## While loop
## For Loop












