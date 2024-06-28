# Spring Boot REST API
REST (Representational State Transfer) API is a set of rules and conventions for building and interacting with web services.

## HTTP methods
### GET: Get resource
- CRUD: R
- *Idempotency (멱등성): O
- **Safe: O

*Performing the operation multiple times will yield the same result as if it was executed only once
** Operation does not alter the state of server

### POST: Create new resource / Add Resource
- CRUD: C
- Idempotency: X
- Safe: X

### PUT: Create new resource / Update resource
- CRUD: C / U
- Idempotency: O
- Safe: X

### DELETE: Delete resource
- CRUD: D
- Idempotency: O
- Safe: X

## GET Method in Spring Boot
### Path Variable
Using path variable (part of the URL path) to send data to server. Used to identify specific resources
```java
@RestController // Controller that handles rest api
@RequestMapping("/api") // Handles all addresses that has /api
public class RestApiController {

    //When get method arrives at api/hello, this method is called.
    //Called at http://localhost:8080/api/hello
    @GetMapping(path = "/hello") 
    public String hello(){
        var html = "<html> <body> <h1> Hello Spring Boot </h1> </body> </html>";
        return html;
    }

    //Takes data from the URL for processing
    //Called at http://localhost:8080/api/echo/blahblah
    // message = "blahblah"
    @GetMapping(path = "/echo/{message}")
    public String echo(
            // Gets message from path {message}. 
            // The name MUST match with the name in annotation (message)
            //@PathVariable String message 

            // Same as the commented code above, but we can use different variable name (msg)
            @PathVariable(name="message") String msg 
    ){
        System.out.println("echo messsage : " + msg);
        return msg;
    }

    // "is-man" because URL can't have capital letters
    @GetMapping(path = "/echo2/{message}/age/{age}/is-man/{isMan}")
    public String echo2(
            @PathVariable(name="message") String msg,
            @PathVariable int age, // age can be Integer or int. Integer can take null values. But URL never gets a null value, so use primitive type int.
            @PathVariable boolean isMan
    ){
        // http://localhost:8080/api/echo2/hello/age/15/is-man/true (true, false, 1, 0)
        System.out.println("echo messsage : " + msg);
        System.out.println("echo age : " + age);
        System.out.println("echo isMan : " + isMan);
        return msg.toUpperCase();
    }


}
```

### Query Parameter
Used to sort/filter resources. Located after the '?' in the URL.

Example: /users?age=25&country=USA

```java
    // http://localhost:8080/api/book?category=IT&issuedYear=2023&issued-month=01&issued_day=31
    // Manual parsing - useful when there are few query parameters
    @GetMapping(path = "/book")
    public void queryParam(
        @RequestParam String category,
        @RequestParam String issuedYear,
        @RequestParam(name = "issued-month") String issuedMonth, //Java string can't have hyphen, so need to set name.
        @RequestParam(name = "issued_day") String issuedDay
    ){
        System.out.println("Category: " + category);
        System.out.println("issuedYear: " + issuedYear);
        System.out.println("issuedMonth: " + issuedMonth);
        System.out.println("issuedDay: " + issuedDay);
    }

    // http://localhost:8080/api/book2?category=IT&issuedYear=2023&issuedMonth=01&issuedDay=31
    // Receive data by an object - useful when they are many query parameters
    @GetMapping(path = "/book2")
    public void queryParamDto(
            BookQueryParam bookQueryParam
    ){
        System.out.println(bookQueryParam);
    }
```

```java
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
import org.springframework.web.bind.annotation.RequestParam;

@Data //getter setter made from lombok
@AllArgsConstructor // Creates constructor with all 4 variables as parameter
@NoArgsConstructor // Creates constructor without any parameter
public class BookQueryParam {
    private String category;
    private String issuedYear;
    private String issuedMonth; // notice the url is now camelCase
    private String issuedDay;
}
```

