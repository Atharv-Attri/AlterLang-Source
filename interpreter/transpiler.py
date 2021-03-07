import re
from random import randint
import os
import subprocess
import rich

progout = None
fname = None


def templates(type: str) -> str:
    template_bank = {
        "var": "{name} = {value}\n",
        "print_plain": "print('!>>'+ '{text}' + '<<;')\n",
        "print_text+var": """print('!>>' """,
        "print_plain_var": "print('!>>'+ str({var}) + '<<;')\n",
        "input": "{name} = input({prompt})\n",
        "if": "if {condition}:\n",
        "elseif": "elif {condition}: \n",
        "else": "else: \n",
        "while": "while {condition}:\n",
    }
    return template_bank[type]


def fill_var(name: str, value: str) -> str:
    template = templates("var")
    line = fill(template, "name", name)
    line = fill(line, "value", value)
    return line


def fill_print_plain(text) -> str:
    template = templates("print_plain")
    line = fill(template, "text", text)
    return line


def fill_print_text_var(args: list) -> str:
    line = templates("print_text+var")
    print(args)
    for i in args:
        if i[1] == 1:
            line = line + ' + "' + i[0] + '"'
        else:
            line = line + " + str(" + i[0] + ")"

    line = line + "+ '<<;')\n"
    return line


def fill_print_plain_var(var: str) -> str:
    template = templates("print_plain_var")
    line = fill(template, "var", var)
    return line


def fill_input(name, prompt: str) -> str:
    template = templates("input")
    line = fill(template, "name", name)
    line = fill(line, "prompt", prompt)
    return line


def fill_while(cond: str) -> str:
    template = templates("while")
    line = fill(template, "condition", cond)
    return line


def fill_if(cond: str) -> str:
    template = templates("if")
    line = fill(template, "condition", cond)
    return line


def fill_elseif(cond: str) -> str:
    template = templates("elseif")
    line = fill(template, "condition", cond)
    return line


def fill_else() -> str:
    template = templates("else")
    return template


def fill(text, holder, value) -> str:
    holder = "{" + holder + "}"
    return text.replace(holder, str(value))


def transfer_var(varlist: dict):
    names = varlist.keys()
    lines = []
    for name in names:
        lines.append(fill_var(name, varlist[name]))
    line = "\n".join(lines)
    return line


def transfer_var_returner() -> str:
    line = '_varlist = globals().copy()\nfor _i in _varlist.keys():\n\tif _i.startswith("_"):\n\t\tcontinue\n\tprint(f"__TRANSPILER.VAR.OUT__--N:{_i}--V:{_varlist[_i]};")'
    return line


def get_stdout() -> None:
    global progout
    line = progout
    todel = re.findall(r"!>>(.+?)<<;", line)
    line = "\n".join(todel)
    return line


def get_var() -> list:
    global progout
    if progout is None:
        raise Exception("No STDOUT set yet")
    varlist = re.findall(r"__TRANSPILER\.VAR\.OUT__--N:(.+?)--V:(.+?);", progout)
    return varlist


def file_maker() -> bool:
    global fname
    try:
        fname = str(randint(0, 999999)).zfill(6)
        while os.path.exists(f"./{fname}.py"):
            fname = str(randint(0, 999999)).zfill(6)
        with open(f"{fname}.py", "w") as f:
            f.write("")
        return True
    except:
        return False


def writer(text: str) -> bool:
    global fname
    try:
        with open(f"./{fname}.py", "a") as f:
            f.write(text)
        return True
    except:
        return False


def verify(tover) -> None:
    if tover is False:
        raise Exception("Whoops! Something went wrong!")


def starter(varlist) -> True:
    verify(file_maker())
    to_write = transfer_var(varlist)
    verify(writer(to_write))
    return True


def ender() -> True:
    to_write = transfer_var_returner()
    verify(writer(to_write))
    return True


def add_line(line: str) -> True:
    verify(writer(line))
    return True


def make_varlist(tupvarlist: list) -> dict:
    varlist = {}
    for i in tupvarlist:
        varlist[i[0]] = i[1]
    return varlist


def run() -> list:
    global fname, progout
    ender()
    args = ["python", f"{fname}.py"]
    process = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = process.communicate()
    out, err = str(out), str(err)
    if err != "b''":
        rich.print("[bold red]ERROR: " + err)
    progout = out.lstrip("b'").rstrip("'")
    os.remove(f"./{fname}.py")
    toret = []
    vars = get_var()
    vars = make_varlist(vars)
    toret.append(vars)
    toret.append(get_stdout())
    return toret


# print(fill_var("x","5"))
# print(fill_print_plain('''"hello"'''))
# print(fill_print_plain_var('''"hi"''',"x"))
# print(fill_input("num",'''"what's a number"'''))
# print(transfer_var({"x": 5, "y": 24, "no": "hi"}))
# print(fill_while('''i < 5'''))
# print(fill_if('''alt == "bad"'''))
# print(get_var())
# print(get_stdout())
