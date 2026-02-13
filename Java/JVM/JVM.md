# JVM - Java Virtual MAchine

1. JDK - Java Development Kit (JRE + Debugging Tools)
2. JRE - Java Runtime Environment (JVM + Runtime environment)
3. JVM - Java Virtual Mchine (computing Machine).

As known, JVM cannot able to read any programming language. All it knows it to execute the set of instructions. Therefore, the java compiler compile the java code to source code (or)bytecode to .class file.


 **A class file contains JVM instructions (or bytecodes) and a symbol table, as well as other ancillary information.**

 # 1. Java Virtual Machine architecture overview

## 1.1 DataType
Like Java, JVM also have data types to hold values and perform operations. There are 2 types, namely,
- Primitive Types
    - byte (8 bit signed)
    - short (16 bit signed)
    - int (32 bit signed)
    - long (64 bit signed)
    - float (32 IEEE Precision point)
    - double (64 IEEE precision point)
    - Special types
        - boolean -> usage is minimun in JVM. As no instruction us boolean. Any boolean value will be converted to int.
        - returnAddress -> holds the pointer to the instruction address.
- Reference Types
    - Class reference -> hold reference to the class
    - interface Reference -> holds reference to the interface
    - Array reference -> hold reference to the class or primitive types.
    
All handled via pointers (= reference values) with possible null.

## JVM memory

1. Stack -> local variables, method calls
2. Heap -> classes and arrays
3. Method memory
4. Native memory
5. PC registors
