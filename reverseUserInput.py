''' Write a program to reverse the number accepted by the user.
'''


num=int(input("enter your no."))
r=0
rnum=0
len=len(str(num))
for i in range(len):
    r=num%10
    rnum=rnum*10+r
    num=num//10
print("reverse no. is",rnum)


# another method:-

# num=(input("enter no."))
# print("reverse no. is",num[::-1])
