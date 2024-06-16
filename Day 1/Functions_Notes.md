These are some instructions packaged together to perform a specific task.
- Example of a simple function:
```
def hello_func():
	print("Hello World!")

hello_func()
hello_func()
hello_func()


# Output := 
Hello World!
Hello World!
Hello World!
```

## Return


```
def hello_func():
	return "Hello World!"

print(hello_func())
print(hello_func())
print(hello_func())


# Output := 
Hello World!
Hello World!
Hello World!
```


### Difference between 'print' and 'return'

| print Statement                              | return Statement                                                                                  |
| -------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| - provide output information to the console. | - used to exit a function and optionally pass an expression to the caller                         |
|                                              | - It stops the execution of the function and sends a value back to where the function was called. |

