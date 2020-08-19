import sys
from ply import lex, yacc
import rich
import math
# TODO: Variable, While loop, For loop, math, conversion
# !Due:    12   ,     14    ,    14   ,  12



# ?: Variable: regular syntax: a = 2, a = "say", a = true. ENG syntax: set a to 2
# ?: Math: regular syntax: 1+1 = 2, a += 1. ENG syntax: add 1 to a, add a to b
# TODO: ?: While loop: TODO
# TODO: ?: For Loop

# TODO: add reserved
ERROR = False
reserved = {
    'say' : "SAY",
    'if': "IF"

}

tokens = [
    'MULTIPLY',
    'QUOTE',
    'SPACE',
    'EQUAL',
    'QTEXT',
    'DIVIDE',
    'PAREN_IN',
    'BOOL',
    'VARIABLE',
    'NUMBER'
] + list(reserved.values())

meta = [

]
 
variables = {

}

t_DIVIDE = r"[A-Za-z0-9]+/[A-Za-z0-9]+"
t_MULTIPLY = r"\w_ ?\*\w_ ?"
t_SAY = "say"
t_IF = "if4"
t_QUOTE = r"\"" 
t_SPACE = r"\s"
t_QTEXT = r"\".+_ ?\""
t_EQUAL = r".+_ ?=.+_ ?"
t_PAREN_IN = r"\(\"?\w+_ ?\"?\)"
t_BOOL = "bool"
t_NUMBER = r'\d+'
def t_VARIABLE(t):
    r".+"
    
def t_error(t):
    global ERROR
    rich.print(f"[bold red]Illegal character {t.value[0]!r} on line {t.lexer.lineno}[/bold red]")
    t.lexer.skip(1)
    ERROR = True

t_ignore = '\n'

lexer = lex.lex()

def p_start(t):
    """
    start : bool
          | divide
          | vars
          | say
          | multiply
          | if
    """
    return

def p_bool(t):
    """
    bool : BOOL PAREN_IN
         | BOOL SPACE PAREN_IN
    """
    entry = 2
    if " " in t:
        print("SPACE!")
        entry = 3
    t[entry] = t[entry].strip('"')
    t[entry] = t[entry].strip('?')

    if t[entry] == "true" or t[entry] == "1":
        return True
    elif t[entry] == "false" or t[entry] == "0":
        return False
    rich.print(f"")


def p_divide(t):
    """
    divide : DIVIDE
    """
    try:
        tmp = t[1].split("/")
        for x, i in enumerate(tmp):
            tmp[x] = float(i)
        t.value = tmp[0] / tmp[1]
        print(tmp[0] / tmp[1])
        return t.value
    except ValueError:
        rich.print("[bold red]Multiplying a non number[/bold red]\n[bold blue]Error Ignored, this may cause your program to malfunction, please fix[/bold blue]")


def p_vars_set(t):
    """
    vars : EQUAL
    """
    name = ""
    value = ""
    stripped = str(t[1]).split("=")
    name = stripped[0]
    value = stripped[1]
    variables[name] = value


def p_vars(t):
    """
    vars : VARIABLE
    """
    tmp = t[1]
    for i in t: 
        print(i)
    t.value = variables[str(tmp)]
    return t.value


def p_multiply(t):
    """
    multiply : MULTIPLY
    """
    try:
        tmp = str(t).split("*")
        for i in tmp:
            int(i)
        #t.value = NUM
        return t.value
    except ValueError:
        try:
            if "true" in t:
                print("1")
            if "false" in t:
                print("2")
            else:
                print("0")
        except:
            pass


def p_say_onlyText(t):
    """
    say : SAY QUOTE QTEXT QUOTE
        | SAY SPACE QTEXT 
    """
    l = len(t)
    start = False
    for i in (t):
        if str(i).startswith('"'):
            to_print = str(i).strip('"')
            print(to_print)

def p_say_onlyVar(t):
    """
    say : SAY SPACE VARIABLE 
    """
    for i in t:
        print(i)
    try:
        print(variables[t[3].strip()])
    except KeyError:
        ERROR = True
        rich.print("UNKOWN OBJECT")
        code1()
        
def p_if_start(t):
    """
    if : IF '='
    """
    for i in t:
        print(i)
 
def p_error(t):
    global ERROR
    ERROR = True
    if t is None:  # lexer error
        return
    print(f"Syntax Error: {t.value!r}")

parser = yacc.yacc(debug=False, write_tables=False)

def code1():
    rich.print("[bold red]Errors![/bold red]")
    rich.print("[bold blue]Program exited with code 1[/bold blue]")
    


if __name__ == "__main__":
    rich.print("[yellow]Hello From The Alter Community[/yellow]")
    try:
        with open(sys.argv[1], "r") as file:
            lines = file.readlines()
            for i in lines:
                print(parser.parse(i))
    except IndexError:
        rich.print("[bold red]No File Specifed[/bold red]")
        rich.print("[bold blue]Program exited with code 5[/bold blue]")
        exit(5)
    except FileNotFoundError:
        rich.print("[bold red]File Not Found[/bold red]")
        rich.print("[bold blue]Program exited with code 5[/bold blue]")
        exit(5)
    if ERROR == True:
        code1()
    else:
        rich.print("[bold green]No Errors![/bold green]")
        rich.print("[bold blue]Program exited with code 0[/bold blue]")
