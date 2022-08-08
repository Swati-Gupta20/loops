# No. series 1 to 100:-


# i=1

# while (i<=100):
#     print(i)
#     i=i+1



# fruits=["apple","mango","banana","grapes","orange","pineapple"]
# for i in fruits:
#     print(i)

# for i in range(101):
#     print(str(i)+" swati")



# i=1

# while i<11:
#     print(i)
#     i+=1
#     i==3
#     break


# num=int(input("enter a number"))
# i=1
# a=0
# while (i<num):
#     num2=int(input("enter no."))
#     a=a+num2
#     print(a)


# i=1
# while(i<=5):
#     print(i)
#     if i==3:
#       break
#     i=i+1

# i=0
# while(i<=5):
#      i=i+1
#      if i==3:
#       continue
#      print(i)

# num=int(input("enter a number:-"))
# i=1
# max=0
# while (i<num):
#     num2=int(input("type no."))
#     if max<num2:
#         max=num2
#     i+=1
# print(max, "is maximum")



# num=int(input("enter a number:-"))
# i=1
# min=1000
# while (i<num):
#     num2=int(input("type no."))
#     if min>num2:
#         min=num2
#     i+=1
# print(min, "is minimum")
 


# num=int(input("enter a number:-"))
# i=0
# max=0
# min=1000
# while (i<num):
#     num2=int(input("type no."))
#     if max<num2:
#         max=num2
#     if min>num2:
#         min=num2
#     i+=1

# print(max, "is maximum","and",min,"is minimum")


# pattern:-


# i=1
# while(i<=5):
#     print(i*" *")
#     i+=1

# for i in range(6):
#     print(i*" *")


# sum=0
# for i in range(101):
#     sum=sum+i
# print(sum) 

# i=0
# sum=0
# while(i<=100):
#     sum=sum+i
#     i+=1
# print(sum)


# num1 = input("Enter any number : ")
# print("Reverse number is : ", num1[: : -1])




# i=0
# while(i<=9):
#     i=i+1
#     if i==7 or i==8:
#         continue
#     if i==9:
        
#       print(" "*2)
# print(i)

# n=9
# i=0
# while n>=i:
#     i=i+1
#     if i==7 or i==8:
#         print()
#         continue
#     print(i)





# word=input("enter the number)
# i=1
# len=len(word)
# while(i<=len):
#     print(i,word[0])
#     word[0]=word[0]+1
#     i=i+1
# name="themshingla"
# name=(input("enter the number"))
# i=0
# while i<len(name):
#     if name=="z":
#        i=i+1
#     print("current letter",name[i])
#     i=i+1
#     print("value=",i)



# fabonaachi series:-

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

# a=2*1+(2%4//3*2)-3*5*6**2
# print(a)



# num=input("enter any binary no.")
# dec=0
# len=len(num)
# for i in range(len):
#     power=(len)-(i+1)
#     dec=dec+int(num[i])*2**power
# print(dec,"is decimal no.of",num)


# for i in (1,2,3):
#     print(i)


# for i in (2,3,4):
#     print("i")

# for i in (4,3,2,1,0):
#     print(i, end=" ")

# for i in range(10):
#     if(i%2!=0):
#         print("Hello",i)

# for i in range(10,2,-2):
#     print(i, "Hello")


# i=0
# while(i<0):
#     print(i)
# i+=1

# a="1111"
# print(len(a))

# a=0+1*2**0
# print(a)



# n=int(input("enter no. of rows:-"))

# for i in range(n):
#     for j in range(i+1):
#         print(j+1,end=" ")
#         if i==n:
#             print()
#     print()



# n=int(input("enter no. of rows:-"))

# for i in range(n):
#     for j in range(n-i):
#         print("*",end=" ")
#     print()


# n=int(input("enter no."))
# i=1
# while(i<=n):
#     print(str(n)+"X"+str(i)+"="+str(i*n))
#     i+=1


# n=int(input("enter no."))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(str(i)+"X"+str(j)+"="+str(i*j))
#     print()



# n=int(input("enter no."))
# i=1
# while(i<=n):
#     j=1
#     while(j<=n):
#         print(str(i)+"X"+str(j)+"="+str(i*j))
#         j+=1
#     print()
#     i+=1





# n=int(input("enter no."))
# p=1
# for i in range(1,n+1):
#     for j in range(i):
#         print(p,end=" ")
#     print()
#     p+=1







# n=int(input("enter no."))
# p=1
# for i in range(n):
#     for j in range(i,n):
#         print(" ",end=" ")
#     for j in range(i+1):
#         print(p,end=" ")
#         p+=1
#     print()



# num=int(input("enter no."))
# if num<0:
#     print(num*-1)
# elif num>0:
#     print(num*-1)
# else:
#     print("enter any positive or negetive no.")




# n=int(input("enter no."))
# p=1
# for i in range(n):
#     for j in range(i+1):
#         print(format(p,"<2"),end=" ")
#         p+=1
#     print()



# n=int(input("enter no."))
# for i in range(n):
#     for j in range(i+1):
#         print(j+1,end=" ")
#     print()



# n=int(input("enter any ASCII number:"))
# print(chr(100))

# i=156
# while(i<=246):
#     print(i-155)
#     i+=1


# n=int(input("enter no."))

# i=0
# while(i<n):
#     i+=1
#     print("swati")


# while loop:
# n=int(input("enter rows:-"))
# i=0
# while(i<n):
#     j=0
#     p=65+i
#     while(j<=i):
#         print(chr(p),end=" ")
#         j+=1
#         p+=1
#     print()
#     i+=1
    
# i=891
# while(i<930):
#     if (i-890)%3==0:
#         print(i-890)
#     i+=1


# n=5
# i=0
# while(i<5):
#     j=0
#     while(j<n-i):
#         print(" ",end=" ")
#         j+=1
#     k=0
#     while(k<i+1):
#         print("*",end=" ")
#         k+=1
#     # a=0
#     # while(a<i):
#     #     print("*",end=" ")
#     #     a+=1
#     print()
#     i+=1



# n=5
# a=0
# i=0
# while(i<5):
#     j=0
#     while(j<n-i):
#         print(" ",end=" ")
#         j+=1
#     k=0
#     while(k<=a):
#         print("*",end=" ")
#         k+=1
#     print()
#     i+=1
#     a+=2

# n=5
# a=0
# for i in range(n):
#     for j in range(n-i):
#         print(" ",end=" ")
#     for j in range(a+1):
#         print("*",end=" ")
#     print()
#     a+=2


# n=5
# for i in range(n):
#     for j in range(i,-1,-1):
#         print(j+1,end=" ")
#     print()


# n=int(input("enter rows:-"))
# i=0
# while i<=n:
#     j=0
#     while j<i:
#         print(i-j,end=" ")
#         j+=1
#     print()
#     i+=1



# n=int(input("enter no."))
# k=0
# if n==1 or n==0:
#     print("it is not a prime no.")
# else:
#     for i in range(2,n):
#        if n%2==0:
#         k=k+1
# if k==0:
#     print("it is a prime no.")
# else:
#     print("it is not a prime no.")

# num1=int(input("enter no."))
# num2=int(input("enter no."))
# sum=0
# # copy=num1
# for i in range(num2):
#     if i%num1==0:
#         sum=sum+num1
# print(sum)


# num1=int(input("enter no."))
# num2=int(input("enter no."))
# sum=0
# i=0
# while(i<num2):
#     if num1%num1==0:
#         sum=sum+num1
#         i+=1
# print(sum)

# i=10
# while(i<20):
#     i+=1
#     if i==13 or i==16:
#         print(" ")
#         continue
#     print(i)
# print("13 and 16 are skipped") 


# a=int(input("enter no?"))
# b=int(input("enter no?"))
# i=a
# sum=0
# while i<b:
#     sum+=i
#     i=i+a
# print(sum)


# n=int(input("enter rows:-"))
# i=0
# while(i<n):
#     j=0
#     while(j<i+1):
#         print(j+1,end=" ")
#         j+=1
#     k=0
#     while(k<i):
#         print(i-k,end=" ")
#         k+=1
#     print()
#     i+=1

# p=1
# for i in range(5):
#     for j in range(p+1):
#         print(p,end=" ")
#         p+=1
#     print()



n=6
for i in range(n):
    for j in range(i+1):
        print(j,end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print()
