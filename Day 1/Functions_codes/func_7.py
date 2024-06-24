# Write a Python function that accepts a string and counts the number of upper and lower case letters.
def up_low(strr):
    low =0
    up=0
    for char in strr:
        if char.islower():
            low += 1
        elif char.isupper():
            up+=1
    return low, up
strr = input()
low_num , up_num= up_low(strr)
print("No. of LOWER case:",low_num)
print("No. of upper case:",up_num)

