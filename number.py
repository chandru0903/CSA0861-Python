n=int(input("Enter the number : "))
count=0
temp=n
for i in str(temp):
    temp=temp//10
    count+=1
print(count)
