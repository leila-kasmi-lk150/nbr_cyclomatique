print("\n")
print("########## Type  #########")
print("\n")
a=int(input("enter a: "))
while(a<=0):
    a=int(input("invalid, enter a,  number positve"))
b=int(input("enter b: "))
while(b<=0):
    b=int(input("invalid, enter b, number positve"))
c=int(input("enter c: "))
while(c<=0):
    c=int(input("invalid, enter c, number positve"))

if(a!=b and a!=c and b!=c):
    print("scalene")
elif(a==b and a==c):
    print("equilateral")
else:
    print("isocal")