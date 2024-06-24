# def even_list(lst):
#     evn_lst = []
#     for i in lst:
#         if i % 2==0:
#             evn_lst.append(i)
#     return evn_lst

# lst_ip= list(map(int,input()))
# print(even_list(lst_ip))


# Write a  Python program to print the even numbers from a given list.
def even_list(input_list):
    even_numbers = []
    for i in input_list:
        if i % 2 == 0:
            even_numbers.append(i)
    return even_numbers

input_list = list(map(int,input()))
print("Even numbers:", even_list(input_list))

