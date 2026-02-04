# Modifier
1. Access modifier (controls the access level)
2. Non Access Modifiers (not controls the access level - how to behave)

### Access Mofifier - Public, Private, default, Protected

- For **Class**,
    - Public -> accessable by any other class.
    - Default -> accessable by classes within the package. (this is the default functionality.)

- For **attributes, methods and constructors**,
    - Public ->  accessable by any other class.
    - Default -> accessable by classes within the package.
    - Private -> accessable only within the class.
    - Protected -> accessible in the same package and subclasses.

### Non Access Modifier - final, static, abstract
- does not provide access, instead it is an addon on how to behave (class, method, variable)
- Types
    1. Static -> belong to the class, no to the individual object.
        - variable -> belong to class, can be used without object
        - method -> belong to class, can be used without object
        - class -> used with nested class, can bve used without object(outer class creation).
    2. final ->  cannot be change
        - variable -> cannot be ressigned
        - method -> cannot be overriden
        - class -> cannot be inherited
    3. abstract -> implement later 
        - ref: [Abstract vs Interface](Main.md)
    4. synchronized -> thread lock
        - allow single thread to execute
    5. volatile -> Always read from main memory
        - Ensures visibility across threads.
        - prevent stale value in concurrent
    6. trancient -> Do not serialize(meaning: convert object to bytes)
    7. strictfp -> precise math in float
    8. native -> call code in C/C++

