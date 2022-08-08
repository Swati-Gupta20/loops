'''
Write a program to accept 10 numbers from the user and display the largest & smallest number.
'''
# while loop:-



num=int(input("enter a number:-"))
i=0
large=0
small=1000
while (i<num):
    num2=int(input("type no."))
    if large<num2:
        large=num2
    if  small>num2:
        small=num2
    i+=1

print(large, "is largest","and",small,"is smallest")



# for loop:-


# num=int(input("enter a number:-"))
# large=0
# small=1000
# for i in range(num):
#     num2=int(input("enter no."))
#     if large<num2:
#         large=num2
#     if small>num2:
#         small=num2
# print(large, "is largest","and",small,"is smallest")


