Using the slice syntax we can return a range of values/characters from the given string/list.

## List Slicing
- Here are some basic slicing examples:
```
list[start:stop]
a=[1,2,3,4,5,6,7,8,9]
print(a[1])        # output= 2
print(a[-1])       # output= 9
print(a[2:8])      # output= 3, 4, 5, 6, 7,8
```
- Mix of +ve and -ve indexes can also work.
```
print(a[1:-2])    # output= 2,3,4,5,6,7
```
- Step Slicing
```
list[start:stop:step]
a=[1,2,3,4,5,6,7,8,9]
print(a[0:8:2])       # output= 1,3,5,7
```
- To reverse a list using step slicing:
```
print(a[::-1])
```
- To reverse the output of the list:
```
print(a[0:8:2][::-1])
```


## String Slicing
- Here are some basic string slicing operation:
```
st= "https//google.com"
print(st[1])     # output= t
print(st[7:])    # output = googe.com
print(st[7:-4])  # output = google
print(st[:5])    # output = https
```
- To reverse string:
```
st= "https//google.com"
print(st[::-1])
```


Slicing is almost same in strings and lists.