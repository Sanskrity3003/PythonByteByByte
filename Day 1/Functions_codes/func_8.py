#Write a  Python function that takes a list and returns a new list with distinct elements from the first list.
# def unq(lst):

#     return list(set(lst))
#     # return lst.unique()
# lst= list(input())
# print(unq(lst))



#Write a Python function that takes a number as a parameter and checks whether the number is prime or not.
def prm(num):
    
    if num%2==0:
        return "isnotPrime"
    elif num%2 != 0:
        return "isPrime"

num = int(input("Enter a number:"))
print(prm(num))