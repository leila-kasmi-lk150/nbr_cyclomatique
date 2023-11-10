print("\n")
print("########## isosceles triangle #########")
print("\n")

m=int(input("Enter the length of base of an isosceles triangle: "))
while(m<=0):
    m = int(input("Invalide lenght,Enter the length of base of an isosceles triangle, number positve: "))
x=int(m/2)

i=1
while(i <= m):
    print(' '*x +"*" * i + '\n', end='')
    x-=1
    i+=2

# C = npr decisions + 1
# c = 2 + 1
# c = 3