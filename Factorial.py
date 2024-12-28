n=int(input())
fact=1
for i in range(1,n+1):
    fact*=i
string_fact=str(fact)
if len(string_fact)<4:
    print(string_fact)

else:
    print(string_fact[-4:])
