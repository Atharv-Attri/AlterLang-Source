# Alter Documentation
Alter Documentation, the following is all that is currently available to you! The rest is under development or testing. 

<!-- vscode-markdown-toc -->
* [Say/Print Statement](#SayPrintStatement)
	* [Basic statement](#Basicstatement)
	* [Printing variables](#Printingvariables)
	* [Mixing the two](#Mixingthetwo)
* [Input statement](#Inputstatement)
	* [Here is an example of a basic statement](#Hereisanexampleofabasicstatement)
	* [Example of the ask/get statement used with the say and variable statements](#Exampleoftheaskgetstatementusedwiththesayandvariablestatements)
* [Variables](#Variables)
	* [Setting variables](#Settingvariables)
	* [Using variables](#Usingvariables)
	* [The values of variables](#Thevaluesofvariables)
* [While loop](#Whileloop)
* [Dump](#Dump)
* [If](#If)
* [Comments](#Comments)

<!-- vscode-markdown-toc-config
	numbering=false
	autoSave=true
	/vscode-markdown-toc-config -->
<!-- /vscode-markdown-toc -->
## <a name='SayPrintStatement'></a>Say/Print Statement
The say statement is used to output things to the terminal. It allows the program to communicate with the user.  
### <a name='Basicstatement'></a>Basic statement
```
say "Hello, World!"
print "Hello World!"
```

Let's break down the syntax: first we tell the computer that we wish to output something onto the terminal by saying, "say" or "print" then in quotes, we tell it what to say, sort of like we would in english.

:warning:**Henceforth, the documention will only use either say or print, however they are interchangable.**
### <a name='Printingvariables'></a>Printing variables
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
### <a name='Mixingthetwo'></a>Mixing the two
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
## <a name='Inputstatement'></a>Input statement
The Input statement is used to ask for "Input" from the user. 
This statement can be used in a variety of scenarios but a simple example is that Input statements are like questions on a test where the test taker is like the user of the program. 
### <a name='Hereisanexampleofabasicstatement'></a>Here is an example of a basic statement
```
ask "What is your name?"
```

or 

```
get "What is your name?"
```
Let's break down the syntax: The ask/get statement uses code very similar to the say statement. 
First we write "ask" or "get" which tells the computer to ask the user the text that follows. 
Then we put the text we want to ask in quotes and then write "What is your name?"
### <a name='Exampleoftheaskgetstatementusedwiththesayandvariablestatements'></a>Example of the ask/get statement used with the say and variable statements
```
name = ask "What is your name"
say "Welcome to Alter, " + name
```
## <a name='Variables'></a>Variables
Variables are a way to store information, and then reference it later in your program.
You can think of them as dictionaries, you assign a value to name of the variable.
### <a name='Settingvariables'></a>Setting variables
Variables can be set using almost any syntax, and we encourage you to try out something different, but here are a few examples:

```
name = value
set name to value
name should equal value
set name to equal value
```

The full list of templates can be found here: https://github.com/Atharv-Attri/Alter-ML/blob/main/data.json
### <a name='Usingvariables'></a>Using variables
Once a variable is set, we can access the value of variables in like a say statement
```
name = Alter
say name
```
### <a name='Thevaluesofvariables'></a>The values of variables
As of now, variables can be either a float(decimal number), an int(whole number), a string(text, put in quotes), or a boolean(true or false).
```
f = 1.02
i = 20
s = "I Am a String"
b = True
```

## <a name='Whileloop'></a>While loop
While loops are essentially used to perform an action repeatedly "while" a condition is true or false. 
```
while i < 10:
    #action
```
This loop can be combined with other commands like the say statement for example.
```
while i < 10:
    say "I love coding"
```
## <a name='Dump'></a>Dump
Dump gives you a look under the hood of what's going on in your program. It'll show you your variables, their values, and stack hierarchy; its kind of like a debugger.
To use the dump command, all you need to do is:
```
dump
```
Ex:
```
c =  55
s = get 'name'
dump
```
## <a name='If'></a>If
This statement is kind of like a one time version of the while loop. Basically it says "if" something is true or false perform a command. 
```
if i < x:
    i + 1
```
## <a name='Comments'></a>Comments

Comments are used to describe your code, and tell the computer what to ignore. 
You would want to use comments to write down what your code does, or to comment out code that you don't want to run, but don't want to delete just yet.
Ex:
```
# ask the user for input
x = ask ">> "

# not getting number yet
# num = get "Number: "

say x
```