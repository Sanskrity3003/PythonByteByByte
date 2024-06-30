## Scope refers to a place in the program where a variable can be used.

### Python works acc, to this LEBG order itself.
# Type of scopes:

1. Local Scope
2. Enclosing (non- local) Scope
3. Global Scope
4. Built- in - Scope

### 1. Local Scope: 
- Variable defined inside a function.
- These variables can only be accessed inside the function it is defined.
- These are created when function is called and destroyed when the function ends.
```
def func():
	x = 2 # local scope
	return 2
print(func())
```
### 2. Enclosing (non-local) Scope:
- Variables are defined in Nested functions.
- The outer function can be accessed by inner function.
```
def func():
	x = 2 # enclosing scope
	def func_2():
		print(x)
	func_2()
print(func())
```
### 3. Global Scope
- Variables defined at the top of a function are global i.e in the main body of the program.
- It can be accessed from anywhere in the program.
- You can also define a global variable inside a local scope using:  
```
a = 10 # global scope
def func():
	global x # this is used to define that well make change in globalx now
```

### 4. Built-in-scope:
- These are built - in functions like : len(), print().
eg:```
```
import builtins
print(dir(builtins)) # provides list of buitlin functions
m = min([1,2,3])
```
## Naming variables: 
If same variable with different values are stated inside and outside the function, the program considers it as two different variables.
