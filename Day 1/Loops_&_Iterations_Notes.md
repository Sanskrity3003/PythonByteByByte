```
nums = [1,2,3,4,5]
for nums in nums:
	print(num)
```

##### Break 
Break keyword completely brakes the loop and comes out of it.
```
nums = [1,2,3,4,5]
for nums in nums:
	if num == 3:
		print("Found")
		break
	print(num)

#output = 1
2
Found
```
##### Continue
Continue keyword jumps to the next iteration.(when u wants to skip a value in iteration)
```
nums = [1,2,3,4,5]
for nums in nums:
	if num == 3:
		print("Found")
		continue
	print(num)

#output = 
1
2
Found
4
5
```

## while 
Iterates till a certain condition is met or we use break statement.
```
x= 10
while x <10:
	print(x)
	x+=1
```
- using breaks in while :
```
x= 10
while x <10:
	if x==5:
		break
	print(x)
	x+=1
# output =
1
2
3
4
```

##### Tip: If stuck in an ifinite loop, use Ctrl + C.
