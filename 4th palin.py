n=int(input("Enter the integer : "))
palin=0
b=n
while(n>0):
    a=n%10
    palin=palin*10+a
    n=n//10
if(b==palin):
    print("true")
else:
    print("false")

    
    
