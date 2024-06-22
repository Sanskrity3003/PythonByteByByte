'''Write a Python function to sum all the numbers in a list.'''

def num_list(nums):
    #initialising with zero
    flag=0
    # for each element in the list
    for i in nums:
        flag += i
    return flag
user_input =input()
list=list(map(int, user_input.split()))
print(num_list(list))
