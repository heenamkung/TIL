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


# Object Mapper
- Deserialize JSON to Java DTO
- Serialize Java DTO to JSON
- Example: Jackson Library (spring boot), GSON

In case of empty fields during serialization/deserialization, check getter/setter name.
```java
// UserRequest.java
@Data
@AllArgsConstructor
@NoArgsConstructor
//When receving data, snake case data (user_name) are mapped to camel case (userName).
@JsonNaming(PropertyNamingStrategies.SnakeCaseStrategy.class)
public class UserRequest {

    private String userName;

    private Integer userAge;

    private String email;

    /*
    Don't use primitive type boolean. 
    #1. if null, isKorean is set to default value false.
    #2. lombok will change setter to setKorean not setIsKorean when using primitive boolean and "is" keyword. This results in isKorean always being false.

    e.g)
    @Getter
    private boolean isGood; // isGood();
    private boolean good; // isGood();
    private Boolean isGood; // getIsGood();
    
    */
    private Boolean isKorean;
}
```

```java
// RestApiApplicationTests.java 
class RestApiApplicationTests {

	@Autowired // Spring automatically creates an instance of this class and manages it.
	private ObjectMapper objectMapper;

	@Test
	void contextLoads() throws JsonProcessingException {
		var user = new UserRequest();
		user.setUserName("Hee");
		user.setUserAge(10);
		user.setEmail("abc@gmail.com");
		user.setIsKorean(true);

		
		var json = objectMapper.writeValueAsString(user);
		System.out.println(json);

		

		
		var dto = objectMapper.readValue(json, UserRequest.class);
		System.out.println(dto);
	}

}
```

When receiving or sending JSON with custom syntax (such as all uppercase EMAIL), we can set @JsonProperty("EMAIL") on "private String email;" to send or receive json ```{ "EMAIL" : "abc@gmail.com" }```
```java
@JsonProperty("EMAIL")
private String email;
```

Object mapper can create instance of UserRequest even if the constructor is private.


## Serialization

Object mapper only serializes value from method names starting with 'get'. ``` public String getUserName(){return "hee"} ```


Lombok created getters and setters (@Data annotation) so there's no problem when using lombok. 

However, when we define getters, if there is no ```getUserName()```, ```userName``` will not be serialized to json (json will not contain ```"user_name" : "hee"```). ```"user_name"``` key derives from method name and ```"hee"``` value derives from ```return userName``` in getter.

If there is another method named ```getName()``` that returns ```userName```, then json will have two fields that return userName ```"user_name" : "hee"``` and ```"name" : "hee"```.

To prevent this, use annotation @JsonIgnore to prevent ```getName()``` from getting serialized.

## Deserialization

When reading json (deserialize), dto must contain EITHER setter or getter to work properly.

Without getter or setter (named correctly: "getUserName", "setEmail"), dto will be an UserRequest object with all members set to null.

``` UserRequest {userName: 'null;, userAge: null, email='null', isKorean=null}```

Json suddenly with a ```"user_names":"Hee"``` (user_names not user_name) will cause userName to be null. Fix this by adding @JsonProperty("user_names") to ```private String username```. Or we can create ```SetUserNames(String name){ this.userName = name; }``` to map it correctly

```java
@JsonProperty("user_names") // Overrides JsonNaming
private String username;
```

```java
private void SetUserNames(String name){
    this.userNAme = name;
}
```