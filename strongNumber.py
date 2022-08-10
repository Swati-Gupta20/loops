n=int(input("enter no:-"))
len=len(str(n))
sum=0
num=n
i=0
while(i<len):
    digit=n%10
    n//=10
    f=1
    j=1
    while(j<=digit):
        f=f*j
        j+=1
    i+=1
    sum+=f
if sum==num:
    print("It's a strong no.")
else:
    print("It's not a strong no.")