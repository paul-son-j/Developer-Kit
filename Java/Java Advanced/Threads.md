# Thread
- **allows us to execute multiple actions at the same time.**
- **Program(application .class) > Process(one process) > Thread (multiple path of execution)**

Can be implemented in two ways.
1. Extending the Thread (old ways):
    - **class Main extend Thread{}**
    - Then we have to override the run method in Thread Class.
    - Create the base class. **Main thread = new Main();**
    - Start th ethread using **thread.start()** method.
2. Implementing the Runnable(basic):
    - **Class Main implement Runnable {
        public void run() {
            // implement thread
        }
    }**
    - Create a Thread object. **Thread thread = new Thread();**
    - Start the thread using **thread.start()** method.
    
Why start() method not the run()?
- Because the run() method will call the method alone.
- But using **start() will tell the JVM to create a thread in System OS level**.

### Why threads exist?
1. improve performance.
2. Background work
3. Concurrency

Note: Main() class itself a single thread in java.

### About threads:
- when executeed the run() method the JVM will create an OS level thread.
- has its own stack memory. (shared heap memory ref:JVM)
- JVM will run the process(method) in that thread.

## Race condition
**When running multiple threads, the value changed by one thread cannot be known to other thread. This results in the logical error called Race condition.**

### Fix: Syncronized Keyword
- The syncrinozed method will allow only one thread execution at a time.
- This can be a method or a code block(Recommended for safety).

##3 Volatile Keywork (Visibility)
- Allow the variable state known to all the threads.
- Good for flags, status checks and not for counter.

### ReentrantLock
- **instead of syncronized we can use ReentrantLock to allow single thread at a time**

Notes:
1. use AtomicInteger -> for Counter
2. Syncronized / lock -> for Complex shared state
3. volatile -> For boolean
4. Use safe collections (concurrent collections).
5. design -> immutability.

Code: [Github](https://github.com/paul-son-j/Scripts/tree/main/Java/ThreadsRaceCondition)

## Deadlock
Having two or more threads and all are waiting for other thread to finished the process is called Deadlock.

### Fix: 
1. Maintain the order of lock eg: sync(a)-> sync(b) follow same in all locks.
2. Avoid nested locks
3. Small lock scope
4. Instead of lock.lock() (wait forever) us lock.tryLock() (non-blocking)

Code: [Github](https://github.com/paul-son-j/Scripts/tree/main/Java/ThreadDeadLock)