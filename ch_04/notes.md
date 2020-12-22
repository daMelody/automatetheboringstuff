# 1. Chapter 4

> Lists

- [1. Chapter 4](#1-chapter-4)
  - [1.1. Accessing Values within the List](#11-accessing-values-within-the-list)
  - [1.2. Attempting to Access Indexes Outside the List](#12-attempting-to-access-indexes-outside-the-list)
  - [1.3. Hierarchical Lists](#13-hierarchical-lists)
  - [1.4. Negative Indexes](#14-negative-indexes)
  - [1.5. Chef Boyardee (Slicing Lists)](#15-chef-boyardee-slicing-lists)
  - [1.6. The `len()` function](#16-the-len-function)
  - [1.7. Mutating Values in a List](#17-mutating-values-in-a-list)
  - [1.8. Concatenating & Replicating Lists](#18-concatenating--replicating-lists)
  - [1.9. Removing Values from Lists](#19-removing-values-from-lists)
  - [1.10. Iterating over Lists](#110-iterating-over-lists)

``` python
list_one = [1,2,3]
list_two = [1, None, True, 'hi there']
```

lists contain items, which can be of any type

## 1.1. Accessing Values within the List

Lists are *zero-indexed*, meaning that the first item in a list is at index 0.

``` python
spam = ['cat', 'bat', 'rat', 'elephant']
spam[0] # => 'cat'
spam[3] # => 'elephant'
# interesting syntax note
['one', 'two', 'three'][2] # => 'three'
```

## 1.2. Attempting to Access Indexes Outside the List

Attempting to access an index that doesn't exist will create an `IndexError`.

## 1.3. Hierarchical Lists

Lists can contain lists inside them.  Plenty of fun challenges regarding "flattening" lists and traversing hierarchical lists using recursion.

``` python
listy = ['cat', ['bark', 'tree', 'thin'], ['one', []]]
```

## 1.4. Negative Indexes

Yes, there is such a thing as negative indexing in Python. Just think of it as counting backwards from the last item.  So index of `-1` is the last value, `-2` is the one before that...

## 1.5. Chef Boyardee (Slicing Lists)

Sometimes we just want part of a list.  We can specify a sub-list by using the syntax `listy[x:y]` which returns a list of *item x* up to, but not including, *item y*.  Leaving out one side of the colon or the other results in taking each value *up to* the specified index or each value *starting with* the index value.

``` python
listy = ['cat', 'bat', 'rat', 'elephant']
spam[1:3] # ['bat', 'rat']
spam[0:-1] # ['cat', 'bat', 'rat']
spam[:2] # ['cat, 'bat']
```

## 1.6. The `len()` function

`let(listy)` will return the length of a list (ie. number of items in the list)

## 1.7. Mutating Values in a List

It is possible to selectively change values inside a list

``` python
listy = [1,2,3]
listy[index] = new_value
```

## 1.8. Concatenating & Replicating Lists

Python allows one to add lists to each other, as well as easily create a repeated list

``` python
[1,2,3] + ['A','B','C'] # => [1,2,3,'A','B','C']
[1] * 3 # => [1,1,1]
listy = [1,2,3]
listy + ['A','B','C']
listy # => [1,2,3,'A','B','C']
```

## 1.9. Removing Values from Lists

Use the `del` keyword

``` python
spam = ['first','second','third']
del spam[1] # => ['first', 'third']
```

## 1.10. Iterating over Lists

This is where the `len()` function is particularly useful.

``` python
listy = ['apples','bananas','cantaloupes']

for i in range(len(listy)):
    print('index: ' + str(i) + ' is ' + listy[i])

# should return:
# index: 0 is apples
# index: 1 is bananas
# index: 2 is cantaloupes
```
