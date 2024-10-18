# Filter, Interceptor, Spring AOP

Filters, Interceptors, and Spring AOP (Aspect-Oriented Programming) are mechanisms used in Spring to handle cross-cutting concerns (such as logging, security, transaction management) and request/response processing, but they work at different levels of the Spring framework.

## Most Common Use Cases for Each:
### Filters
- Authentication: Filters can verify JWT tokens or OAuth2 tokens to authenticate the user before the request reaches the Spring MVC layer.
- Global Logging: Logging every incoming and outgoing request/response for monitoring and debugging purposes.
- CORS Handling: Ensuring cross-origin requests are properly handled with the necessary headers.

### Interceptors:
- Authorization: Verifying whether the user has the appropriate permissions to access the resource (role-based access control).
- Performance Tracking: Measuring the execution time of controller methods and logging it for performance monitoring.
- Controller-Specific Logging: Logging specific requests going to certain controllers or endpoints.

### Spring AOP:
- Transaction Management: Starting, committing, or rolling back transactions declaratively around service methods.
- Audit Logging: Capturing detailed logs of which business methods were called, by whom, and with what parameters.
- Method-Level Security: Applying security rules to individual service methods to check if users have access to certain business operations.

```text
 [ Incoming HTTP Request ]
                |
                v
        +----------------------+
        |       Filters         |  <-- Common Use Case: 
        |  (Servlet Level)      |      - Authentication (JWT, OAuth)
        |  Pre-processing:      |      - Global Request Logging
        |  - Authenticate User  |
        |  - Log HTTP Request   |
        |  - CORS Handling      |
        +----------------------+
                |
                v
        +----------------------+
        |     Interceptors      |  <-- Common Use Case:
        |   (Spring MVC Level)  |      - Authorization Check
        |  Pre-handle:          |      - Logging specific to controllers
        |  - Authorization      |      - Execution time tracking
        |  - Logging start time |
        +----------------------+
                |
                v
        +----------------------+
        |     Spring AOP        |  <-- Common Use Case:
        |  (Method Level)       |      - Method Execution Logging
        |  - Transaction Mgmt   |      - Performance Monitoring
        |  - Security Check     |      - Auditing Business Logic
        +----------------------+
                |
                v
   [ Controller / Service Method ]
                |
                v
        +----------------------+
        |     Spring AOP        |  <-- Common Use Case:
        |  Post-processing:     |      - Post-Transaction Handling
        |  - Audit Logs         |      - Logging method execution time
        |  - Commit/Rollback    |
        +----------------------+
                |
                v
        +----------------------+
        |     Interceptors      |  <-- Common Use Case:
        |  Post-handle:         |      - Logging response details
        |  - Logging execution  |      - Post-processing MVC model
        |    time               |
        +----------------------+
                |
                v
        +----------------------+
        |       Filters         |  <-- Common Use Case:
        |  Post-processing:     |      - Logging HTTP Response
        |  - Log HTTP Response  |      - Security headers, CORS
        +----------------------+
                |
                v
    [ Outgoing HTTP Response ]
```