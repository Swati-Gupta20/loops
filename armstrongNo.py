'''
Write a program to check whether a number is Armstrong or not. (Armstrong number is a number that is equal to the sum of cubes of its digits, for example : 153 = 1^3 + 5^3 + 3^3.)
'''


# while loop:-


num=int(input("enter a no."))
power=len(str(num))
copy_num=num
sum=0
i=0
while(i<power):
    digit=num%10
    sum=sum+digit**power
    num=num//10
    i+=1
if sum==copy_num:
    print(copy_num,"is an armstrong number.")
else:
    print(copy_num,"is not an armstrong number.")


# for loop:-

# num=int(input("enter a no."))
# power=len(str(num))
# copy_num=num
# sum=0
# for i in range(power):
#     digit=num%10
#     sum=sum+digit**power
#     num=num//10
# if sum==copy_num:
#     print(copy_num,"is an armstrong number.")
# else:
#     print(copy_num,"is not an armstrong number.")




