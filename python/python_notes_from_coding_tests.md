# Python notes from coding tests
A collection of python knowledge that I learned from studying other people's coding test solutions

## Dynamic attribute Creation
Dynamic attribute creation in Python allows you to add new attributes to instances of a class at runtime, even if these attributes were not defined in the class
```python
class DynamicAttributes:
    def __init__(self, name):
        self.name = name

# Create an instance of the class
obj = DynamicAttributes("Test Object")

# Dynamically add a new attribute to the instance
obj.new_attribute = "This is a new attribute"
```
This makes it extremely difficulty to debug when there is a typo (such as mixing node.next and node.nextNode)

## Data Structure
### Remove Duplicates: Set 
Remove all duplicate values
Put them in a set, as a set does not allow duplicate values
```python
set([1,4,1,2,3,51,2,3,2,1,23])
# {1, 2, 3, 4, 51, 23}
```
### Iterate Dictionary with key and value
Use items() method for retrieving both key and value
```python
# Define a dictionary
my_dict = {
    "apple": 2,
    "banana": 3,
    "cherry": 5
}

# Iterate through the dictionary using items()
for key, value in my_dict.items():
    print(f"The key is {key} and the value is {value}")

#output    
#The key is apple and the value is 2
#The key is banana and the value is 3
#The key is cherry and the value is 5
```


## String

### Join
Combine items into one string
```python
a = ["a", "b," , "c", "d", "e"]
b = ["1", "2," , "3", "4", "5"]

result = "".join(a)
# 'abcde'    only works on string items. 
result = "/".join(a)
# 'a/b/c/d/e'
```

### Multiply by number
```python
string = "ABC" * 3
# ABCABCABC
```

### Replace
Remove empty space from string
```python
string.replace(' ', '')
```


### Split
```python
char = "hello".split("e") # ['h', 'llo']
char = " h e l l o ".split() # ['h', 'e', 'l', 'l', 'o']
char = "12:41:15".split(":") # ['12, '41','15']

```
### Strip
```python
"   hello   ".strip()
"   hello   ".strip(" ")
# both results in "hello"

"hello".strip("abcdefgh")
# llo    removes characters from the START and END
# First character h is removed. Then checks e. e is removed. l is not included so checks the end of the string, which is o. o is not included so strip is finished 
```

### Raw String (print strings with special chracters)
```python
# Question: Print !@#$%^&*(\'"<>?:; (source: )
print('!@#$%^&*(\\\'\"<>?:;') # using \\ \' \"
print(r'!@#$%^&*(\'"<>?:;') # using raw string
# same result 
```

## Counting 
### Count both uppercase/lowercase letters
```python
"aaBbBbbbCbbBBb".lower().count('b')
```

## Python Built-in functions
### Map
Executes a given function to each item in an iterable
```python
words = ["hello", "world", "python", "programming"]

# 1. built in method
uppercased_words = list(map(str.upper, words))
# ['HELLO', 'WORLD', 'PYTHON', 'PROGRAMMING']


# 2. custom function with 1 parameter. each item is inserted to parameter
def add_exclamation(word):
    return word + "!"

exclaimed_words = list(map(add_exclamation, words))
# ['hello!', 'world!', 'python!', 'programming!']


# 3. custom function with 2 parameters. requires two list with the same length
def multiply(x, y):
    return x * y
list1 = [1, 2, 3, 4]
list2 = [10, 20, 30, 40]
result = list(map(multiply, list1, list2))
# [10, 40, 90, 160]

```

### Zip
- Combine multiple iterables (such as lists, tuples, etc.) element-wise into tuples. 
- If the iterables are of unequal length, zip stops creating tuples when the shortest input iterable is exhausted.
```python
list1 = [1, 2, 3]
list2 = [4, 5, 6]

summed_list = [x + y for x, y in zip(list1, list2)]
print(summed_list)  # Output: [5, 7, 9]
```

```python
keys = ['name', 'age', 'city']
values = ['Alice', 25, 'New York']

dictionary = dict(zip(keys, values))
print(dictionary)  # Output: {'name': 'Alice', 'age': 25, 'city': 'New York'}
```


### Max, Min
1. Largest of two or more arguments
2. Returns largest item in an iterable

```python
#1. Largest of two or more arguments
maxString= max("990", "1230")
# 990    compares string by each character. first char is 9 and 1


#2. Returns largest item in an iterable
maxString= max(["990", "1230", "abc", "1231235", "151209310", "zpodzf"])
#zpodzf    compares ascii value of each character in string
```

### Ascii Values - ord, chr
```python
ord('a') # 97
ord('d') # 101
chr(97) # a
chr(ord(a)+3) # d  
```

### Sum
Sums an iterable from left to right
```python
sum(range(1,8,2)) #1+3+5+7 = 16 # way to add odd numbers
sum(range(2,8,2)) #2+4+6 = 12 # way to add even numbers
```

## Math

### GCD (greatest common divisor)
```python
from math import gcd
_gcd = gcd(122, 305) # _gcd = 61
```

## Type declaration (Python 3.6)
```python
variable_name : type
number: int
```

```python
def func(variable_name: type) -> type:
    return

```

## Optional Parameter
- When a type can also be None, use optional[type]
- Does NOT mean parameter is optional. Check foo2() below.
```python
from typing import Optional

def foo(bar: int) -> int:
    return bar+5

def foo2(bar: Optional[int]) -> Optional[int]:
    return bar

foo2() # ERROR: missing parameter. In order for this to work, foo2(bar: Optional[int] = None)
foo2(4)
```