# Exception vs Error

- both are not same and both can not be handled by try..catch.

Both has the same parent classs **Throwable**. Then the java split the throwable into two

## Exception

Exception is a state where your application might handle the problem
Eg: Input file error, Invalid input error...

### Checked and Unchecked Exception

- **Checked** - usually exception thrown by compiler

  - SqlException, IOException
  - Must be handled

- **Unchecked** - extend the runtime exception
  - occurs due to bad programming.
  - NullPointer, IndexOutOfBounds

## Error

Error is a state where the application should not handle the problem.
Eg: OutOfMemoryError, StackOverflow

These occurs due to JVM broken, unstable application.

Error is the java way of telling people this is not your problem to fix.

### What happens if we handle the Error?

Since the error usually means the application is unstable, since we are handling it for not, but at one point the whole scenario becomes diabolical.

## One line:

Exception -> might handle by the application
Error -> should not handle by the application.
