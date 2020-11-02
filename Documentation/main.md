# Alter Documentation
Alter Documentation, the following is all that is currently avalible to you! The rest is under development or testing. 

## Say Statement
The say statement is used to output things to the terminal. It allows the program to communicate with the user.  
### Basic statement
`say "Hello, World!"`
Let's break down the syntax: first we tell the computer that we wish to output something onto the terminal by saying, "say" then in quotes, we tell it what to say, sort of like we would in english.
### Printing variables
```
name = "Alter"
say name
```
With the above example, we can print out the values of [variables](#Variables). 
We can also print out multiple variables at once like this:
```
name = "Alter"
age = 1
say name, age
```
### Mixing the two
```
name = "Alter"
say "My name is: " + name
```
This allows us to print a mix of text and variables. We join the 2 together by using the + sign.

An example of everything together:
```
name = "Alter"
age = 1
say "My name is " + name + ", and my age is " + age
```
## Input statement
The Input statement is used to ask for "Input" from the user. 
This statement can be used in a variety of scenarios but a simple example is that Input statements are like questions on a test where the test taker is like the user of the program. 
### Here is an example of a basic statement
`ask "What is your name?"`
or 
`get "What is your name?"`
Let's break down the syntax: The ask/get statement uses code very similar to the say statement. 
First we write "ask" or "get" which tells the computer to ask the user the text that follows. 
Then we put the text we want to ask in quotes and then write "What is your name?"
### Example of the ask/get statement used with the say and variable statements
```
name = ask "What is your name"
say "Welcome to Alter: " + name
```
## Variables
Variables are a way to store information, and then reference it later in your program.
You can think of them as dictionaries, you assign a value to name of the variable.
### Setting variables
Variables can be set using the following syntax:
`name = value`
Real world example:
`age = 13`
### Using variables
Once a variable is set, we can access the value of variables in like a say statement
```
name = Alter
say name
```
### The values of variables
variables can be either a float(decimal number), an int(whole number), a string(text, put in quotes), or a boolean(true or false).
```
f = 1.02
i = 20
s = "I Am a String"
b = True
```