''' 1. Write a Python function to find the maximum of three numbers. '''


#1ST APPORACH
# def max3(a,b,c):
#     if a > b:
#         print(a)
#     elif b > c:
#         print(b)
#     else:
#         print(c)

# a= int(input())
# b= int(input())
# c= int(input())
# print("The maximum no is:\n")
# max3(a,b,c)


#2nd APPORACH
def max3(a,b,c):
    if a > b:
        return a
    elif b > c:
        return b
    else:
        return c

a= int(input())
b= int(input())
c= int(input())
print("The maximum no is:",max3(a,b,c))
