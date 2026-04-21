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

JVM memory can be splited in to two, One shared by all threads, per thread memory.

1. Accessed/Shared by all
    - Heap -> classes and arrays
    - Method Area
    - Runtime Constant Pool
2. Per thread memory
    - Stack
    - Native memory
    - PC Register (Program Counter)


### Shared Memory
 **Heap:** is a shared memory that holds all the objects and arrays.

 **Method Area:** is a part of heap and it holds the class/interface metadata, fields, methods, constructors.

 **Runtime Constant Pool:** Each class/interface has its own runtome constane pool, per class pool it holds the values of literals, consrtants.

 ### Per thread memory
 **Stack:** is a per thread memory stacked up of **Frames**. each frame represent one method invocation, storing
 -  local variable
 - Frame Data
 - Operand stack.
 
 **Native Memory**: it will be created when the JVM execute the native methods. store frames for native method
 **PC registers:** holds the address of the currrent instruction to be executed.


 | Area                       | Shared?    | Purpose                                     |
| -------------------------- | ---------- | ------------------------------------------- |
| **Heap**                   | Yes        | Stores all objects & arrays                 |
| **Method Area**            | Yes        | Stores class metadata, methods, static vars |
| **Run-Time Constant Pool** | Yes        | Stores constants & symbolic references      |
| **PC Register**            | Per Thread | Tracks current instruction for a thread     |
| **JVM Stack**              | Per Thread | Stores call frames for Java methods         |
| **Native Method Stack**    | Per Thread | Stores frames for native method calls       |

Refer: [JVM Flow](image.jpg)