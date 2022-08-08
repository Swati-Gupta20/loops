'''
Write a program to find the product of the digits of a number accepted from the user.
'''

# for loop:-

# num=(input("enter number:-"))
# f=1
# for i in num:
#     f=f*int(i)
# print("product of no.is",f)


# while loop:-


num=int(input("enter number:-"))
i=0
p=1
while(num!=0):
    i=num%10
    p=p*i
    num=num//10
print("product of the digits are",p)

