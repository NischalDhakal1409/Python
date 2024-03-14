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
## Comments in Python
Comments is used to explain what the code is about. It makes the code more readable. It can be done by using #.
```
#This is comment
print("Checking Comment")
```
## Variables in Python
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
### 1. Global Variable
   
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
### 2. Local Variable
   
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
String Slicing is the method of creating a substring by extracting elements from the other string. We can create it by two methods i.e. index[] or slice()
### Use of index[]
We can create a substring by extracting the elements from other string using index[]. We need to specify the start index and end index, separated by a colon, to return a part of the string. We can also specify steps to skip and extract substring following that steps.
The general format for indexing is [start:end:step]
```
name = "John Smith"
first_name = name[0:5]                  
last_name = name[5:11]                  
random_name = name[0:11:2]
print(first_name)
print(last_name)
print(random_name)
```
### Use of slice()
We can return a range of characters by using the slice syntax.We need to the start index and the end index, separated by a colon, to return a part of the string.
```
website = "https://www.google.com"
slice = slice(12,-4)
print(website[slice])
```
### Escape Characters
Escape character is the backslash followed by the character that causes escape from the normal interpretation of a string. There are different escape characters used in Python. Some of them are given below.
For example:
```
print("He is so called "rich" son of a college")
```
If we run the above code in python, python returns error as we have used multiple quotes inside a string. To fix this problem, we can use escape character.
```
print(" He is so called \"rich\" son of a college")
```
| Code | Result |
| ------------- | ------------- |
| \' | Single Quote |
| \n | New line |
| \\ | backslash |
| \t | tab |

### Use of escape characters
```
print("He is \'special\'")
print("He\\she ")
print("Rayne\t is a student")
print("He is a guy.\nHe is from Kathmandu")
```
### String Methods
Python has a set of built in methods that we can use on strings.

| Method | Description |
| ------------- | ------------- |
| len() | find the length of string |
| find() | find the specified alphabet in the string |
| capitalize()  | converts the first charatcer to capital |
| upper() | converts the string into uppercase |
| lower() | converts the string into lowecase |
| isalpha() | returns True if all characters in the string are in the alphabet |
| isalnum() | returns True if all characters in the string are in the alphanumeric |
| count() | counts and displays how many times is the specified alphabet is used in string. |
| replace() | replaces the target alphabet with the another alphabet in the string |

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

## Numbers in Python
### Types of Numeric Data Types
In Python, Basically we have 3 different types of numeric data types. They are:
 ### 1. Integer

Integer are the whole number, negative or positive without a decimal. To assign a variable with integer, we can write a variable name followed by equals to sign and integer.
```
a = 21
b = -10
print(a)
print(b)
```
  ### 2. Float
Float, "Floating Point Number" is a number, positive or negative, containing one or more decimals. To assign a variable with float, we can write a variable name followed by equals to sign and float. 
```
x = 55.6
y = -20.3
print(x)
print(y)
```
### 3. Complex
Complex numbers are written with a "j" as the imaginary part.
```
c = 5j
d = 3+2j
print(c)
print(d)
```
## Boolean in Python 
Boolean represents one of the two values i.e True or False
While programming , there may arise a situation where we have to know if expression is true or false. When we compare two values, python evaluates and sends the boolean value.
```
print(10>2)
```
In the above code, python analyze the expression and returns the true value.
### bool() function
The bool() function allows you to evaluate any value, and give you True or False in return.
Generally, any value is True if it is not empty strings, 0 or empty sets,tuples or dictionary.
```
x = "Hi"
print(bool(x))
```
However, if the values evaluates to empty values, such as (), [], {}, "", the number 0, and the value None, then the python returns False.
```
y = 0
print(bool(y))
```
## Lists in Python
List are the data types that allows us to store multiple items in a single variable. Lists are created using  big brackets i.e [] .
```
name = ["Kevin", "Smith", "Shawn"]
print(name)
```
### Features of Lists
1. List are ordered. It means that items in a list have a definite order. Whenever a new item is added to the list, it is added at last.
2. Lists are changeable. It means that the items in a list can be removed after being created. Also the new item can be added.
3. Lists allows duplicate. Since, lists are indexed, so lists can have items with the same value. For example:
```
lang = ["Eng", "French", "Japanese", "Eng", "French"]
print(lang)
```
4. Lists items can be of any data types. They can be of same data types or different data types.
```
numlist = [1,2,3,4]
randomlist = [ "xyz", True, 22.5, 40 ]
print(numlist)
print(randomlist)
```   
## Tuples in Python
## Set in Python
## Dictionaries in Python
## If-else
```
if b > a:
   print("b is greater than a")
```
```
if b > a:
   print("b is greater than a")
elif b == a:
   print("They both are equal")
```
```
a=200
b=20

if b > a:
   print("b is greater than a")
elif b == a:
   print("They both are equal")
else:
   print("a is greater than b")
```
## While loop
## For Loop

## Math in Python
In Python, we have built-in math functions, including math module that allows us to perform mathematical tasks on numbers. 

### Built-in Math functions
There are different built-in math functions to perform mathematical operations.
| Functions | Use |
| ------------- | ------------- |
| round() | It rounds the number to the nearest value |
| pow(x,y) | returns the value of x to the power of y (xy) |
| max() | used to find the highest value in an iterable |
| min() | used to find the lowest value in an iterable |
```
a=3
b=4
c=1
x=-2
print(abs(x))
print(pow(x,2))
print(max(a,b,c))
print(min(a,b,c))
```
### Built-in Math Module
Python has also a built-in module called math, which extends the list of mathematical functions.
To use it, you must import the math module:
```
import math
```
After importing math module, we can use different methods to perform mathematical calculations in python.

| Module | Description |
| ------------- | ------------- |
| sqrt() | finds the square roof of a number |
| ceil() | rounds a number upwards to its nearest integer |
| floor() | rounds a number downwards to its nearest integer |

```
import math
pi = 3.14
print(math.ceil(pi))
print(math.floor(pi))
print(math.sqrt(5))
```













