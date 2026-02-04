# Enums - Enumerators
- is a type of class, used to group a similar constants.
- By default, they are unchangable (final)
- they are meaninhful type grouped of public static final.
Eg: USER, ADMIN, DEVELOPER

### Enum Constructors
- have constructor by defalut like class.
- if the Enum has the value to be passed. Explicit constructor is required.
Eg:
``` code
public enum Direction {
    WEST("left"),
    NORTH("UP");

    private final String description;

    Direction(String description) {
        this.description = description;
    }

    public String getDescription() { return description; }
    
}
```

### Enum Switch
- Java 5+ supports Enum Switch
 ``` code
Process status = Process.STARTED;
switch(status) {
    case STARTED:
        System.out.println("Process started");
        break;
}
```
- Java 11# supports Enum Expression
```code
String result = switch(status) {
    case STARTED -> "Process started";
    case IN_PROGRESS -> "Process in progress";
};
```

### Enum methods
1. name() -> gives name of the constant.
2. ordinale() -> gives the position of the constant.
3. compareTO() -> gives the integer value by comparing the other constant.
4. equals() -> check for the equality with other constant.
5. values -> gives the array of enum values
6. valueOf(name) -> gives the values in the Enum constant.

### Why Enum not Public static final constant

1. it helps to group the similar constants.
2. The value can not be ressiagned. Compiler prevents assigning values outside of the predefined set.
3. Enums provide some built-in methods.

### Enum == is faster than equals() - why?
- Enum constants are singletons: The JVM creates exactly one instance per constant and == checks if references point to the same memory address.

