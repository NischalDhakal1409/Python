#OOP in Python

#Class
class school:
    x = "school"
output = school()
print(output.x)

#In-it function
class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
p = person("Ray",22)
print(p.name)
print(p.age)
