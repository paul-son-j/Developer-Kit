# Exceptions
Before exception we have to know what are the types of error in java
1. Compile time error -> Invalid syntax, undeclared variables.
2. Run time error -> Array index out of bounds, Divided by zero.
3. Logical error -> Wrong answer by code.


When an error occurs, Java will normally stop and generate an error message. The technical term for this is: Java will throw an **Exceptions**.

## try.. catch - final
- try keyword is to box the code which might broke with Exception.
- catch() is used to handle the particular exception.
- final regardless of the result after the try.. catch the final block of code will be execute.

## throw keyword
- allows us to create a custom exception with the java provided exception.

## Multiple Exception
1. catch can be defined multiple times to catch differernt exception.
2. Order of the Exception need to be maintained, so that the Exception won't handle in the generic one first.

## try with resource
- when working with streams and files. we have to close these objects manually after use.
- or else the object will be open and will not be cleaned by the GC or can not be reopen till the program ended or crashed.
- try with resource allows us to close the resource object after the blockl executed automatically, even there occurs an error.
