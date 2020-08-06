from ply import lex, yacc

tokens = [
    'SAY',
    'QUOTE',
    'SPACE',
    'TEXT'
]

t_SAY = "say"
t_QUOTE = r"\""
t_SPACE = r"\s"

def t_TEXT(t):
    r"[A-Za-z0-9]"


def t_error(t):
    print(f"Illegal character {t.value[0]!r} on line {t.lexer.lineno}")
    t.lexer.skip(1)

t_ignore = '\t'

lexer = lex.lex()

def p_say(t):
    """
    say : SAY QUOTE TEXT QUOTE
        | SAY SPACE QUOTE QUOTE
    """
    print("SAID")


def p_error(t):
    if t is None:  # lexer error
        return
    print(f"Syntax Error: {t.value!r}")


parser = yacc.yacc()

if __name__ == "__main__":
    with open("test.kinos", "r") as file:
        raw = file.readlines()
        for i in raw:
            print(parser.parse(i))
