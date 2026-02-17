# Spring

- By default spring gives **tomcat** which is a servlet container that manages the servlets.
- A **servlet** is a Java class that can take in a request and return a response
- In a web application, we are talking about HTTP requests and HTTP responses

1. Browser gives **request to Spring MVC** Web Application.
2. The request reaches the web server (e.g., Tomcat, Jetty, or Undertow) embedded in the Spring Boot application.
3. **Filter** -> logging, authorization/authentication, modification takes place
4. **DispatcherServlet** (front controller) --> orchestrates the request processing by delegating it to other components.
5. The `DispatcherServlet` consults the **HandlerMapping** to find the appropriate handler (controller method) for the incoming request based on the URL, HTTP method, or other criteria.
6. If **HandlerInterceptor** is configured, its `preHandle` method is executed before calling the handler.
7. **Handler Execution (Controller Method)** perform business logic or retrieve data from a database. 
8.  If **HandlerInterceptor** is configured, its `postHandle` method is called after the handler executes, but before the view is rendered.
9. The handler (controller) returns a **`ModelAndView`** object or data (like a JSON response in REST APIs).
10. The **`ViewResolver`** resolves the logical view name to a specific view (e.g., an HTML template, JSON response, or another format).
11. **Response Rendering** : The resolved view renders the response.
12. **Handler Interceptor (After Completion)** after the view has been rendered. Clean up
13. Response to the Client.

Diagram:
[Spring Http Request flow](Screenshot%202026-02-17%20at%207.50.11 PM.png)
