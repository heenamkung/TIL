# Python Basics
Here are some basics I learned about python, coming from a C# background.

For most of the example code below, assume they are inside the print() function. 

## Print
Note that print() ends with a newline. Running multiple print(x) will result in multiple lines of x.

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
# Be aware that converting a non-integer string directly to an integer will cause an error.
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
'c' in 'cat' # True

# not in
'c' not in 'cat' # False
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

### Methods (★)
Strings are immutable, so ALL methods return a new string
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

## Data Structures
### List
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

#List comprehension
my_list = [1,2,3,4,5]
new_list = [x for x in my_list if x > 3] # 4 5
new_list = [x**2 for x in my_list if x > 3] # 16 25
new_list = [x+1 for x in my_list if x > 3] # 5 6
new_list = [str(x)+"번째" for x in my_list if x>3]  # 4번째 5번째
```

### Tuple
Similar to list but uses a round brackets. Also they are immutable, meaning they CANNOT be modified. Read-only version of list
```python
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

### Set
Unlike list or tuple, Set does NOT allow duplicate elements and does NOT preserve order

Think of it as a set of foods that you want to eat. You can't have 2 lasagna elements and the order doesn't matter

```python
foo = {"candy", "chocolate", "coffee"} # curly brackets for set
bar = {"coffee", "cake", "icecream"}

foo.intersection(bar) # {"coffee"}    foo ∩ bar

foo.union(bar) # {"candy", "chocolate", "coffee" , "cake", "icecream"}     foo ∪ bar

foo.difference(bar) # {"candy", "chocolate"}    foo - bar


# Can't access element by index because it is not sorted
foo.add() # add element to set
foo.clear() # empties set
del foo # removes foo 
```

### Dictionary
Composed of key and value. Duplicate keys are NOT allowed 

Curly brackets like set but with : between key and value
```python
_dict = {key1:value1,key2:value2,key3:value3} # hard to read
_dict = { # better readability
    key1:value1
    ,key2:value2
    ,key3:value3
}

# Key supports all types
person = { 
    "name": "foo",
    "age": 5,
    "height": 175,
    25: "string 25",
    True: "string True"
}

# Get values
person[True] # string True
person[25] # string 25
person["age"] # 5
person["nickname"] # error    key "nickname" doesn't exist
person.get("nickname") # None    checks if key exists and returns either the value or None
person.get("age") # 5    

# CRUD
person["nickname"] = "bar" # add data
person[age] = 7 # update data
person.update({"name":"newName", "age" : 9}) # update multiple data at once
person.pop("age") # deletes "age" key

# Get keys
keys_view = person.keys() # dict_keys(['name', 'age', 'height', 25, True, 'nickname'])    returns an object. needs conversion to use this data
keys_list = list(keys_view)
for key in keys_list:
    value = person[key]
    print(f"Key: {key}, Value: {value}") 
'''Output:
Key: name, Value: newName
Key: age, Value: 9
Key: height, Value: 175
Key: 25, Value: text 25
Key: True, Value: string True
Key: nickname, Value: bar
'''

# Get every item
person.items()
''' 
dict_items([('name', 'newName'), ('age', 9), ('height', 175), (25, 'text 25'), (True, 'string True'), ('nickname', 'bar')])    
once again, it returns an object
'''
```

### Summarize
|             | List                         | Tuple  | Set                                 | Dictionary                |
|-------------|------------------------------|--------|-------------------------------------|---------------------------|
| Declaration | l = []                       | t = () | s = {}                              | d = {key:value}           |
| Ordering    | o                            | o      | x                                   | o (python v3.7)           |
| Duplicate   | o                            | o      | x                                   | x (key)                   |
| Access      | l[i]                         | t[i]   | x                                   | d[key], d.get(key)        |
| Update      | o                            | o      | x                                   | o (value only)            |
| Add         | append(), insert(), extend() | x      | add(), update()                     | d[key] = val, update()    |
| Delete      | remove(), pop(), clear()     | x      | remove(), discard(), pop(), clear() | pop(), popitem(), clear() |

### When to use which data structure
List: Manage multiple items in order

Tuple: Manage multiple items in order that CANNOT be modified

Set: Importance in whether the item exists or not, and cannot be duplicated

Dictionary: Use keys to efficiently manage data

### Modifying tuple by type converison
```python
my_tuple = ("foo", "bar")
my_list = list(my_tuple)
my_list.append("baz")
my_tuple = tuple(my_list)
```

### Removing duplicates from list by type comversion.
Using Set: ordering is NOT preserved
```python
my_list = ["foo", "bar", "bar", "bar"]
my_set = set(my_list)
my_list = list(my_set) # ["foo", "bar"] 
```

Using Dictionary: ordering IS preserved
```python
my_list = ["foo", "bar", "bar", "bar"]
my_dict = dict.fromkeys(my_list) # returns {"foo":None, "bar":None}
my_list = list(my_dict) # ["foo", "bar"] 
```

## Syntax:
### if, else, elif
```python
if x==5:
    print("5") # tab or 4 space
elif x==6:
    print("6")
elif x==7:
    print("7")
else:
    print("not 5 6 7")
```
### for
```python
for x in range(5):
    print(x) # 0 1 2 3 4

range(2,6) # 2 3 4 5
range(0,10,2) # 0 2 4 6 8    step = 2

my_list = [1,2,3]
for x in my_list:
    print(x) # 1 2 3

my_tuple = (1,2,3)
for x in my_tuple:
    print(x) # 1 2 3

my_dict = {'name':'foo', 'age':25, 'height': 170}
for x in my_dict.keys():
    print(x)
for y in my_dict.values():
    print(y)
for u, v in my_dict.items():
    print(u, v)

my_string = "apple"
for x in my_string:
    print(x) # apple with new lines between each character
```

### while
```python
x=0
while x<5:
    print(x)
    x +=1 # 0 1 2 3 4
```
### break, continue
```python
for x in range(10):
    if(x==2):
        print(f"x is {x}")
        continue
    if(x==5):
        break   
    print(x) # 0 1 x is 2 3 4
```

### function
```python
#1.
def print_price(x):
    print(f"The price is {x} dollars")
print_price(500) # The price is 500 dollars

#2.
def get_half_price(x):
    return x / 2
print(get_half_price(500)) # 250

#3.
def add_two(x, y):
    return x+y
print(add_two(23,123)) # 146

#4.
def give_price(isVip = False):
    if(isVip):
        return 5000
    else:
        return 7000
print(give_price()) # 7000
print(give_price(True)) # 5000

#5.
def get_price(isVip = False, is_Membership = False, card = False, review = False, first_time = False):
    ...
get_price(review = True, isVip = True) # order does NOT matter

#6
def print_multiple_customer_names(name1, name2, name3, name4 ... ) # don't know how many inputs
def print_multiple_customer_names(*names): # can only include one * for parameters. (x, *y, *z) will cause error 
    for n in names:
        print(n)
print_multiple_customer_names("hey", "i", "just", "met", 5, True, "we") # hey i just met 5 True we
```

### global variable (★)
```python
message = "i'm global"

def do_sth():
    message = "i'm local" # creates a LOCAL variable. It does NOT modify the global variable
    print(message)

def do_sth_to_global():
    global message
    message = "i'm really global" # changes global variable to "i'm really global"
    print(message)

```

### IO
```python
# inp is always a string. in order to add conditions , need type conversion
inp = input("How many do you need") # takes line input, inp is string
inp = int(input("How many do you need")) # inp is int
```
### File IO: open, close
open(file_name, mode, encoding="encoding_mode")

Frequently used mode:
- r : read
- a : append 
- w : write - overwrites existing file or creates new file

```python
# write
f = open('list.txt', 'w', encoding='utf8') # utf8 for korean support
f.write('Name1ㅋㅋ\n')
f.write('Name2ㅋㅋ\n')
f.close()

# read whole content
f = open('list.txt', 'r', encoding='utf8')
contents = f.read()
print(contents)
f.close()
'''output:
Name1ㅋㅋ
Name2ㅋㅋ
'''

# read line by line
f = open('list.txt', 'r', encoding='utf8')
for line is f:
    print(line, end="") ## end is to prevent two newlines. print adds \n and Name1ㅋㅋ\n already has a newline.
f.close()
```

### File IO: with
Ensure resources are properly managed and released (such as closing a file). Best practice to use it when handling file io.
```python
#write example
f = open('list.txt', 'w', encoding='utf8') # before with
with open('list.txt', 'w', encoding='utf8') as f: # after with
    f.write('Name1ㅋㅋ\n')
    f.write('Name2ㅋㅋ\n')
# no need for close() just leave the scope and it's already closed


#read example
with open('list.txt', 'r', encoding='utf8') as f:
    contents = f.read()
    print(contents)

```
## Class
### Basic syntax
```python
class Keyboard:
    pass # used when it is implemented later

k1 = Keyboard() # creating keyboard object
k1.name = "class80" # added name variable inside k1 instance. doesn't apply to any other instance
print(k1.name)
```
### \_\_init\_\_

```python
class Keyboard:
    def __init__(self, name, price): # starts when instance is created
        self.name = name
        self.price = price

k1 = Keyboard("class80", 400)
k2 = Keyboard("mr.suit", 600)


```
### Member variable
```python
class Keyboard:
    def __init__(self, name, price): # name and price are member variable
        self.name = name
        self.price = price

k1 = Keyboard("class80", 400)
k1.color = "red" #only k1 instance has this variable
k2 = Keyboard("mr.suit", 600)
```
### Method
```python
class Keyboard:
    def __init__(self, name, price): # name and price are member variable
        self.name = name
        self.price = price
    def get_name(self): # need to add 'self' when there are no parameters
        return self.name
    def change_name(self, name):
        self.name = name

k1 = Keyboard("class80", 400)
print(k1.get_name()) # class80
k1.change_name("tofu65")
print(k1.get_name()) # class tofu
```
### self
self implies the object itself (similar to this in c# or java)

<b>All</b> class methods must have the first parameter as self

Access member variables by using self.variable_name
```python
class Keyboard:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def print_color(self, color):
        print(f'{self.name}\'s color is {color}')
    
k1 = Keyboard("class80", 400)
k1.print_color("red") # class80's color is red
Keyboard.print_color(k1, "red") # class80's color is red : same result
    
```

### Inheritance
```python
class CustomKeyboard(Keyboard):
    def printType(self):
        print("Custom Keyboard")

CustomKeyboard("f2 84", 300).printType() # Custom Keyboard
```

###
super refers to parent class
```python
class CustomKeyboard(Keyboard):
    def __init__(self, name, price, keys):
        super().__init__(name, price)
        self.keys = keys
```
Multiple Inheritance
```python
class CustomKeyboard(Keyboard, LEDScreen, KeyboardCable):
    def __init__(self, name, price, keys):
        super().__init__(name, price)
        self.keys = keys
```


Method overriding
```python
class CustomKeyboard(Keyboard):
    def printType(self):
        print("Custom Keyboard")

class AdvancedCustomKeyboard(CustomKeyboard("Link65", 400, "88")):
    def printType(self): # Same method name causes method overriding
        print("Advanced Custom Keyboard")

```
Pass
```python
class Keyboard: ## used for designing before implementation
    def __init__(self):
        pass
    def do_sth(self):
        pass

if(A == 0): # Also available for if, while
    pass
elif(A==1):
    do_sth()
else:
    pass

```

## Exception handling
Allows program to continue running in case of error 
```python
try:
    do_sth() # potential error in do_sth
except: # executed when error happens
    fix_error() #
else: # executed when error does not happen
    do_sth_successful()
finally: # executed at the very end (doesn't matter error or not)
    do_sth_done()


# Example
try:
    result = num1 / num2
    print(result)
except:
    print("ERROR!") # when num2 is 0
else:
    print("Success")
finally:
    print("End of error handling")

# Find cause of error
try:
    result = num1 / num2
    print(result)
except Exception as err: # this is used to get the ALL cause of error
    print("ERROR!", err) # when num2 is 0, result is ERROR!division by zero

#Improve from previous example
try:
    result = num1 / num2
    print(result)
except ZeroDivisionError:
    print("Cannnot divide by 0")
except TypeError:
    print("Cannot divide integer by string")
except Exception as err: # When all error cases (zero division, typeerror) above doesn't work, this is the one that is executed
    print("ERROR!", err)


# All error handling processes
# 1. try except
# 2. try finally
# 3. try except else
# 4. try except else finally 
```

## Module
A single python file (.py)
```python
# Two ways to use module

# 1. import module_name 
# Brings in the whole module and use all functionality

# 2. from module_name import variable/method/class 
# Use specific functionalities

#goodjob.py
def say():
    print("Good job!")

#script.py
import goodjob
goodjob.say() # Good job!

from goodjob import say # 
say() # Good job!
```

## Package
Collection of modules
```python

# my_coding/goodjob.py (in folder my_coding)
def say():
    print("Good job!")

# my_coding/goodbye.py (in folder my_coding)
def bye():
    print("Good bye!")

# practice.py 
import my_coding.goodjob
import my_coding.goodbye

my_coding.goodjob.say()
my_coding.goodbye.bye()

# practice2.py
from my_coding import goodjob
from my_coding import goodbye
goodjob.say()
goodbye.bye()

#practice3.py
from my_coding import goodjob, goodbye
goodjob.say()
goodbye.bye()

```






## Sources
https://youtu.be/T6z-0dpXPvU?si=ucaSKc1oyySv5S2b