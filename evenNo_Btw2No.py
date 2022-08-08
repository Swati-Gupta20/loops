'''
 Write a program to display all even numbers that fall between two numbers (exclusive both numbers) entered by the user.
'''
# while loop:-

num1=int(input("enter first no.:-"))
num2=int(input("enter second no.:-"))
i=1
if num1>num2:
   while(num1>num2):
      if num2%2==0:
          print(num2)
      num2=num2+1
else:
    while(num1<num2):
        if num1%2==0:
           print(num1)
        num1=num1+1



# for loop:-

# num1=int(input("enter first no.:-"))
# num2=int(input("enter second no.:-"))

# if num1<num2:
#     for i in range(num1+1,num2):
#         if i%2==0:
#          print(i)
# else:
#      for i in range(num2+1,num1):
#         if i%2==0:
#          print(i)


        

