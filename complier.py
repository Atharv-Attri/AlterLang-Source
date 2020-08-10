import sys
from ply import lex, yacc
import rich

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
    'QUOTE',
    'SPACE',
    'TEXT',
    'EQUAL',
    'QTEXT',
    'TEXT',
    'ADD',
    'NUMBER'
] + list(reserved.values())

meta = [

]
 
variables = [

]
t_ADD = r"\+"
t_NUMBER = r"\d+"
t_SAY = "say"
t_QUOTE = r"\"" 
t_SPACE = r"\s"
t_QTEXT = r"\".+_ ?\""
t_EQUAL = "="
t_TEXT  = r"\w+"

def t_error(t):
    rich.print(f"[bold red]Illegal character {t.value[0]!r} on line {t.lexer.lineno}[/bold red]")
    t.lexer.skip(1)

t_ignore = '\n'

lexer = lex.lex()

def p_math_add(t):
    """
    math : NUMBER PLUS NUMBER
    """
    for i in t:
        print(i)

def p_say_onlyText(t):
    """
    say : SAY QUOTE QTEXT QUOTE
        | SAY SPACE QTEXT 
    """
    l = len(t)
    start = False
    for x, i in enumerate(t):
        if str(i).startswith('"'):
            to_print = str(i).strip('"')
            print(to_print)


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
