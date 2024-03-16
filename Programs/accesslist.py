#Managing List items

#Accesing items from positive index
lang = ["Python","C","Java"]
print(lang[1])

#Accesing items from negative index
num = [1,3,5,2,3]
print(num[-2])

#Accesing from range of index
random = ["a","c","q","r","i","p","g"]
print(random[2:5])

#Checking if the items exists or not
fruits = ["mango", "apple", "grapes"]
if "apple" in fruits:
  print("Yes, 'apple' is in the fruits list")

#Changing list items
alphabet = ["A", "D", "E"]
alphabet[1] = "W"
print(alphabet)

#Changing range of list items
num = [1,2,4,6,7]
num[0:3] = [9,0,10]
print(num)

#inserting an item in a list
country = ["Nep","Ind","Pak"]
country.insert(2,"US")
print(country)

#Append items
position = ["First","Second","Third"]
position.append("Last")
print(position)
