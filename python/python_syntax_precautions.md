# Python Syntax Precautions
Here are some new things I learned about python, coming from a C# background.

## Spacing
```
Spaces are the preferred indentation method.

Tabs should be used solely to remain consistent with code that is already indented with tabs.

Python disallows mixing tabs and spaces for indentation. PICK ONE.
```

## Capitalized Booleans
```
if(True)
    print(True)
if(False)
   print(False)
```

## Type Conversion
```python
int('1') # returns integer 1
int('1.5') # error
int(float('1.5')) # returns integer 1

#True when not empty, False when empty
bool() # False
bool('') #False
bool(' ') # True

#True when any number except 0
bool(0) # False
bool(0.0000) # False
bool(3.1231) # True

# None Keyword
bool(None) # False
```

## Arithmetic Operators
```python
#Modulus
print(10%3) # returns 1

#Floor division
print(10//3) # returns 3

#Exponentiation
print(10**2) # returns 25
```

## Logical Operators
```python
# and (no &&)
print(3<=5 and 5 <= 3) # returns False

# or (no ||)
print(10>3 or 2>3) # returns True

# not (no !)
print(not 3<5) # returns False
```

## Membership Operators
``` python
# in
print('c' in 'cat') # returns True

# not in
print('c' not in 'cat') # returns False
```

## Comments
``` python
#Single Line

'''
Multi 
line 
comments
'''
```

## String
### String Slicing
```python
x = "python"
x[-1] # returns 'n', the LAST element
x[-2] # returns 'o'
x[1:6] # returns ython
x[6:6] # returns empty string
x[6:6] == '' # returns true
x[-2:1] == '' #returns true. -2:1 is 4:1 which doesn't make sense
x[1:] # returns ython. 1 to end
x[:4] # returns pyth. 0 to end - 1. CAUTION
x[:-1] # returns pytho
x[:] # returns python
```

### String Methods
```python
x = "PYthon"
y = "hello world haha"

x.lower() # return python
x.upper() # return PYTHON
x.capitalize() # returns Python (capitalize first letter)
y.title() # returns Hello World Haha (capitalize first letter of every word) 
y.split() # returns list ['hello', 'world', 'haha']
y.count('hello') # returns 1
y.count('o') # returns 2
x.startswith("hel") # returns true
x.endswith("aha") # returns true
"...f.o.o...".strip(".") # returns f.o.o the method removes "." from START and END ONLY
"   f o o   ".strip() # returns f o o it strips ' ' from string
```

### Printing Strings
```python
he = "hello"
wo = "world
print("hello" + " " + "world") # hello world

```

## Sources
https://cbea.ms/git-commit/#why-not-how

https://github.com/joelparkerhenderson/git-commit-template

