s=input()
p=list(s)
p.reverse()
sp=''.join(p)
if  s==sp:
    print("Yes")
else:
    print("No")