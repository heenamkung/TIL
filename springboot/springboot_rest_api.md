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
}

```
