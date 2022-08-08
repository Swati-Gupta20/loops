'''
 Write a program to check whether a number is palindrome or not.
'''



# for loop:-

# num=int(input("enter your no."))
# r=0
# rnum=0
# len=len(str(num))
# copy_num=num
# for i in range(len):
#     r=num%10
#     rnum=rnum*10+r
#     num=num//10
# if rnum==copy_num:
#     print(copy_num,"is a palindrome no.")
# else:
#     print(copy_num,"is not a palindrome no.")



# while l(oop:-



num=int(input("enter your no."))
r=0
rnum=0
len=len(str(num))
copy_num=num
i=1
while(i<=len):   
     r=num%10
     rnum=rnum*10+r
     num=num//10
     i+=1
    #  print(rnum,end="")
if rnum==copy_num:
    print(copy_num,"is a palindrome no.")
else:
    print(copy_num,"is not a palindrome no.")




# another way:-

# num=(input("enter a no."))
# rnum=num[::-1]
# if num==rnum:
#     print(num,"is a palindrome no.")
# else:
#     print(num,"is a palindrome no.")
