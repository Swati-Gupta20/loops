'''
write a program to print the sum of multiples of number falls between two user input.
'''

# num1=int(input("enter no."))
# num2=int(input("enter no."))
# i=num1
# sum=0
# while(i<num2):
#     sum=sum+i
#     i+=num1
# print(sum)

num1=int(input("enter no."))
num2=int(input("enter no."))
sum=0
for i in range(num1,num2,num1):
    sum=sum+i
print(sum)