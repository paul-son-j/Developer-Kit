# Java Methods

### Method: 
- is a block of code, which only runs, when it is called.

### Method Parameter
- it act as a variable inside the method.
- Helps to pass the information inside the method.

### Method Arguments
- Are the input values for any method.
- i.e: value of the method parameter.

### Method Overloading
- is having same method name with different parameters.
- why? To improve code readability, usability, and compile-time polymorphism.

#### Compile-time binding

```code
class A {}
class B extends A {}

void test(A a) {
    System.out.println("A");
}

void test(B b) {
    System.out.println("B");
}

A obj = new B();
test(obj);

//Output: "A"
```
Reason: 
1. Overloading is decided at compile time
2. Based on reference type, not object type.


### Method scope:
- is the area where the variable has the access.

### Method Recursion:
- is function calling itself.
- can be used insted of loop.
