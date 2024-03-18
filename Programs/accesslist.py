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

#extend list
programs = ["Word", "Excel", "Powerpoint"]
software = ["Office", "VS-Code"]
programs.extend(software)
print(programs)

#Removing items from a list using remove method
names = ["Ram", "Sita", "Hari", "Kevin", "Drogy", "Brogy", "Rayne"]
names.remove("Ram")
print(names)

#Removing items from a list using remove method(specifying index)
name = ["Ram", "Sita", "Hari", "Kevin", "Drogy", "Brogy", "Rayne"]
name.pop(1)
name.pop()
print(name)

##Removing items from a list using remove method(without specifying index)
person = ["Ram", "Sita", "Hari", "Kevin", "Drogy", "Brogy", "Rayne"]
person.pop()
print(person)

#Removing list completely
#primenumber = [1,3,5,7,13]
#del primenumber
#print(primenumber) #this will cause an error because we have successfully deleted the list.

#Using clear method to remove list items.
texts = ["abc","bcd","def"]
texts.clear()
print(texts)