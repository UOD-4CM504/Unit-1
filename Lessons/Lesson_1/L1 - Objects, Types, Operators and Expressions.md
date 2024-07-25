# Objects, Types, Operators, and Expressions

To do anything useful in our programs, Python will need to represent data such as numbers, words and booleans. We will learn more about these in Units 2 and 3.

For now we will introduce the most common 4 built-in data types.

## 1. Objects and Types
In Python, we will work with **objects**. Every **object** has a **type** that tells the program what can be done with the **object**. Python has a number of built-in **data types** which Python uses internally to represent data.

We will look at 4 of these **data types** to start. We will cover more later in the course as we progress.

| Data Type | Description |
| --- | --- |
| ```int``` | An integer. This is a whole number, it can be positive, negative or zero. e.g. ``5``|
| ```float``` | A decimal number. e.g. ``3.14``
| ```str``` | Text.  It consists of individual characters. Strings are enclosed in single quotation marks `'` or double quotation marks `"`. e.g. ``"Hello World"``|
| ```bool```   | The values `True` or `False`. Used to make decisions, more in Unit 3|


A very useful function in python that we can use is ```type()```. This lets us ask Python what the **type** of an **object** is.

Type the following into the **console** (you will find this to the right of the instructions tab near to top right of the window):

```python
type(10)
```

You will see the output:

```
<class 'int'>
```
This is python telling you that ```10``` is an **object** of **type** ```int```. For now, read class as **type**.

Try it for these other **objects**.

```python
type(10.3)
```

```python
type("This is a string")
```

```python 
type(True)
```

The console automatically prints out the last command. To do this in **main.py** you will need to use the **print()** function. Try the following in **main.py**.

```python 
print(type("This is a string"))
```
This first gets the type of the object, here a ``str`` and then passes that to the ``print()`` function.

## 2. Operators and Expressions

We can combine **objects** with **operators** to form **expressions**. When evaluated, these **expressions** produce a new **object**. 

For example, we can combine the **objects** ```10``` and ```5``` with the ```+``` **operator**,

```python
10 + 5
```
to create a new object ```15``` of type ```int```.

All built-in **data types** have **operators** that we can use to form **expressions**. 

For example, we can test if two **expressions** are equal with the ```==``` comparison **operator**. Type the following **expression** into the **console**,

```python
10 + 5 == 3 * 5
```

This will return ```True```. Python knows how to test whether two numbers are equal and returns you a new **object** of type ```bool```.

We will cover operators for numbers, strings, and bools in their respective lessons in this unit.

***

## 3. Help Function

The ``help()`` function gets information about an object (it can also be used for other things.)

Try typing the following into the **console**:

```python
help(str)
```

Press q (for quit) to exit the help.


# === TASK ===
Update **main.py** to print out the type of the following expressions. You will need to use the ``print()`` and the ```type()``` function.

Make sure you have read all of the above before attempting this (especially the end of Section 1).
```python
12 + 5
```
```python
5 + 3.0
```
```python
12 / 5
```
```python
12 + 5 == 5 * 3.0
```

***