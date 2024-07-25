# Comments  

In programming languages sometimes it is important to provide comments in your code for either yourself or other people who are going to read your source code. 

Comments are not interpreted by Python and therefore do not affect the running of your code.

There are two types of comments
* Single Line Comments
* Multiline Comments

  ## 1. Single Line Comments

Single line comments start with a ```#``` (hash). For example:
```python 
# This is a single-line comment (This won't run). The line below will.
print("I am learning about comments")
```
Note that the colour of the comment is different to the colour of the code.

  ## 2. Multiline Comments
Unlike many languages, Python does not have multiline comments. If you wish to block out multiple lines you should use the ```#``` for each line For example:
```python 
# This is a single-line comment (This won't run). 
# This is also a single-line comment
print("I am learning about comments")
```
If you highlight a block of code and press ```Ctrl``` + ```/``` it will turn each of the lines into a comment. 

***Note - it is possible to use multiline strings that are triple-quoted to do something like multiline commenting; however, these are actually docstrings (more about this later on). DO NOT DO THIS!***
  ## 3. A Note on Using Comments
  
  There is a lot of debate about when to comment. Some are personal preferences and you will find that every programmer probably does it differently. My basic advice is this.
  
### 3.1 Comment When it is Useful.

For example, the following is not useful:

```python
# This line prints out Hello World!
print("Hello World!")
```

What is the point, everyone knows what this line does!

Commenting when it is not obvious what a piece of code does is useful!

### 3.2 Be Professional

Your comments reflect on you, someone reading it may make a judgement about you based on your comments. For example, don't do the following:

```python
# This code sucks!
print("Hello World!")
```

or 

```python
# Workaround for Tyrion being a traitor and going off with that dragon lady!
print("Hello World!")
```

### 3.3 Keep Comments Brief and Use Multiple Lines

Try to keep your comments to the point and if they are long, break them up into multiple lines.

For example,

```python
# The following is a comment that has the job of telling the person reading the source code that this prints Hello World!
print("Hello World!")
```

would be better as

```python
# Prints Hello World!
print("Hello World!")
```

or:

```python
# The following is a comment that has the following job.
# To tell the person reading the source code that this prints Hello World!
print("Hello World!")
```

***
# === TASK ===

Copy and paste the following code into **main.py**.

```python
# This is a single line comment in Python

print("Replace this line with TASK 1")

print("Hello")
print("World")
print("with Comments")
```

1. Print ```Single line comments start with #``` to the console.
2. Highlight lines 5-7 and use ```Ctrl``` + ```/``` to comment out the lines.

Make sure to check the tests to see that you have passed them!

You can access the tests at any point by clicking on the tests option via the tools menu on the left-hand side of the window.
***