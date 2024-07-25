# Simple I/O (Input/Output)

For most of this course, we will work with the **console**. For your programs to be of more use, we need to have a way for the user to interact with them.

## 1. User Input

You can ask the user for input via the console using the ``input()`` function.

For example,

```python
input("Please enter something:\n")
```

will print out ``Please enter something`` and then a blank line (this is because of the ``\n`` escape character in the string). 

The user can then enter something. Try this in **main.py**

## 2. Storing User Input

The above code does not store the input that the user enters. To do this you need to assign it to a **variable**. Update **main.py** as follows:

```python
input_string = input("Please enter something:\n")
print(f"You entered - {input_string}")
```

Now the input is stored in the **variable** ``input_string`` and we can use it in our program. 

You can think of ``input_string`` as a box that stores the input from the user. We can then get the contents of the box at different points of our program.

The line,

```python
print(f"You entered - {input_string}")
```

uses a Python **f-string**, which just lets you put the contents of the variable into the string. Here we put the contents of ``input_string`` in between the curly braces ``{}``.

We will discuss **variables** and **f-strings** a lot more in the next unit.

## 3. Casting the Input

Whenever you get input from the user, it will be of type ``str``. Sometimes we wish to convert this to a number or other type. To do this we can cast the variable to another type. We can cast to an ``int`` using the ``int()`` function.

```python
input_string = input("Please enter a number:\n")
x = int(input_string)
print(f"{x} + 5 = {x+5}")
```

The above code asks for a number, then casts the ``str`` to an ``int`` and then prints the result of adding ``5`` to the number. 

Note that the line `print(f"{x} + 5 = {x+5}")` places the contents of `x` into the curly braces. 

What happens if you don't enter a number? Copy the code into **main.py** and have a play with this.

NOTE: We could have done the casting in one line.

```python
x = int(input("Please enter a number:\n"))
print(f"{x} + 5 = {x+5}")
```


***
# === TASK ===
Create a simple program that asks the user for a number and then prints out 10 times that number

If the user enters ``3`` the program should work as follows:
```
Please enter a whole number:
3
3x10 = 30
```

If the user enters ``10`` the program should work as follows:
```
Please enter a whole number:
10
10x10 = 100
```

***

***Note that to pass the tests you must have exactly the output above, apart from the numbers which will differ depending on what the user inputs.***

HINT: You will need to cast the input to an ``int``.
***

