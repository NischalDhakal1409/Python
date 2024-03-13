temp = int(input("What is the temperature outside today?: "))

if temp >=0 and temp <=38:
    print("We got good weather today")
elif temp < 0 or temp > 30:
    print("We got bad weather today")