'''
Write a program to add first n terms of the following series using a while loop :
1/1! + 1/2! + 1/3! + …….. + 1/n!
'''

# while loop:-


# num=int(input("enter a no."))
# sum=0
# fact=1
# i=1
# while(i<=num):
#     fact=fact*i
#     sum=sum+i/fact
#     i+=1
# print(round(sum,2))


# for loop:-

num=int(input("enter a no."))
sum=0
fact=1
for i in range(1,num+1):
    fact=fact*i
    sum=sum+i/fact
print(round(sum,2))
