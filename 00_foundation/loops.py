# Loops Module

#1. Basic loop
numbers = [1,2,3,4,5]

for i in numbers:
    print("Number",i)


#Square the each number
squared = []
for num in numbers:
    squared.append(num ** 2)

print("Squared :",squared)

# Conditional processing 
filtered = []
for num in numbers:
    if num %2 ==0:
        filtered.append(num)

print("Even Numbers :",filtered)

# Simulating dataset cleaning
data = [10,20,None,30,None,40]

clean_data = []

for value in data:
    if value is not None:
        clean_data.append(value)

print("Clean Data", clean_data)
