def maxareas(self, heights):
    maxarea=0
    for i in range(len(heights)):
        for j in range(i+1,len(heights)):
            maxarea=max(min(heights[i],heights[j]*(j-i)))
    return maxarea
n=int(input("Enter the number :"))
heights=[]
for i in range(n):
    m=input("Enter the numbers ::: ")
    heights.append(m)
maxareas  (heights)
