print("\n")
print("########## rhombus shape #########")
print("\n")

m=int(input("Enter the length of base of an rhombus shape: "))
while(m<=0):
    m=int(input("enter number positve: "))
x=int(m/2)

i=1
while(i <= m):
    print(' '*x +"*" * i + '\n', end='')
    x-=1
    i+=2
i=(i-4)
x=1
while(i >= 0):
    print(' '* x +"*" * i + ' '*x + '\n', end='')
    i-=2
    x+=1

# C = npr decisions + 1
# c = 2 + 1
# c = 3