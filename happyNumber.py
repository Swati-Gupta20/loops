n=int(input("enter no:-"))
copy=n
i=0
while(i<n):
    sum=0
    num2=n
    j=0
    while(j<len(str(num2))):
        num=n%10
        sum=sum+num**2
        n//=10
        j+=1
    n=sum
    i+=1
if sum==1:
    print(copy,"is a happy no.")
else:
    print(copy,"is a unhappy no.")