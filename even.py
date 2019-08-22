

numbers = []
n = int(input("Enter number of elements: \t"))
for i in range(1, n+1):
    allElements = int(input("Enter element:"))
    numbers.append(allElements)

print("all the elements ", numbers)
even_lst=[]
for j in numbers:
    if j % 2 == 0:
        even_lst.append(j)

print("even elements ", even_lst)        


'''
 ==============
Enter number of elements: 	4
Enter element:2
Enter element:4
Enter element:5
Enter element:7
all the elements  [2, 4, 5, 7]
even elements  [2, 4]
>>> 
'''
        
