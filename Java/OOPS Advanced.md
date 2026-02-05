# OOPS Advanced

## Encapsulation
 - **is to make sure certain informtion is hidden from the user.**
 - can be achieved using private access modifier and the getter, setter methods.

### why?
- increased security of data.
- better control over class and method.

## Inheritance
- **is to inherit the methods and attributes of another class**
- can be achieved using the keyword **extends**.
    - **subclass** is the child class
    - **superclass** is the paernt class

### why?
- code reusability.

### Note: 
1. final class cannot be inherited.
2. private modifier methods or attribbutes can not be accessed.

## Polymorphism
- **means many forms.**
- inheriting many class to have same method works differently.
- This allows us to perform a single action in different ways.

### why?
- code reusability.

## Abstraction
- **means hiding certain details and showing only the required details.**
- This can be achieved by both **abstract** and **interface**.

### Abstract 
- Abstract class cannot be used to create object. It has to be inherite first.
- Abstract method cannot have body. The inherited class have to imoplement it.

### why?
- To achieve security - hide certain details and only show the important details of an object

### Interface
- is the strict blueprint. Class that extending the interface have to implement the defined methods

### Why interface over abstract?
1. A class cannot inherit mutiple class, but implementing imterface, we can have multiple interface.

### Note:  
1. Interface does not have constructor. 
2. Interface methods are by default abstract and public.
3. Interface attributes are by default final, static and public.


## Anonymous class
- **are the classes without names.**
- these are used to override an method of a class or interface.

### why?
To override a method of a class for one time use.
