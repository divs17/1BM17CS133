numbers = []
n = int(input("Enter number of elements: \t"))
for i in range(1, n+1):
    allElements = int(input("Enter element:"))
    numbers.append(allElements)

print("all the elements ", numbers)

num=int(input("element you want to search"))
if num in numbers:
    print(num," is present")
else:
    print(num,"is not present")


