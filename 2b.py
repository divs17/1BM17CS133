str=input("enter a string")

def reverse(input):
    list=str.split(" ")
    list=list[-1::-1]
    str1=' '.join(list)
    return str1
print(reverse(str))
print(reverse(str)[::-1])
    
