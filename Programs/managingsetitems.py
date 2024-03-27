#Adding items in a set
num = {1,2,3,5,67,89,0}
num.add(22)
print(num)

#Adding items in a set from another set
country ={"Nepal","USA","UK"}
city = {"Kathmandu", "San Franscisco", "London"}
country.update(city)
print(country)

#Adding items from list to a set
country ={"USA","UK"}
city = [ "San Franscisco", "London"]
country.update(city)
print(country)

#Removing items from a set
name = {"Kevin", "David", "Rayne", "Lucifer"}
name.remove("Kevin")
name.discard("David")
print(name)

#Clearing items of a set
