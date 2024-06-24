# Design Pattern - Behavior Pattern

## Types of Design Patterns
- Creational (생성패턴)
- Structural (구조패턴)
- Behavioral (행동패턴)

## Behavioral
- These patterns are concerned with algorithms and the assignment of responsibilities between objects. 
- They focus on how objects communicate with each other.

Example: Observer, Iterator, Strategy

## Strategy Pattern
Defines a family of algorithms, encapsulates each one, and makes them interchangeable

Example: Passport.js
- Use ```passport.authenticate('google');``` to easily authenticate user for various platforms.
- Supports 'google', 'facebook', 'twitter', etc.
- Users can authenticate via various strategies (login methods).
- Creating account with username / password is called local strategy.

```java
interface PaymentStrategy{
    public void Pay(int amount);    
}

class KAKAOCardStrateg implements PaymentStrategy{
    private String name;
    private String cardNumber;
    private String cvv;
    private String dateOfExpiry;

    public KAKAOCardStrategy(String name, String cardNumber, String cvv, String dateOfExpiry){
        this.name = name;
        this.cardNumber = cardNumber;
        this.cvv = cvv;
        this.dateOfExpiry = dateOfExpiry
    }

    @Override
    public void Pay(int amount){
        System.out.println(amount + " paid by KAKAKO card");
    }
}

class GOOGLECardStrategy implements PaymentStrategy{
    private String emailID;
    private String password;

    public GoogleCardStrategy(emailID, password){
        self.emailID = emailID;
        self.password = password;
    }

    @Override
    public void Pay(int amount){
        System.out.println(amount + " paid by GOOGLE card");
    }
}

public class ShoppingCart{
    ...
    public void pay(PaymentStrategy paymentStrategy){
        int amount = calculateTotal();
        paymentStrategy.pay(amount);
    }
    ...
}

public class HelloWorld{
    public static void main(String[] args){
        ShoppingCart cart = new ShoppingCart();

        Item A = new Item("itemA", 100);
        Item B = new Item("itemB", 300);

        cart.addItem(A);
        cart.addItem(B);

        //pay with google card
        cart.pay(new GOOGLECardStrategy("abc@abc.com", "12341234"));
        //part with kakao card
        cart.pay(new KAKAOCardStrategy("Kim Jason", "87655678", "412", "12/05"));
    }
}

```

## Observer Pattern
Allows an object to notify other objects when something changes.

Example: Twitter, MVC Pattern

```java

interface Subject{
    public void register(Observer obj);
    public void unregister(Observer obj);
    public void notifyObservers();
    public Object getUpdate(Observer obj);    
}

interface Observer{
    public void update();
}

class Topic implements Subject{
    private List<Observer> observers;
    private String message;

    public Topic(){
        this.observers = new ArrayList<>();
        this.message = "";
    }

    @Override
    public void register(Observer obj){
        if(!observers.contains(obj)) observers.add(obj);
    }

    @Override
    public void unregister(Observer obj){
        observers.remove(obj);
    }

    @Override
    public void notifyObservers(){
        this.observers.forEach(Observer::update);
    }

    @Override
    public Object getUpdate(Observer obj){
        return this.message;
    }

    public void postMessage(String msg){
        System.out.println("Message sent to Topic: " + msg);
        this.message = msg;
        notifyObservers();
    }
}

class TopicSubscriber implements Observer{
    private String name;
    private Subject topic;

    public TopicSubscriber(String name, Subject topic){
        this.name = name;
        this.topic = topic;
    }

    @Override
    public void update(){
        String msg = (String) topic.getUpdate(this);
        System.out.println(name + ":: got message >> " + msg);
    }
}


public class HelloWorld{
    public static void main(String[] args){
        Topic topic = new Topic();
        Observer a = new TopicSubscriber("a", topic);
        Observer b = new TopicSubscriber("b", topic);
        Observer c = new TopicSubscriber("c", topic);
        topic.register(a);
        topic.register(b);
        topic.register(c);
        
        topic.postMessage("Blah Blah!");
        /* output:
            Message sent to Topic: Blah Blah!
            a:: got message >> Blah Blah!
            b:: got message >> Blah Blah!
            c:: got message >> Blah Blah!
        */
    }
}

```