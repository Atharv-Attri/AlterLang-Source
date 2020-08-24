from os import write
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
    'if': "IF",
    'while' : "WHILE"
}

tokens = [
    'Divide',
    'NUMBER',
    'MULTIPLY',
    'QUOTE',
    'SPACE',
    'EQUAL',
    'QTEXT',
    'VARIABLE',
    'DIVIDE',
    'NUMBER',
    "LEQUAL",
    "LGT",
    "LLT",
    "STARTMARK",
    "ENDMARK"
] + list(reserved.values())

meta = {

}
 
variables = {

}

order = []

t_STARTMARK = "->"
t_ENDMARK = "<-"
t_LLT = "<"
t_LGT = ">"
t_LEQUAL = "="
t_NUMBER = r'[0-9]+'
t_DIVIDE = r"[A-Za-z0-9]+/[A-Za-z0-9]+"
t_MULTIPLY = r"\w_ ?\*\w_ ?"
t_SAY = "say"
t_IF = "if"
t_QUOTE = r"\"" 
t_SPACE = r"\s"
t_QTEXT = r"\".+_ ?\""
t_EQUAL = r".+\=.+"

def t_VARIABLE(t):
    r"\.\w+"
    print(variables)
    if t.value in variables:
        return
    else:
        print("SYMBOL NOT")

def t_error(t):
    global ERROR
    rich.print(f"[bold red]Illegal character {t.value[0]!r} on line {t.lexer.lineno}[/bold red]")
    t.lexer.skip(1)
    ERROR = True


t_ignore = "\n\t"

lexer = lex.lex()

def p_start(t):
    """
    start : vars
          | multiply
          | say
          | divide
          | if
          | endmark
    """
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
    name = "."
    value = ""
    stripped = str(t[1]).split("=")
    name = name + stripped[0]
    value = stripped[1]
    variables[name] = value

def p_vars_get(t):
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
    say : SAY QTEXT
        | SAY SPACE QTEXT
    """
    if meta["ifS"] == True and meta["lC"] == False:
        pass
    else:
        l = len(t)
        start = False
        for i in (t):
            if str(i).startswith('"'):
                to_print = str(i).strip('"')
                print(to_print)
    

def p_if_num(t):
    """
    if : IF SPACE NUMBER LEQUAL LEQUAL NUMBER SPACE STARTMARK
       | IF SPACE NUMBER LGT NUMBER SPACE STARTMARK
       | IF SPACE NUMBER LLT NUMBER SPACE STARTMARK
       | IF SPACE NUMBER LLT LEQUAL NUMBER SPACE STARTMARK
       | IF SPACE NUMBER LGT LEQUAL NUMBER SPACE STARTMARK
    """
    if len(t) == 9:
        if t[4] == "=":
            if int(t[3]) == int(t[6]):
                meta["ifS"] = True
                meta["lC"] = True
                order.append("if")
            else:
                meta["ifS"] = True
                meta["lC"] = False
                order.append("if")

        elif t[4] == ">":
            if int(t[3]) >= int(t[6]):
                meta["ifS"] = True
                meta["lC"] = True
                order.append("if")

            else:
                meta["ifS"] = True
                meta["lC"] = False
                order.append("if")

        elif t[4] == "<":
            if int(t[3]) <= int(t[6]):
                meta["ifS"] = True
                meta["lC"] = True
                order.append("if")

            else:
                meta["ifS"] = True
                meta["lC"] = False
                order.append("if")

    if len(t) == 8:
        if t[4] == ">":
            if int(t[3]) > int(t[5]):
                meta["ifS"] = True
                meta["lC"] = True
                order.append("if")

            else:
                meta["ifS"] = True
                meta["lC"] = False
                order.append("if")

        elif t[4] == "<":
            if int(t[3]) < int(t[5]):
                meta["ifS"] = True
                meta["lC"] = True
                order.append("if")

            else:
                meta["ifS"] = True
                meta["lC"] = False

def p_if_var_r(t):
    """ 
    if : IF SPACE NUMBER LGT VARIABLE SPACE STARTMARK
       | IF SPACE NUMBER LLT VARIABLE SPACE STARTMARK
       | IF SPACE NUMBER LEQUAL VARIABLE SPACE STARTMARK
       | IF SPACE NUMBER LLT LEQUAL VARIABLE SPACE STARTMARK
       | IF SPACE NUMBER LGT LEQUAL VARIABLE SPACE STARTMARK
    """
    print(len(t))
    if len(t) == 9:
        if t[4] == "=":
            if int(t[3]) == int(variables(t[6])):
                meta["ifS"] = True
                meta["lC"] = True
                order.append("if")
            else:
                meta["ifS"] = True
                meta["lC"] = False
                order.append("if")
        elif t[4] == ">":
            if int(t[3]) >= int(variables(t[6])):
                meta["ifS"] = True
                meta["lC"] = True
                order.append("if")
            else:
                meta["ifS"] = True
                meta["lC"] = False
                order.append("if")
        elif t[4] == "<":
            if int(t[3]) <= int(variables(t[6])):
                meta["ifS"] = True
                meta["lC"] = True
                order.append("if")
            else:
                meta["ifS"] = True
                meta["lC"] = False
                order.append("if")
    if len(t) == 8:
        if t[4] == ">":
            if int(t[3]) > int(variables(t[5])):
                meta["ifS"] = True
                meta["lC"] = True
                order.append("if")
            else:
                meta["ifS"] = True
                meta["lC"] = False
                order.append("if")
        elif t[4] == "<":
            if int(t[3]) < int(variable(t[5])):
                meta["ifS"] = True
                meta["lC"] = True
                order.append("if")
            else:
                meta["ifS"] = True
            meta["lC"] = False
            order.append("if")
    print(meta)


def p_endmark(t):
    """
    endmark : ENDMARK
    """
    if order[-1] == "if":
        meta["ifS"] = False
        meta["lC"] = False
        order.remove("if")


def p_error(t):
    global ERROR
    ERROR = True
    if t is None:  # lexer error
        return
    print(f"Syntax Error: {t.value!r}")


parser = yacc.yacc(write_tables=False)

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
    if ERROR == True:
        rich.print("[bold red]Errors![/bold red]")
        rich.print("[bold blue]Program exited with code 1[/bold blue]")
    else:
        rich.print("[bold green]No Errors![/bold green]")
        rich.print("[bold blue]Program exited with code 0[/bold blue]")
