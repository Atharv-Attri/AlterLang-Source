from os import write
import sys
from ply import lex, yacc
import rich
import math

#keep track of if there were errors
ERROR = False
#declare reserved tokens
reserved = {
    'say': "SAY",
    'if': "IF",
    'while': "WHILE",
    'dump': "DUMP",
    'ask': "ASK"
}
# declate rest of the tokens
tokens = [
    'SUBTRACT',
    'ADD',
    'MULTIPLY',
    'SPACE',
    'EQUAL',
    'QTEXT',
    'VARIABLE',
    'DIVIDE',
    'NUMBER',
    "LEQUAL",
    "SLEQUAL",
    "LGT",
    "LLT",
    "SLGT",
    "SLLT",
    "STARTMARK",
    "ENDMARK",
    "ANYTHINGM"
] + list(reserved.values())
# meta keeps track of the program (if, while)
meta = {

}
# variables keeps track of the varibles
variables = {

}
# Defining the tokens
order = []
t_ASK = "ask"
t_DUMP = "dump"
t_SUBTRACT = "-"
t_ADD = r"\+"
t_STARTMARK = "->"
t_ENDMARK = "<-"
t_LLT = "<"
t_SLGT = "greater_than"
t_SLLT = "less_than"
t_SLEQUAL = "equal_to"
t_LGT = ">"
t_LEQUAL = "="
t_NUMBER = r'[0-9]+'
t_DIVIDE = r"[A-Za-z0-9]+/[A-Za-z0-9]+"
t_MULTIPLY = r"\w_ ?\*\w_ ?"
t_SAY = "say"
t_IF = "if"
t_WHILE = "while"
t_SPACE = " _{1}"
t_QTEXT = r"\".+_?\""
t_EQUAL = r".{1}=.+"
t_ANYTHINGM = r"[A-Za-z0-9]+"

def t_VARIABLE(t):
    r"\..{1}"
    if t.value in variables:
        return t
    else:
        print("SYMBOL NOT FOUND")
        ERROR = True

# Error function


def t_error(t):
    global ERROR
    rich.print(
        f"[bold red]Illegal character {t.value[0]!r} on line {t.lexer.lineno}[/bold red]")
    t.lexer.skip(1)
    ERROR = True


t_ignore = "\n"

lexer = lex.lex()


def p_start(t):
    """
    start : say
          | multiply
          | vars
          | divide
          | if
          | endmark
          | while
          | add
          | subtract
          | dump
          | ask
    """


def p_dump(t):
    """
    dump : DUMP
    """
    print(meta, variables, order)
# Addition


def p_add(t):
    """
    add : NUMBER ADD NUMBER
    """
    return t[1] + t[3]


def p_add_var(t):
    """
    add : VARIABLE ADD NUMBER
    """
    variables[t[1]] = str(int(variables[t[1]]) + int(t[3]))
    t.value = variables[t[1]] + t[3]
    return t
# Subtraction


def p_subtract(t):
  """
  subtract : NUMBER SUBTRACT NUMBER
  """
  return t[1] - t[3]


def p_subtract_var(t):
    """
    subtract : VARIABLE SUBTRACT NUMBER
    """
    return variables[t[1]] - t[3]
# Division


def p_divide(t):
    """
    divide : DIVIDE
    """
    try:
        tmp = t[1].split("/")
        for x, i in enumerate(tmp):
            tmp[x] = float(i)
        t.value = tmp[0] / tmp[1]
        return t.value
    except ValueError:
        rich.print("[bold red]Multiplying a non number[/bold red]\n[bold blue]Error Ignored, this may cause your program to malfunction, please fix[/bold blue]")


def p_vars_set(t):
    """
    vars : ANYTHINGM LEQUAL ANYTHINGM
    """
    print("KFSKHFKJSHFKJFHKJSH")
    for i in t:
        print(i)
    #name = "."
    #value=  ""
    #stripped = str(t[1]).split("=")
    #name = name + stripped[0]
    #value = stripped[1]
    #variables[name] = value


def p_vars_get(t):
    """
    vars : VARIABLE
    """
    tmp = t[1]
    for i in t:
        print(i)
    t.value = variables[str(tmp)]
    return t.value

# Input Statement


def p_ask(t):
    """
    ask : ASK SPACE QTEXT
    """
    value = t[3].strip('"')
    value = input(value)
    variables[".L"] = value
    t.value = value
    return t
# Multiplication


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

# Say/Print Statement


def p_say_onlyText(t):
    """
    say : SAY QTEXT
        | SAY SPACE QTEXT
    """
    for i in t:
        print(i)
    try:
        if meta["ifS"] == True and meta["lC"] == False:
            return
    except:
        pass
    try:
        if meta["WS"] == True and meta["WLC"] == True and meta["P"] == False:
            meta["WTD"].append(t[1] + t[2] + t[3])
            meta["P"] = True
    except KeyError:
        pass

    l = len(t)
    start = False
    for i in (t):
        if str(i).startswith('"'):
            to_print = str(i).strip('"')
            print(to_print)


def p_say_onlyvar(t):
    """
    say : SAY SPACE VARIABLE
    """
    print(variables[t[3]])

# If Statement


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
                meta["lC"] = True
            else:
                meta["lC"] = False
        elif t[4] == ">":
            if int(t[3]) >= int(t[6]):
                meta["lC"] = True
            else:
                meta["lC"] = False
        elif t[4] == "<":
            if int(t[3]) <= int(t[6]):
                meta["lC"] = True
            else:
                meta["lC"] = False

    if len(t) == 8:
        if t[4] == ">":
            if int(t[3]) > int(t[5]):
                meta["lC"] = True
            else:
                meta["lC"] = False
        elif t[4] == "<":
            if int(t[3]) < int(t[5]):
                meta["lC"] = True
            else:
                meta["lC"] = False
    order.append("if")
    meta["ifS"] = True


def p_if_var_r(t):
    """ 
    if : IF SPACE NUMBER LGT VARIABLE SPACE STARTMARK
       | IF SPACE NUMBER LLT VARIABLE SPACE STARTMARK
       | IF SPACE NUMBER LLT LEQUAL VARIABLE SPACE STARTMARK
       | IF SPACE NUMBER LGT LEQUAL VARIABLE SPACE STARTMARK
       | IF SPACE NUMBER LEQUAL VARIABLE SPACE STARTMARK
    """
    if len(t) == 9:
        if t[4] == "=":
            if int(t[3]) == int(variables(t[6])):
                meta["lC"] = True
            else:
                meta["lC"] = False
        elif t[4] == ">":
            if int(t[3]) >= int(variables(t[6])):
                meta["lC"] = True
            else:
                meta["lC"] = False
        elif t[4] == "<":
            if int(t[3]) <= int(variables(t[6])):
                meta["lC"] = True
            else:
                meta["lC"] = False
    if len(t) == 8:
        if t[4] == ">":
            if int(t[3]) > int(variables[t[5]]):
                meta["lC"] = True
            else:
                meta["lC"] = False
        elif t[4] == "<":
            if int(t[3]) < int(variables[t[5]]):
                meta["lC"] = True
            else:
                meta["lC"] = False
    order.append("if")
    meta["ifS"] = True


def p_if_num_eng(t):
    """
    if : IF SPACE NUMBER SPACE SLEQUAL SPACE SLEQUAL SPACE NUMBER SPACE STARTMARK
       | IF SPACE NUMBER SPACE SLGT SPACE NUMBER SPACE STARTMARK
       | IF SPACE NUMBER SPACE SLLT SPACE NUMBER SPACE STARTMARK
       | IF SPACE NUMBER SPACE SLLT SPACE SLEQUAL SPACE NUMBER SPACE STARTMARK
       | IF SPACE NUMBER SPACE SLGT SPACE SLEQUAL SPACE NUMBER SPACE STARTMARK
    """

    if len(t) == 12:
        if t[5] == "=" or t[5] == "equal_to":
            if int(t[3]) == int(t[9]):
                meta["lC"] = True
            else:
                meta["lC"] = False
        elif t[5] == ">" or t[5] == "greater_than":
            if int(t[3]) >= int(t[9]):
                meta["lC"] = True
            else:
                meta["lC"] = False
        elif t[5] == "<" or t[5] == "less_than":
            if int(t[3]) <= int(t[9]):
                meta["lC"] = True
            else:
                meta["lC"] = False
    if len(t) == 10:
        if t[5] == ">" or t[5] == "greater_than":
            if int(t[3]) > int(t[7]):
                meta["lC"] = True
            else:
                meta["lC"] = False
        elif t[5] == "<" or t[5] == "less_than":
            if int(t[3]) < int(t[7]):
                meta["lC"] = True
            else:
                meta["lC"] = False
    order.append("if")
    meta["ifS"] = True


def p_if_var_r_eng(t):
    """ 
    if : IF SPACE NUMBER SPACE SLGT SPACE VARIABLE SPACE STARTMARK
       | IF SPACE NUMBER SPACE SLLT SPACE VARIABLE SPACE STARTMARK
       | IF SPACE NUMBER SPACE SLEQUAL SPACE VARIABLE SPACE STARTMARK
       | IF SPACE NUMBER SPACE SLLT SPACE LEQUAL SPACE VARIABLE SPACE STARTMARK
       | IF SPACE NUMBER SPACE SLGT SPACE LEQUAL SPACE VARIABLE SPACE STARTMARK
    """
    a = 0

    if len(t) == 9:
        if t[4] == "=":
            if int(t[3]) == int(variables(t[6])):
                meta["lC"] = True
            else:
                meta["lC"] = "." + False
        elif t[4] == ">":
            if int(t[3]) >= int(variables(t[6])):
                meta["lC"] = True
            else:
                meta["lC"] = False
        elif t[4] == "<":
            if int(t[3]) <= int(variables(t[6])):
                meta["lC"] = True
            else:
                meta["lC"] = False
    elif len(t) == 10:

        if t[5] == "greater_than":
            if int(t[3]) > int(variables(t[7])):
                meta["lC"] = True
            else:
                meta["lC"] = False
        elif t[5] == "less_than":
            if int(t[3]) < int(variables[t[7]]):
                meta["lC"] = True
            else:
                meta["lC"] = False
    meta["ifS"] = True
    order.append("if")
# While Statement


def p_while(t):
    """
    while : WHILE SPACE VARIABLE LLT NUMBER SPACE STARTMARK
          | WHILE SPACE VARIABLE LGT NUMBER SPACE STARTMARK
    """
    order.append("while")
    meta["P"] = False
    meta["WTD"] = []
    meta["WS"] = True
    meta["WC"] = t[3] + t[4] + t[5]
    if t[4] == ">":
        if t[3] > t[5]:
            meta["WLC"] = True
        else:
            meta["WLC"] = False
    elif t[4] == "<":
        if t[3] < t[5]:
            meta["WLC"] = True
        else:
            meta["WLC"] = False

# End of If or While Statement


def p_endmark(t):
    """
    endmark : ENDMARK
    """
    try:
        if order[-1] == "if":
            meta["ifS"] = False
            meta["lC"] = False
            order.remove("if")
    except:
        pass
    try:
        if order[-1] == "while":
            if meta["WC"][2] == "<":
                a = True
                tmp = meta["WTD"]
                if variables["." + meta["WC"][1]] < meta["WC"][3]:
                    for i in tmp:
                        parser.parse(i)
                        tmp[-1] = None
                else:
                    meta["WTD"] = None
                    meta["WLC"] = False
                    a = False
    except:
        pass


# Error Statement


def p_error(t):
    global ERROR
    ERROR = True
    if t is None:  # lexer error
        return
    print(f"Syntax Error: {t.value!r} ")


parser = yacc.yacc(debug=False, write_tables=False)


if __name__ == "__main__":
    #print the intro
    rich.print("[yellow]Hello From The Alter Community[/yellow]")
    #load file and scan for errors, print out a custom message if there were errors
    try:
        with open(sys.argv[1], "r") as file:
            raw = file.readlines()
            for i in raw:
                parser.parse(i)
    #except IndexError:
    #    rich.print("[bold red]No File Specifed[/bold red]")
    #    rich.print("[bold blue]Program exited with code 5[/bold blue]")
    #    exit(5)
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

