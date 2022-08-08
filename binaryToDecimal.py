'''
18. Write a program to convert binary to decimal.
'''


# for loop:-

num=input("enter any binary no.")
dec=0
len=len(num)
for i in range(len):
    power=(len)-(i+1)
    dec=dec+int(num[i])*2**power
print(dec,"is decimal no.of",num)



# while loop:-

# num=input("enter any binary no.")
# dec=0
# len=len(num)
# i=0
# while(i<len):
#     power=(len)-(i+1)
#     dec=dec+int(num[i])*2**power
#     i+=1
# print(dec,"is decimal no.of",num)
