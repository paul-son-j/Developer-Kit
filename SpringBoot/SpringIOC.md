# Spring IOC (inversion of Control) Container
- manages the Bean creation and Bean lifecycle.
- Automatically injects required dependencies into beans.

Container - is a runtime env that manages the all the objects lifecycle.

Bean - is a single object managed by the container. 


## Why Spring IOC?
Imagine we have an interface named SIM and classes implementing the interface named Airtel and Jio. Whenever we have to create an object we have to use new object() to create an object and use its method. 
        
        Eg: Sim s = new Jio(); s.call() 

To call the Airtel we have to change the code to new Airtel(). **A tightly coupled code**

To resolve this, came spring **Bean** where we tell spring that Airtel and Jio are Bean and inject this Bean using any one of the following.
- Bean Factory -> support DI & Bean lifecycle
- ApplicationContext -> DI, BLC + Additional(event handling, annotation)
    1. xml based Bean injection -> 
    2. Java configuration class based Bean injection
    3. Spring Anotation. -> @componentScan at config class and @component at Bean class  and @Autowired to inject the object.

By doing so, we can loosely couple our code.
refer:
