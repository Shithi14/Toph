a,b=map(int,input().split())
hour=a*30+b*.5
minutes=6*b
difference=hour-minutes
difference2=abs(360-difference)
ans=min(difference,difference2)
print(f"{ans:.7f}")