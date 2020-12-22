# 1. Chapter 2

> Logic Flow

- [1. Chapter 2](#1-chapter-2)
  - [1.1. Falsy values](#11-falsy-values)
  - [1.2. Truthy values](#12-truthy-values)
  - [1.3. For loop](#13-for-loop)
  - [1.4. While loop](#14-while-loop)
  - [1.5. Range function](#15-range-function)
  - [1.6. Ending a program early](#16-ending-a-program-early)
  - [1.7. Practice Questions](#17-practice-questions)

ie. `if`, `while`, `for`

important: **remember to think about how your loops will terminate**

`break`:
> will exit a loop

`continue`:
> will skip to next run of the loop

## 1.1. Falsy values

- 0
- 0.0
- '' (empty string)

## 1.2. Truthy values

- anything else

## 1.3. For loop

``` python
for i in range(5):
    print('Jimmy Five Times ('+ str(i) + ')')
```

## 1.4. While loop

``` python
i = 0
while i < 5:
    print('Jimmy Five Times (' + str(i) + ')')
    i = i + 1
```

## 1.5. Range function

examples:

- `range(x)` => from 0 to (not including) X,
- `range(x, y)` => from X to (not including) Y
- `range(x, y, z)` => from X to (not including) Y, going in steps of Z

important: **DO NOT OVERWRITE MODULE NAMES**

## 1.6. Ending a program early

use `sys.exit()`

## 1.7. Practice Questions

1)
    - True
    - False
2)
   - and
   - not
   - or
3) Ctrl+C
4) `break` kicks out of the loop entirely, `continue` moves to the next cycle
5) spam.bacon()
