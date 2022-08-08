# n=int(input("enter no."))
# len=len(str(n))
# sum=0
# copy_n=n
# i=0
# while(i<len):
#     n2=n%10
#     sum=sum+n2
#     n//=10
#     i+=1
# if copy_n%sum==0:
#     print("it's a harshad no.")
# else:
#     print("it's not a harshad no.")


# for loop:-

n=int(input("enter no."))
len=len(str(n))
sum=0
copy_n=n
for i in range(len):
    n2=n%10
    sum=sum+n2
    n//=10
if copy_n%sum==0:
    print("it's a harshad no.")
else:
    print("it's not a harshad no.")
