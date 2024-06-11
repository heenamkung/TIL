# Java

## Object vs Instance
``` java
public Class Person{}
...
Person A; // object
A = new Person(); // Instance
```
## Static Keyword
- Classes that contain static variable/method automatically take up memory even if the class is never used.
- Non static variables are allocated in heap - GC takes care of this memory. 
- Static variables are stored in Method Area. Memory is released only when the program is terminated.

## Overloading, Overriding
 Overloading: Same method name but with different parameters. 
``` java
void multiple(int a, int b)
void multiple(int a, int b, int c)
```

Overriding:
Child class redefines the method of parent class. Static, final methods cannot be overriden.
```java
class Animal{
    void eat(){
        return;
    }
}

class Person extends Animal{
    @Override
    void eat(){
        return;
    }
}
```

## Abstraction
Two types of abstractions: data abstraction, process abstraction.

### Data Abstraction:
- Focus on similarities and discard differences
- Cats, dogs, and monkeys are categorized into animal


```java
abstract class Animal{
    public abstract void animalSound();
}
class Pig extends Animal{
    public void animalSound(){
        //oink
        return;
    }
}

class Dog extends Animal{
    public void animalSound(){
        //bark
        return;
    }
}
```

### Process Abstraction:
- Hide internal process
- DB can hide how it processes data, while being easily accessible through insert, upsert queries