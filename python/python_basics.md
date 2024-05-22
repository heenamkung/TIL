# Python Basics
Here are some basics I learned about python, coming from a C# background.

For most of the example code below, assume they are inside the print() function. 

## Spacing
```
Spaces are the preferred indentation method.

Tabs should be used solely to remain consistent with code that is already indented with tabs.

Python disallows mixing tabs and spaces for indentation. PICK ONE.
```

## Capitalized Booleans
```python
if(True)
    print("Hello")
if(False)
    print("World")
```

## Type Conversion
```python
int('1') # 1    integer
int('1.5') # error    it's a string not a float
int(float('1.5')) # 1    integer

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
10%3 # 1

#Floor division
10//3 # 3

#Exponentiation
10**2 # 25
```

## Logical Operators
```python
# and (no &&)
3<=5 and 5 <= 3 # False

# or (no ||)
10>3 or 2>3 # True

# not (no !)
not 3<5 # False
```

## Membership Operators
``` python
# in
'c' in 'cat' # returns True

# not in
'c' not in 'cat' # returns False
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
### Slicing
```python
x = "python"
x[-1] # 'n'    the LAST element
x[-2] # 'o'
x[1:6] # ython
x[6:6] # ''    empty string
x[6:6] == '' # True
x[-2:1] == '' # True    -2:1 is 4:1 which doesn't make sense
x[1:] # ython    1 to end
x[:4] # pyth    
x[:-1] # pytho    0 to end-1. CAUTION
x[:] # python
```

### Methods
```python
x = "PYthon"
y = "hello world haha"

x.lower() # python
x.upper() # PYTHON
x.capitalize() # Python   capitalize first letter
y.title() # Hello World Haha    capitalize first letter of every word) 
y.split() # list ['hello', 'world', 'haha']
y.count('hello') # 1
y.count('o') # 2
x.startswith("hel") # True
x.endswith("aha") # True
"...f.o.o...".strip(".") # f.o.o    the method removes "." from START and END ONLY
"   f o o   ".strip() # f o o    it strips ' ' from string
```

### Printing
```python
foo = "FOO"
bar = "BAR"
"This is {} and this is {}.".format(foo, bar) # This is Foo and this is Bar.
"This is {0} and this is {1}.".format(foo, bar) # This is Foo and this is Bar.    0 =foo, 1 = bar
f"This is {foo} and this is {bar}" # This is Foo and this is Bar    Careful of f in front of string
f"This is \"{foo}\" and this is \"{bar}\"" # This is "FOO" and this is "BAR"     \n \' \'' are all escape characters
```

## List
```python
my_list = ["foo", "bar", 3.14, True, False] # Elements doesn't need to be type specific
temp_list ["temp", "values"]
new_string = "baz"
empty_list = []

# Similar to strings
my_list[0,2] # ["foo", "bar"]    same as string slicing

"foo" in my_list # True    checks if element is inside, returns boolean

len(my_list) # 5

# Editing list
my_list[1] = "foo" # ["foo", "foo", 3.14, True, False]
my_list.append(new_string)  # ["foo", "bar", 3.14, True, False, "baz"]
my_list.remove("foo") # ["bar", 3.14, True, False]
my_list.extend(temp_list) # ["foo", "foo", 3.14, True, False, "temp", "values"]

# Many other methods (insert, pop, clear, sort, index...)
```

## Tuple
Similar to lists but uses a different syntax and CANNOT be modified. Read-only version of list
```python
_list = ["foo", "bar", 1] # square brackets for list
_tuple = ("foo", "bar", 1) # round brackets for tuple

# Packing and Unpacking
_tuple = ("foo", "bar", 1, 2, "baz") # packing
(var1, var2, var3, var4, var5) = _tuple # unpacking    values are inserted into var1~5 variables

(one, two, *others) = _tuple # asterisk(*) inserts the rest of the tuple elements inside a LIST
*others # [1, 2, "baz"]    notice the SQUARE BRACKETS
(*others, one, two) = _tuple # 
*others # ["foo", "bar", 1]
(one, *others, two) = _tuple # 
*others # ["bar", 1, 2]

```