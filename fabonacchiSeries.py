'''
Write a program to print the Fibonacci series till n terms (Accept n from user)
'''


# for loop:-

# n= int(input("enter no."))
# a=0
# b=1
# if n==1:
#     print(a)
# else:
#     print(a)
#     print(b)
#     for i in range(2,n+1):
#      c=a+b
#      a=b
#      b=c
#      print(c)





# while loop:-



n= int(input("enter no."))
a=0
b=1
i=1
if n==1:
    print(a)
else:
    print(a)
    print(b)
    while(i<=n):
        c=a+b
        a=b
        b=c
        print(c)
        i+=1