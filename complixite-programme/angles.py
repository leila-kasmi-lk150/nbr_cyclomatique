print("\n")
print("########## Angles #########")
print("\n")
a=int(input("enter a: "))
while(a<=0):
    a=int(input("invalid, enter a, number positve"))
b=int(input("enter b: "))
while(b<=0):
    b=int(input("invalid, enter b, number positve"))
c=int(input("enter c: "))
while(c<=0):
    c=int(input("invalid, enter c, number positve"))
if((a+b+c)!=180 ):
    print("NOT TRIANGLE")
elif(a<90 and b<90 and c<90 ):
    print("aigu")
elif(a==90 or b==90 or c==90):
    print("droit")
elif(a>90 or b>90 or c>90):
    print("obruse")
elif((a^2!=b^2+c^2) or (b^2!=a^2+c^2) or (c^2!=b^2+a^2) ):
    print("not traingle")