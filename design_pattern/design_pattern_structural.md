# Design Pattern - Structural Pattern

## Types of Design Patterns
- Creational (생성패턴)
- *Structural (구조패턴)
- Behavioral (행동패턴)

## Structural
Deal with object composition or the way to assemble objects and classes into larger structures while keeping these structures flexible and efficient.

Example: Proxy, Adapter

## Proxy Pattern
The Proxy Pattern is a structural design pattern that provides an object that acts as a substitute or placeholder for another object. 

A proxy controls access to the original object, allowing you to add a layer of control over the original object's functionality. 

This pattern is useful for various purposes, such as access control, logging, or caching.

E.g. Client accessing server
- Server is http server
- Put https proxy server between client and server.

E.g. Lots of traffic (or ddos)
- Traffic can increase drastically but it might not all be users
- Lots of them might be bots. Need a proxy server (cloudflare) to filter out the bots and block them.

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

