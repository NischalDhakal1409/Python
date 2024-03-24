#Accesing items in tuples
num = (1,2,5,9)
print(num[1])

#Accessing items in tuples with negeative indexing
num = (12,346,82,1)
print(num[-1])

#Accessing range of items 
alphabet = ("a","ed","as","qo")
print(alphabet[0:2])

#Adding items in a tuple
fruits = ("Apple","Banana","Mango")
y = list(fruits)
y.append("Pineapple")
fruits = tuple(y)
print(fruits)

#Adding tuple to a tuple
random = (1,2,3,4,67,89,1)
add = (12,)
random += add
print(random)