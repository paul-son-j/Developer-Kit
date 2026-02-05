# Generics
**Genberics let us to write classes and methods to work on different data types. So that the developer need not to duplicate the code.**

### Pros:
1. **Code Reusability:** Write one class or method that works with different data types
2. **Type Safety:** Catch type errors at compile time instead of runtime.
3. **Cleaner Code:** No need for casting when retrieving objects.

Example: ArrayList, Collections internally uses generics.

Generic Class:
```Code

class Resource<T> {
    T resource;

    T getResource(){
        return this.resource;
    }
}

class Main{
    Resource<String> strRes = new Resource<>();
    strRes.set("Hello");
    System.out.println("Value: " + strRes.get());

    Resource<int> strRes = new Resource<>();
    strRes.set(10);
    System.out.println("Value: " + strRes.get());
}

```

Generics also works on the methods. 

### Note: 
We can use the **extends** keyword to bound the data types of Generics.
Example: class Resource<T extends Number> {}
means rhe Resource can only have the Subclasses of Number as its datatypes.