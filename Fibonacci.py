n = int(input())
count = 0
first = 1
second = 1


if n==0:
    print("0")
elif n==1 or n==2:
    print("1")
else:
    for i in range (3,n+1):
        fibo=first+second
        first=second
        second=fibo

    print(fibo)
          
'''
while count < n:
    if count <= 1:
    
        fibo = count
    else:
        fibo = first + second
        first = second
        second = fibo
    print(fibo)
    count += 1'''

        


