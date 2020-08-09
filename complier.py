from ply import lex, yacc

# TODO: Variable, While loop, For loop, math
# !Due:    12   ,     14    ,    14   ,  12

# ?: Variable: regular syntax: a = 2, a = "say", a = true. ENG syntax: set a to 2
# ?: Math: regular syntax: 1+1 = 2, a += 1. ENG syntax: add 1 to a, add a to b
# TODO: ?: While loop: TODO
# TODO: ?: For Loop


tokens = [
    'SAY',
    'QUOTE',
    'SPACE',
    'TEXT'
]

t_SAY = "say"
t_QUOTE = r"\"" 
t_SPACE = r"\s"
t_TEXT = r"\".+_ ?\""

def t_error(t):
    print(f"Illegal character {t.value[0]!r} on line {t.lexer.lineno}")
    t.lexer.skip(1)

t_ignore = '\t'

lexer = lex.lex()

def p_say_onlyText(t):
    """
    say : SAY QUOTE TEXT QUOTE
        | SAY SPACE TEXT 
    """
    l = len(t)
    start = False
    for x, i in enumerate(t):
        if str(i).startswith('"'):
            to_print = str(i).rstrip('"')
            to_print = to_print.lstrip('"')
            print(to_print)



def p_error(t):
    if t is None:  # lexer error
        return
    print(f"Syntax Error: {t.value!r}")


parser = yacc.yacc(debug=False, write_tables=False)

if __name__ == "__main__":
    with open("test.kinos", "r") as file:
        raw = file.readlines()
        for i in raw:
            parser.parse(i)
