# Spring

## Beans
In Spring, a bean is an object that is managed by the Spring Inversion of Control (IoC) container. These beans are the backbone of a Spring application and are used to manage the dependencies between different objects.

Easier Version:

A bean in Spring is simply an object that Spring manages for you. Think of it as an instance of a class that Spring creates and takes care of, so you don't have to create it manually.

Key characteristics of beans:

- Lifecycle Management: The Spring container is responsible for the creation, initialization, configuration, and destruction of beans.
- Configuration: Beans can be defined either through annotations (like @Component, @Service, @Repository, etc.) or through XML configuration.
- Dependency Injection: Beans can be injected into other beans to fulfill their dependencies, which helps in decoupling the code.

### Example Code

```java
import org.springframework.stereotype.Component;

@Component  // This tells Spring to manage this class as a bean
public class HelloService {
    public String sayHello() {
        return "Hello, Spring!";
    }
}
```

The HelloService class is marked with @Component, so Spring will automatically create and manage an instance (bean) of it.

```java
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

@Component
public class MyApp {

    private final HelloService helloService;

    @Autowired  // Spring will automatically inject the HelloService bean here
    public MyApp(HelloService helloService) {
        this.helloService = helloService;
    }

    public void run() {
        System.out.println(helloService.sayHello());  // Using the bean's method
    }
}
```

In this case, MyApp has a dependency on HelloService. Spring injects the HelloService bean into MyApp through the constructor.

### @Autowired
- When Spring sees a class with a constructor (even without @Autowired), it checks the types of the parameters in the constructor.
- Spring then looks in its context (which is where Spring-managed beans live) for beans that match those parameter types.
- If a matching bean is found, Spring injects it as a dependency when creating the object.

### Example Code
```java
import org.springframework.stereotype.Component;

@Component
public class MyApp {

    private final HelloService helloService;

    // Spring automatically injects HelloService here
    public MyApp(HelloService helloService) {
        this.helloService = helloService;
    }

    public void run() {
        System.out.println(helloService.sayHello());
    }
}
```

- Constructor parameter: The constructor of MyApp has a parameter of type HelloService.
- Spring's role: Spring looks for a bean of type HelloService in its context (e.g., one marked with @Component, @Service, or other annotations that make it a Spring bean).
- Injection: If it finds a matching bean, Spring automatically injects it when MyApp is created.


## @Component vs @Bean
@Component and @Bean are both used in Spring to define beans, but they serve different purposes and are used in different scenarios. Here’s a detailed comparison:

### @Component:
- Purpose: @Component is a class-level annotation used to automatically detect and register beans during Spring's component scanning.
- Usage: It is used to annotate classes so that Spring will automatically register them as beans in the application context.
- Implicit Registration: When Spring scans your project for components, it automatically detects classes annotated with @Component (or its specialized versions like @Service, @Repository, and @Controller) and registers them as beans.
- Specializations: @Component is a general-purpose annotation, while @Service, @Repository, and @Controller are specializations of @Component for specific use cases (business logic, data access, web controllers).

```java
import org.springframework.stereotype.Component;

@Component
public class MyComponent {
    public void doSomething() {
        System.out.println("Doing something...");
    }
}
```
In this example, MyComponent is automatically registered as a bean when Spring performs component scanning.

### @ Bean:
- Purpose: @Bean is a method-level annotation used to explicitly define a bean within a Spring @Configuration class.
- Usage: It is used inside a class annotated with @Configuration to manually declare and configure beans.
- Explicit Registration: @Bean allows you to manually create and configure beans, which is useful when you want to define how the bean is created, modify the bean, or if the class itself is from an external library and cannot be annotated with @Component.
- Fine Control: You can use @Bean when you need more fine-grained control over the creation of beans (for example, passing parameters, configuring properties, etc.).

```java
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class AppConfig {

    @Bean
    public MyComponent myComponent() {
        return new MyComponent(); // Explicitly defining the bean
    }
}
```

### When to Use Each:
- @Component is best when you want Spring to automatically detect and register your beans. It’s typically used for your own custom classes, such as services, repositories, controllers, or general-purpose components.

- @Bean is used when you need explicit control over how the bean is created or for defining beans from classes that you can’t annotate (like third-party libraries). It’s also useful when bean initialization requires complex logic or additional parameters.

## @Component as singleton

Yes, you can think of @Component in Spring as making a class a singleton (by default) and allowing it to be called elsewhere using Dependency Injection (DI).

### 1. Singleton Scope by Default:
When you annotate a class with @Component, Spring automatically creates a singleton instance (one instance per Spring context) of that class. This means:

The instance of the class will be created once by Spring.
The same instance will be injected wherever needed throughout the application.
This is the default behavior in Spring, called singleton scope. You don’t have to do anything special to get this behavior, it’s automatic.

```java
import org.springframework.stereotype.Component;

@Component
public class MyComponent {
    public void doSomething() {
        System.out.println("Doing something...");
    }
}
```
This MyComponent class will be instantiated by Spring as a singleton. Whenever this class is needed, the same instance will be injected.

### 2. Dependency Injection:
You can inject this @Component bean (the singleton instance) into other classes using Spring’s constructor injection, field injection, or setter injection. This allows you to call the same instance of the @Component elsewhere in your application.

```java
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

@Component
public class MyApp {

    private final MyComponent myComponent;

    // Injecting the singleton instance of MyComponent
    @Autowired
    public MyApp(MyComponent myComponent) {
        this.myComponent = myComponent;
    }

    public void run() {
        myComponent.doSomething();
    }
}
```
In this example, Spring injects the same instance of MyComponent into the MyApp class.

## What can be beans?

While beans are typically instances of classes, Spring allows you to create beans in various forms, depending on your needs.

### 1. Classes (Most Common):
The most common type of Spring bean is a class instance. Any class that is annotated with @Component, @Service, @Repository, or defined via @Bean in a configuration class will be managed as a Spring bean

```java
@Component
public class MyService {
    public void doSomething() {
        // business logic
    }
}
```
In this example, MyService is a class, and an instance of it will be a Spring bean managed by the Spring container.

### 2. Interfaces:
Interfaces themselves cannot be directly instantiated as beans (since they can't be instantiated), but their implementations can be. Spring can manage beans that are instances of classes that implement interfaces.

```java
public interface PaymentProcessor {
    void processPayment();
}

@Component
public class CreditCardProcessor implements PaymentProcessor {
    @Override
    public void processPayment() {
        // process credit card payment
    }
}
```
Here, CreditCardProcessor is an implementation of the PaymentProcessor interface, and Spring manages it as a bean.

### 3. Abstract Classes:
Abstract classes, like interfaces, cannot be directly instantiated as beans. However, any class that extends an abstract class can be a Spring bean if it is marked with an appropriate annotation or defined in a configuration class.

```java
public abstract class AbstractPaymentProcessor {
    public abstract void processPayment();
}

@Component
public class BankTransferProcessor extends AbstractPaymentProcessor {
    @Override
    public void processPayment() {
        // process bank transfer payment
    }
}
```
Here, BankTransferProcessor extends an abstract class, and Spring manages it as a bean.

### 4. Primitive Types, Collections, and Custom Objects:
Spring can manage not just class instances but also primitive types, collections (like List, Set, Map), or any other custom objects, which are often declared as beans via configuration classes.

```java
@Configuration
public class AppConfig {

    @Bean
    public String appName() {
        return "MyApplication"; // Primitive type (String) as a bean
    }

    @Bean
    public List<String> supportedLanguages() {
        return Arrays.asList("English", "Spanish", "French"); // Collection (List) as a bean
    }
}
```

#### Example of DI:
```java
import org.springframework.stereotype.Service;
import org.springframework.beans.factory.annotation.Autowired;
import java.util.List;

@Service
public class LanguageService {

    private final String appName;
    private final List<String> supportedLanguages;

    @Autowired  // Constructor injection
    public LanguageService(String appName, List<String> supportedLanguages) {
        this.appName = appName;
        this.supportedLanguages = supportedLanguages;
    }

    public void printAppInfo() {
        System.out.println("Application Name: " + appName);
        System.out.println("Supported Languages: " + supportedLanguages);
    }
}
```

Here, the LanguageService class has its appName and supportedLanguages dependencies injected by Spring. You can now call the printAppInfo() method to access and use the beans.

```java
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.beans.factory.annotation.Autowired;
import java.util.List;

@RestController
public class AppController {

    private final String appName;
    private final List<String> supportedLanguages;

    @Autowired
    public AppController(String appName, List<String> supportedLanguages) {
        this.appName = appName;
        this.supportedLanguages = supportedLanguages;
    }

    @GetMapping("/app-info")
    public String getAppInfo() {
        return "App: " + appName + " supports " + supportedLanguages;
    }
}
```

In this controller:

The appName and supportedLanguages beans are injected into the AppController.
The getAppInfo() method is a handler for an HTTP GET request, returning information about the application name and supported languages.

## DI (Dependency Injection) in Spring


In Spring, Dependency Injection (DI) is the process by which the Spring IoC (Inversion of Control) container automatically manages and injects dependencies (i.e., the required beans) into your classes. This process is crucial for decoupling object creation from object usage and helps in making the code more modular and testable. Let’s look at how DI works internally in Spring.

How Dependency Injection Happens in Spring:
### 1. Component Scanning and Bean Registration:
Spring starts by scanning the application for beans and registers them in the IoC container. This happens when Spring Boot starts or when the Spring context is initialized in any Spring-based application.

Component Scanning: Spring automatically detects classes annotated with @Component, @Service, @Repository, @Controller, or any other stereotype annotations.

@Configuration and @Bean: Spring also detects configuration classes (@Configuration) and methods annotated with @Bean, which define beans manually.

### 2. Bean Creation:
When Spring detects classes marked with @Component, @Service, or @Bean, it creates an instance of these classes (beans) and registers them in the Spring IoC container.

Each bean is managed as a singleton by default, meaning Spring creates only one instance of the bean and reuses it across the application.

For each bean, Spring creates a bean definition internally. This includes the bean’s name, type, scope, dependencies, and the way it will be instantiated.

### 3. Dependency Resolution:
Once the beans are registered in the IoC container, Spring determines dependencies for each bean by examining the class constructors, fields, or setter methods.

If a class has a constructor with parameters, Spring resolves the dependencies by checking the types of the parameters.
If a field is annotated with @Autowired, Spring checks the field’s type to figure out what bean needs to be injected.
If a setter method is annotated with @Autowired, Spring will inject the corresponding bean into the method.
### 4. Dependency Injection (DI):
Once the dependencies are resolved, Spring injects the required beans into the classes at runtime. There are three main types of DI in Spring:

1. Constructor Injection (Preferred):

Spring uses the constructor to inject dependencies.
When Spring creates an instance of a bean, it looks for the bean’s constructor and checks if any of the parameters can be resolved as beans in the IoC container.
If there’s only one constructor, Spring automatically uses it, even without @Autowired.
```java
@Component
public class MyService {
    private final UserRepository userRepository;

    @Autowired
    public MyService(UserRepository userRepository) {
        this.userRepository = userRepository;  // Dependency is injected here
    }
}
```
2. Field Injection:

Spring injects dependencies directly into class fields using the @Autowired annotation.
Spring resolves the field’s type and injects the corresponding bean into it.
```java
@Component
public class MyService {
    @Autowired
    private UserRepository userRepository;  // Field injection happens here
}
```
3. Setter Injection:

Dependencies are injected through a setter method. Spring identifies the setter method and resolves the dependencies based on the parameter types.
```java
@Component
public class MyService {
    private UserRepository userRepository;

    @Autowired
    public void setUserRepository(UserRepository userRepository) {
        this.userRepository = userRepository;  // Dependency is injected via setter
    }
}
```
### 5. Lifecycle Management:
Once all dependencies are injected, Spring manages the lifecycle of the beans:

It creates and initializes the beans as needed.
It also manages destruction of beans if necessary (e.g., when the application context shuts down).
### 6. Handling Bean Scopes:
Spring handles different scopes for beans. By default, Spring beans are singleton, but you can also define other scopes like prototype, request, or session.

- Singleton Scope: Spring creates only one instance of the bean, which is shared across the application.
- Prototype Scope: Spring creates a new instance of the bean every time it is requested.

The bean's scope affects how dependency injection works. For example, prototype beans will be injected as new instances each time.

---
### Internal Steps of Spring DI (Summary):
1. <b>Component Scanning</b>: Spring scans the classpath for beans (annotated with @Component, @Service, etc.) or finds beans declared in @Configuration classes via @Bean.

2. <b>Bean Definitions</b>: For each bean, Spring creates a bean definition that includes information about the bean’s type, scope, and dependencies.

3. <b>Dependency Resolution</b>: Spring analyzes the constructors, fields, and setter methods of the beans and determines what dependencies are required. It resolves these dependencies by looking them up in the IoC container.

4. <b>Bean Instantiation</b>: Spring instantiates the beans and injects the necessary dependencies into constructors, fields, or setter methods.

5. <b>Dependency Injection</b>: Once resolved, Spring injects the dependencies at runtime, ensuring the beans are fully constructed and ready for use in the application.

6. <b>Lifecycle Management</b>  : Spring manages the lifecycle of the beans, including their creation, initialization, and destruction.

### Example Walkthrough:
Here’s an example of how Spring performs DI internally using constructor injection:

```java
@Component
public class MyService {
    private final UserRepository userRepository;

    @Autowired
    public MyService(UserRepository userRepository) {
        this.userRepository = userRepository;
    }
    
    public void doSomething() {
        // business logic using userRepository
    }
}

@Component
public class UserRepository {
    // Data access logic
}
```
What Happens Internally:

1. <b>Component Scanning</b>: Spring scans the application context and finds MyService and UserRepository classes annotated with @Component.
2. <b>Bean Definition</b>: Spring creates bean definitions for both MyService and UserRepository.
3. <b>Dependency Resolution</b>: Spring sees that MyService has a constructor with a UserRepository parameter. It resolves that the UserRepository bean must be injected into the MyService bean.
4. <b>Bean Instantiation</b>:
- Spring first instantiates UserRepository because it's a dependency of MyService.
- Then, Spring instantiates MyService and injects the UserRepository instance into its constructor.
5. <b>Lifecycle Management</b>: The beans are now ready for use, and Spring manages their lifecycle, including initialization and destruction when necessary.
---

### Summary:
- DI in Spring is facilitated by the IoC container, which scans for beans, resolves dependencies, and injects them using constructor, field, or setter injection.
- Spring creates a bean definition for each bean, resolves the dependencies from the IoC container, and injects the dependencies at runtime.
- This entire process decouples object creation from object usage, improving code modularity, testability, and maintainability.

Spring handles all of this automatically, ensuring that your components are created and injected as needed throughout the application's lifecycle.