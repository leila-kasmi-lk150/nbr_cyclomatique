print("\n")
print("########## right triangle #########")
print("\n")


m=int(input("Enter the length of the right triangle: "))
while(m<=0):
    m = int(input("Invalide length,enter the length of the right triangle, number positve: "))
i=1
while(i <= m):
    print("*" * i + '\n', end='')
    i+=1

# C = npr decisions + 1
# c = 2 + 1
# c = 3