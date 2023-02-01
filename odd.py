n=int(input("Enter the number of elements : "))
mylist=[]
i=0
odd=0
even=0
while(i<n):
    m=int(input("Enter the number : "))
    mylist.append(m)
    i+=1
print("The given list is : ",mylist)
for i in mylist:
    if(i%2==0):
        even+=i**2
    else:
        odd+=i**2
print("[",odd,",",even,"]")
