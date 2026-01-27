# Java
- class based object orientied programming
- core principle: Write once run any where (**Platform independent**)
- consist syntax, variables, loop, branching, class, object...

### Javac compile
    converts source code (.java file) to bytecode (.class file). Therefore any system with JVM installed can be able to run the java application(Write once run anywhere).

### JVM
    is a machine, that inteprete the bytecode to machine code. 
    JVM loads the bytecode, verifies it, links it, and then executes it


contains
- Class Loader to load, link, verify and execute the bytecode(.class)
- Memory Areas consist of
    - method memory (store class and method level info)
    - heap memory (store all object)
    - stack memory (local var, method call. each thread has its own stack)
    - pc registors (address of currently executing instruction of each thread)
    - native method stack (each thread -> each native method execution)
- Execution Engine
    - Interpreter -> interprets the bytecode line by line and then executes
    - JIT (Just In Time Compiler) -> JIT provides direct native code for that part so re-interpretation is not required
    - Garbage Collection (GC) ->  It destroys un-referenced objects. 
- JNI (Java Native Interface) -> interface to handle te native method libraries
- Native libraries -> c/c++ native libraries.

### Garbage collection
        clears the unreferenced object from the heap memory.

- heap is divided into 
    - **New Generation** Newly created objects stored here.
    - **Old Generation** long lived objects stored here.

- GC Activity
    - **Minor/Incremental GC** The unreference object in the new generation will be cleared from heap.
    - **Major/Full GC** the object that escaped the minor clean up will be cleaned here. This is a less frequent action.
- Key concept:
    - implicitly make the object unreferenced. (NULL)
    - Call the garbage collection to clean up. System.gc()
    - use the finalize method to clean (deprecated).
