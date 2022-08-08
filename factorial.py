'''
Write a program to print the factorial of a number accepted by the user.
'''

# for loop:-


# n=int(input("enter a no."))
# f=1
# for i in range(1,n+1):
#     f*=i
#     print(f)


# while loop:-


n=int(input("enter a no."))
f=1
i=1
while(i<=n):
    f*=i
    i+=1
print(f)