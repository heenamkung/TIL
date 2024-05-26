# Python notes from coding tests
A collection of python knowledge that I learned from studying other people's coding test solutions


## Data Structure
### Set 
Remove all duplicate values
Put them in a set, as a set does not allow duplicate values
```python
set([1,4,1,2,3,51,2,3,2,1,23])
# {1, 2, 3, 4, 51, 23}
```

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

## String

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