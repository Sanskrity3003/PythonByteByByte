# Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.
def fact(num):
    f = 1
    while num >= 1:
        f = num * f
        
        num = num -1
    return f

num = int(input())
print("The factorial of", num ,"is",fact(num))