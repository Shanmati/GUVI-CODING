n=int(input())
a=0
b=1
for j in range(n):
    c=a+b
    a=b
    print(a,end=" ")
    b=c
