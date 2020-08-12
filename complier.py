import sys
from ply import lex, yacc
import rich
import math
# TODO: Variable, While loop, For loop, math
# !Due:    12   ,     14    ,    14   ,  12

# ?: Variable: regular syntax: a = 2, a = "say", a = true. ENG syntax: set a to 2
# ?: Math: regular syntax: 1+1 = 2, a += 1. ENG syntax: add 1 to a, add a to b
# TODO: ?: While loop: TODO
# TODO: ?: For Loop

# TODO: add reserved
reserved = {
    'say' : "SAY",

}

tokens = [
    'Divide',
    'NUMBER',
    'MULTIPLY',
    'QUOTE',
    'SPACE',
    'EQUAL',
    'QTEXT',
] + list(reserved.values())

meta = [

]
 
variables = {

}

t_DIVIDE = r""
t_MULTIPLY = r"\w_ ?\*\w_ ?"
t_SAY = "say"
t_QUOTE = r"\"" 
t_SPACE = r"\s"
t_QTEXT = r"\".+_ ?\""
t_EQUAL = r"\w+_ ?=\w+_ ?"

def t_error(t):
    rich.print(f"[bold red]Illegal character {t.value[0]!r} on line {t.lexer.lineno}[/bold red]")
    t.lexer.skip(1)

t_ignore = '\n'

lexer = lex.lex()

def p_divide(t):
    """
    divide : DIVIDE
    """
    try:
        tmp = str(t).split("*")
        for i in tmp:
            int(i)
        t.value = NUM
        return t.value
    except ValueError:
        try:
            if "true" in t:
                print("1")
            if "false" in t:
                print("2")
            else:
                print("0")
        try: 
            if 
        except:
            pass

def p_multiply(t):
    """
    multiply : MULTIPLY
    """
    try:
        tmp = str(t).split("*")
        for i in tmp:
            int(i)
        t.value = NUM
        return t.value
    except ValueError:
        try:
            if "true" in t:
                print("1")
            if "false" in t:
                print("2")
            else:
                print("0")
        try: 
            if 
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

def p_error(t):
    if t is None:  # lexer error
        return
    print(f"Syntax Error: {t.value!r}")


parser = yacc.yacc()

if __name__ == "__main__":
    rich.print("[yellow]Hello From The NAME Community[/yellow]")
    try:
        with open(sys.argv[1], "r") as file:
            raw = file.readlines()
            for i in raw:
                parser.parse(i)
    except IndexError:
        rich.print("[bold red]No File Specifed[/bold red]")
        rich.print("[bold blue]Program exited with code 5[/bold blue]")
        exit(5)
    except FileNotFoundError:
        rich.print("[bold red]File Not Found[/bold red]")
        rich.print("[bold blue]Program exited with code 5[/bold blue]")
        exit(5)
    rich.print("[bold green]No Errors![/bold green]")
    rich.print("[bold blue]Program exited with code 0[/bold blue]")
