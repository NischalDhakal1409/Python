#General example of list
name = ["Kevin", "Smith", "Shawn"]
print(name)

#Demonstration of lists allows duplicate
lang = ["Eng", "French", "Japanese", "Eng", "French"]
print(lang)

#Demonstrating that the lists can be of any data type
numlist = [1,2,3,4]
randomlist = [ "xyz", True, 22.5, 40 ]
print(numlist)
print(randomlist)

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