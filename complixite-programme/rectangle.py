print("\n")
print("########## rectangle #########")
print("\n")


m=int(input("Enter the length of the rectangle: "))
while(m<=0):
    m = int(input("invelid lenght,Enter the length of the rectangle, number positve: "))
n=int(input("Enter the width of the rectangle: "))
while(n<=0):
    n = int(input("invalid width,Enter the width of the rectangle, number positve: "))
print(('*' * m + '\n') * n, end='')

# C =    npr decisions + 1
# c = 2+1
# c = 3