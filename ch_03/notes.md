# 1. Chapter 3

> Functions

- [1. Chapter 3](#1-chapter-3)
  - [1.1. Simple `Hello` Function](#11-simple-hello-function)
  - [1.2. Functions with Parameters](#12-functions-with-parameters)
  - [1.3. Functions with Keywords](#13-functions-with-keywords)
  - [The Call Stack](#the-call-stack)
  - [Scope: Global vs. Local](#scope-global-vs-local)
    - [Shopping Mall](#shopping-mall)
  - [Exception Handling](#exception-handling)

## 1.1. Simple `Hello` Function

``` python
def hello()
    print('Howdy!')
    print('Howdy!!!')
    print('Hello there.')

hello() # calls the function defined above
```

## 1.2. Functions with Parameters

``` python
def hello(name):
    print('Hello ' + name)

hello('Bob')
```

## 1.3. Functions with Keywords

``` python
print('cats', 'dogs', 'mice') # => cats dogs mice
print('cats', 'dogs', 'mice', sep=',') # => cats,dogs,mice
```

some functions can have optional parameters/keywords

## The Call Stack

how Python runs code, see [call_stack.py](./call_stack.py)

the Python interpreter starts at the first line and works its way to the bottom.  With defined functions, it can get a little tricky.  essentially, a function has to be *defined* above where it is *called* otherwise the Python interpreter gets confused and doesn't know what to do.

## Scope: Global vs. Local

everything has to be stored somewhere, whether it's a defined function, or a value that is stored inside a variable ie. `x = 5`.  that storage is broken up into spaces that we call *scope*.

### Shopping Mall

You are at a shopping mall looking for shoes.  There is a shoe store, a food court, a computer store, etc. If you go into the computer store and ask for shoes, they don't have an answer for you.  Shoes are out of *scope* for a computer store.  Similarly, each Python program has a *scope* which we call the **Global Scope**.  Each defined function has a *scope*, it is much smaller so we call it a **Local Scope**.

Just like a store in the mall, any piece of code -- whether it's in a **Local Scope** or not -- can call to the **Global Scope**, but cannot call across to another **Local Scope** or even a smaller **Local Scope** within.

Code can have multiple variables of the same name as long as they are stored in different *scopes*.

For a fun example, see [same_name.py](./same_name.py)

## Exception Handling

Exception => a program error => program crash & burn

use the `try`/`except` clauses to handle program errors gracefully
