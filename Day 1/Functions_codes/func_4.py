# Write a Python program to reverse a list.

def revstr(strr):
    strr = strr[::-1]
    return strr
user= input()
strr= list(map(str,user.split()))
#or
#strr= list(user)
print(revstr(strr))


#Write a Python program to reverse a string.

def revstr(strr):
    strr = strr[::-1]
    return strr

user_input = input()
print(revstr(user_input))
