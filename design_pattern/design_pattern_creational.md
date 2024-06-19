# Design Pattern - Creational Pattern

## Types of Design Patterns
- Creational (생성패턴)
- Structural (구조패턴)
- Behavioral (행동패턴)

## Creational
All about how objects are created.

Example: Singleton, Factory

### Singleton Pattern
A class has only one instance. Widely used for database connection.

Pros: A single instance is shared by various modules, saving resources for creating instances. Hence it is used for IO bound applications which has high cost of instantiating.

*IO bound: Tasks that spend more time waiting for input/output operations (read write) than performing computations. 
* Network Communications - downloading a file: spends time waiting for data to be transferred over netowrk
* DB operation - executing SQL queries: wait for DB to process query and return result
* Disk IO - copying a large file: wait for disk to read / write data

Cons: Not suitable for TDD. In TDD, unit tests should be independent, and should work regardless of execution order. However, singleton instance is shared across tests, making it not possible for unit test to have an independent instance. 

### Implementing Singleton

#### Bad Implementation
 The code below does not work properly under multiple threads. JAVA is multi-threaded language. 
```java
public class Singleton{
    private static Singleton instance;

    private Singleton(){

    }

    public Singleton getInstance(){
        if(instance == null){
            instance = new Singleton();
        }
        return instance;
    }
}
```
Problem: Assume thread t1 and thread t2 both call getInstance()

Optimal Case:
1. t1: if(instance == null)
2. t1: instance = new Singleton()
3. t2: return instance (since instance already exists)

Worst Case: Two singletons created. Not singleton anymore
1. t1: if(instance == null)
2. t2: if(instance == null)
3. t1: instance = new Singleton()
4. t2: instance = new Singleton() 


#### Good Implementation 1: Lazy Holder
Create a nested class singletonInstanceHolder, to prevent initialization of singleton when first loaded (saves resource). Instance is only created when getInstance() is called
```java
class Singleton{
    // private constructor prevents instantiation from other classes
    private Singleton(){} 

    private static class singletonInstanceHolder{
        private static final Singleton INSTANCE = new Singleton();
    }

    public static Singleton getInstance(){
        return singletonInstanceHolder.INSTANCE;
    }
}

public class Main{
    public static void main(String[] args){
        Singleton a1 = new Singleton(); // ERROR: constructor is private
        Singleton a2 = Singleton.getInstance();
    }
}
```

#### Good Implementation 2: Enum
Enum is a special class in java that represents a group of constants. Just like a class, it has attributes and methods. The only difference is that enum constants are public, static and final. Also an enum cannot be used to create objects.

Instance of enum is thread safe, and any 'enum' value is only instantiated once in a Java program.

```java
enum Singleton{
    INSTANCE;

    private int value;

    public void setValue(int value){
        this.value = value;
    }

    public int getValue(){
        return this.value;
    }

    public void showMessage(){
        System.out.println("Hello the value is " + value);
    }
}

public class Main{
    public static void main(String[] args){
        Singleton singleton = Singleton.INSTANCE;
        singleton.setValue(20);
        singleton.showMessage(); // 20
        Singleton singleton2 = Singleton.INSTANCE;
        singleton2.showMessage(); // 20
        singleton2.setValue(40);
        singleton.showMessage(); // 40
    }
}
```

### Factory Pattern
- Creational design pattern that provides an interface for creating objects in a superclass, but allows subclasses to alter the type of objects that will be created.
- The super class does not need to know about how the objects are created. All logics regarding instanciating an object is handled in the sub class, allow code to be easily maintained.

```java
enum CoffeeType {
    LATTE,
    ESPRESSO
}

abstract class Coffee{
    protected String name;
    public String getName(){
        return name;
    }
}

class Latte extends Coffee{
    public Latte(){
        name = "latte";
    }
}

class Espresso extends Coffee{
    public Espresso({
        name = "espresso";
    })
}

class CoffeeFactory{
    public static Coffee createCoffee(CoffeeType type){
        switch(type){
            case LATTE:
                return new Latte();
            case ESPRESSO:
                return new Espresso();
            default:
                throw new IllegalArgumentException("Invalid Coffee Type");
        }
    }
}

public class Main{
    public static void Main(String[] args){
        Coffee coffee = CoffeeFactory.createCoffee(CoffeeType.LATTE);
    }
}

```
Classes coffee, latte and espresso are the subclasses that manages object creation. CoffeeFactory is the superclass that is just used for run().


### Dependency Injection(DI)
Dependency Injection is a design pattern used to implement IoC (Inversion of Control), allowing a program to follow the Dependency Inversion Principle.

*Dependency: A -> B (A depends on B). If B changes, A will also change
```java
// A depends on B. if B changes go() to come(), A needs to change go() code to B().come().
class B{
    public void go(){}
}

class A{
    public void go(){
        new B().go();
    }
}
```

*IoC (Inversion of Control 제어의 역전) pattern: 
- IoC pattern is about providing any kind of callback, which "implements" and/or controls reaction, instead of acting ourselves directly (in other words, inversion and/or redirecting control to the external handler/controller) - DI is a specific version of IoC.
``` java
// non IoC example. new SpellChecker() means the TextEditor directly depends on SpellChecker
public class TextEditor {

    private SpellChecker checker;

    public TextEditor() {
        this.checker = new SpellChecker();
    }
}

```
```java
/// IoC example. 
public class TextEditor {

    private IocSpellChecker checker;

    public TextEditor(IocSpellChecker checker) {
        this.checker = checker;
    }
}

SpellChecker sc = new SpellChecker(); // dependency
TextEditor textEditor = new TextEditor(sc);
```
 IoC example creates an abstraction by having the SpellChecker dependency class in TextEditor's constructor signature (not initializing dependency in class). Now the client creating the TextEditor class has control over which SpellChecker implementation to use because we're injecting the dependency into the TextEditor signature.

- Reversing traditional program control structures to achieve increased flexibility and ease of application testability
- Example: input program
    - traditional method: "enter name", "enter address" in command line interface. user input order is fixed
    - Controlling flow of user interaction: GUI program with input fields. User can input that in any order and press submit.

*Dependency inversion principle:
- The conventional dependency relationships established from high-level, policy-setting modules to low-level, dependency modules are reversed, thus rendering high-level modules independent of the low-level module implementation details.
- Implementing DI applies DIP
- Need to follow the 2 rules:
    - High-level modules should not import anything from low-level modules. Both should depend on abstractions (e.g., interfaces).
    - Abstractions should not depend on details. Details (concrete implementations) should depend on abstractions.

#### DI Example: Without DI
Dependency: Project -> BackendDeveloper, FrontendDeveloper

```java
class BackendDeveloper{
    public void writeJava(){System.out.println("write java");}
}

class FrontendDeveloper{
    public void writeJavascript(){System.out.println("write javascript");}
}

public class Project{
    private final BackendDeveloper backendDeveloper;
    private final FrontendDeveloper frontendDeveloper;

    public Project(BackendDeveloper backendDeveloper, FrontendDeveloper frontendDeveloper ){
        this.backendDeveloper = backendDeveloper;
        this.frontendDeveloper = frontendDeveloper;
    }

    public void implement(){
        backendDeveloper.writeJava();
        frontendDeveloper.writeJavascript();
    }

    public static void main(String[] args){
        Project p = new Project(new BackendDeveloper(), new FrontendDeveloper());
        p.implement();
    }
}

```
Changing writeJava() to writeC#() forces Project class code to change the implement() method. Project is dependent on BackendDeveloper and FrontendDeveloper 

#### DI Example: With DI
Dependency: Project -> Developer <- BackendDeveloper, FrontendDeveloper

```java
import java.util.*;

interface Developer{
    void develop();
}
class BackendDeveloper implements Developer{
    @Override
    public void develop(){
        writeJava();
    }

    public void writeJava(){
        System.out.println("write java");
    }
}

class FrontendDeveloper implements Developer{
    @Override
    public void develop(){
        writeJavascript();
    }

    public void writeJavascript(){
        System.out.println("write javascript");
    }
}

public class Project{
    private final List<Developer> developers;

    public Project(List<Developer> developers){
        this.developers = developers;
    }

    public void implement(){
        developers.forEach(Developer::develop);
    }

    public static void main(String[] args){
        List<Developer> dev = new ArrayList<>();
        dev.add(new BackendDeveloper());
        dev.add(new FrontendDeveloper());
        Project p = new Project(dev);
        p.implement();
    }
}
```
- All classes depend on developer interface
- Changing Developer interface method from void develop() to develop2() means changing FrontendDeveloper, BackendDeveloper and also Project classes.
- Can easily add new classes such as iOSDeveloper. Just implement from developer interface.

Pros of DI:
- Easily swap modules (dev.add(new BackendDeveloper()))
- Eases unit testing and migration
- Consistent flow of dependency makes code more accessible

Cons of DI:
- Ultimately adding more code to the project (interface), increasing the complexity
- DI happens in runtime not compile time, so may be harder to find bugs

## Structural
Object/class composition or how objects can be combined to form larger structures.

Example: Proxy, Adapter

## Behavioral
How objects/classes interact and communicate with each other.

Example: Observer, Iterator, Strategy