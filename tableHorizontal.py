n=int(input("enter no."))
i=1
while(i<=n):
    j=1
    while(j<=n):
        print(j,"X",i,"=",i*j,end="    ")
        j+=1
    print()
    i+=1
