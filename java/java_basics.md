# Java

## Project Components

Mainly composes of classes, files and packages. 

1. Classes
    - Blueprint for creating objects. 
    - It defines fields (attributes) and methods (functions) that the created objects will have.
2. Files
    - Java Source Files: Each class is typically defined in its own .java file. The filename must match the class name.
    Example: The Car class would be in a file named Car.java.
    - Bytecode Files: When you compile a Java source file, the Java compiler (javac) generates a bytecode file with the .class extension. 
    Example: Compiling Car.java produces Car.class.
    - Execution: The Java Virtual Machine (JVM) executes the bytecode files.
3. Packages
    - Namespaces that organize classes and interfaces into a structured hierarchy. They help prevent naming conflicts and control access.
    - Default Package: Classes with no package declaration belong to the default package.
    - Named Package: Defined using the package keyword at the top of the Java source file.

```java
package com.example.vehicles;

public class Car {
    // Class definition
}
```
```java
import com.example.vehicles.Car;

public class Main {
    public static void main(String[] args) {
        Car myCar = new Car("red", "Toyota");
        myCar.drive();
    }
}
```

Project Structure:

```
MyJavaProject/
|-- src/
|   |-- com/
|       |-- example/
|           |-- vehicles/
|               |-- Car.java
|-- bin/
|   |-- com/
|       |-- example/
|           |-- vehicles/
|               |-- Car.class
|-- lib/
|-- test/
```

- src/: Contains the source files organized by package.
- bin/: Contains the compiled .class files.
- lib/: Contains external libraries and dependencies.
- test/: Contains test classes and resources.

## Build Tools
Java projects often use build tools like Maven or Gradle to manage dependencies, automate the build process, and handle tasks like compiling, testing, and packaging.

Maven: pom.xml
Gradle: build.gradle



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

