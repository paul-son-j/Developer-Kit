# Lambda Expressions
**is a short block of code to create any method without name and class.**

## syntax:
    parameter -> expression (or) (parameter) -> {expressions}


Example: 
print( x -> x+10 )

## Why ?
- Lambdas let you pass behavior as data.
- less boilerplate code
- reduce number for unanted classes.

## Lambda works only with functional interface.

### Lambda with methods
**Functional Interface** is an interface with single abstract method.

Example:
```code
interface StringFunction {
  String run(String str);
}

public class Main {
  public static void main(String[] args) {
    StringFunction exclaim = (s) -> s + "!";
    StringFunction ask = (s) -> s + "?";
    printFormatted("Hello", exclaim);
    printFormatted("Hello", ask);
  }

  public static void printFormatted(String str, StringFunction format) {
    String result = format.run(str);
    System.out.println(result);
  }
}
```
### Lambda with variables.
Lambda expression can be stored in variables, it the variable is a Functional Interface. 

Example: 
``` code

interface StringFunction {
  String run(String str);
}

StringFunction m = () -> System.out.println("Hi");

```

### Built-in Functional Interfaces
1. Consumer<T> -> return Consumer
2. Supplier<T> -> return Producer
3. Predicate<T> -> return boolean

## Lambda + Streams 
Readable like english
    
    users.stream()
     .filter(u -> u.isActive())
     .map(User::getName)
     .forEach(System.out::println);

