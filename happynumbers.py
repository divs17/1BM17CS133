prime = open('happy-no.txt', 'r')
happy = open('prime_no.txt', 'r')

prime_string = prime.read()
happy_string = happy.read()

prime_no = prime_string.split(",")
happy_no = happy_string.split(",")

prime_no[-1] = prime_no[-1].strip()
happy_no[-1] = happy_no[-1].strip()

overlap = []

for number in prime_no:
     if number in happy_no:
          overlap.append(number)

print("The overlapping numbers are: ",overlap)

'''
Output:
The overlapping numbers are:  
[' 7', ' 13', ' 19', ' 23', ' 31', ' 79', ' 97', ' 103', ' 109', ' 139', ' 167', ' 193', ' 239', ' 263', ' 293', ' 313',
' 331', ' 367', ' 379', ' 383', ' 397', ' 409', ' 487', ' 563', ' 617', ' 653', ' 673', ' 683', ' 709', ' 739', ' 761',
' 863', ' 881', ' 907', ' 937']
