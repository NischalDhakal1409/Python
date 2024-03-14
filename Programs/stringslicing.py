#slicing is the method of creating a substring by extracting elements from the other string.
# indexing[] or slice()
# [start:end:step]

#Use of indexing

name = "John Smith"
first_name = name[0:5]                  #This line of code can also be written as first_name = name[:5]
last_name = name[5:11]                  #This line of code can also be written as last_name = name[5:]
random_name = name[0:11:2]

print(first_name)
print(last_name)
print(random_name)

#Use of slicing

website = "https://www.google.com"
slice = slice(12,-4)
print(website[slice])
