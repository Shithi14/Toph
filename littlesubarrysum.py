n,a,b=map(int,input().split())
arr=list(map(int,input().split()))
sum=0
for i in range(a,b+1):
    sum=sum+arr[i]
print(sum)