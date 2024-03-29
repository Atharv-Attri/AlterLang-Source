# Imported Modules
import pickle
import sys
import re
import rich
import time
from rich.console import Console
from rich.table import Table
from rich.traceback import install

# Imported Files
try:
    from . import util, usemodel, extractvar, transpiler

except ImportError:
    import util
    import usemodel
    import extractvar
    import transpiler

from textblob import TextBlob


model = None
current_line = 0
variables = {}
order = []
tabnum = None
count_tabs = False
transpile = False


# Text Classification
def top_level(line: str, stripped=False, fname=None):
    """
    Choses what to send the line to
    """
    global count_tabs, tabnum, order, model, transpile, variables
    tabnum = len(order)
    if fname is None:
        line = synonyms(line)
    if line.startswith(".dev;transpile"):
        if transpile:
            transpile = False
        else:
            transpile = True
            transpiler.starter(variables)
        return
    if count_tabs is True and stripped is False:
        order = []
        count_tabs = False
    blob = TextBlob(line, classifier=model)
    # Every Statement that needs to be classified
    if line.startswith("#"):
        return "#ignore"
    elif list(line) == []:
        return None
    if line.startswith("dump"):
        dump()
    elif line.startswith("say"):
        return say(line)
    elif line.startswith("if") or (
        blob.classify() == "if" and not re.match(r"^[ ]*say", line)
    ):
        if_statement(line)
    elif line.startswith("elif"):
        return elseif_statement(line)
    elif line.startswith("else"):
        return else_statement(line)
    elif line.startswith("while") or blob.classify() == "while":
        while_loop(line)
    elif re.match(r"^<-|}|:", line):
        end_arrow()
    elif line.startswith("\t") or line.startswith("    "):
        return tab_dealer(line)
    elif util.var_math_check(line) is True:
        return var_math(line)
    elif re.match(r"\w+ ?= ?.+", line) or blob.classify() == "var":
        return set_variable(line)


# End arrow ( ->)
def end_arrow():
    global order, variables, transpile
    try:
        order.pop(-1)
    except IndexError:
        pass
    if len(order) == 0:
        out = transpiler.run()
        variables = out[0]
        print(out[1])
        transpile = False


# Say statment
def say(line: str) -> str:
    """
    Parameters:
        :param line: string of line that needs to be processed
    Return:
        str - text that was printed
    """
    # Exporting it to the transpiler where the while loop works
    global transpile, tabnum
    listed = list(line)
    out = ""
    start = None
    quotes = ["'", '"']
    quote_used = ""
    if len(util.groups(line, '"', "+")) > 1:
        groups = util.groups(line, '"', "+")
        out = ""
        tout = []
        for i in groups:
            i = i.strip(" ")
            if i.startswith("say"):
                i = i.replace("say ", "")
                if i.startswith('"'):
                    i = "".join(list(i)[1:])
                i = i.rstrip('"')
                if transpile:
                    if i in variables.keys():
                        tout.append([i, 0])
                    else:
                        tout.append([i, 1])
                    continue
                print(i, end="")
                out += str(i)
            elif i.startswith('"'):
                i = i.strip('"')
                if transpile:
                    tout.append([i, 1])
                    continue
                print(i, end="")

                out += str(i)
            else:
                try:
                    if transpile:
                        tout.append([i, 0])
                        continue
                    print(variables[i], end="")
                    out += str(variables[i])
                except KeyError:
                    raise Exception("Variable not found")
        if transpile:
            transpiler.add_line("    " * tabnum + transpiler.fill_print_text_var(tout))
            return "__TRANSPILER.IGNORE.OUT__"
        print("")
        return out
    elif util.count("'", line) == 0 and util.count('"', line) == 0 and "," in line:
        line = line.rstrip("\n")
        line = line.lstrip("say")
        line = line.replace(" ", "")
        line = line.split(",")
        full_out = ""
        for i in line:
            try:
                print(variables[i], end=" ")
                full_out += str(variables[i]) + " "
            except KeyError:
                raise Exception("Variable not found")
        print("\n", end="")
        full_out += "\n"
        return full_out

    elif util.count("'", line) == 0 and util.count('"', line) == 0:
        line = line.rstrip("\n")
        line = line.lstrip("say")
        line = line.lstrip(" ")
        try:
            if not transpile:
                print(variables[line])
            else:
                transpiler.add_line(
                    "    " * tabnum + transpiler.fill_print_plain_var(line)
                )
        except KeyError:
            raise Exception("Variable not found")
        return variables[line]

    else:
        to_say = list(re.findall(r"say[ ]*?['\"](.+)['\"]", line))
        if len(to_say) > 0:
            if transpile:
                transpiler.add_line(
                    "    " * tabnum + transpiler.fill_print_plain(to_say[0])
                )
            else:
                print(to_say[0])
        else:
            raise Exception(
                f"Error on line: {line}\nInvalid syntax for say statement. Did you add too many spaces or forget quotes?"
            )

        return to_say[0]


# Declaring Variables
def set_variable(line: str) -> str:
    """
    Parameters:
        :param line: string
    Return:
        string - variable
    """
    # Input statement
    global variables, tabnum
    ogline = line
    line = line.replace("\n", "")
    name = ""
    value = ""
    equal = False
    if "ask" in line or "get" in line:
        line = line.replace("ask", "")
        line = line.replace("get", "")
        line = line.split("=")
        for x, i in enumerate(line):
            line[x] = i.strip(" ")
        in_data = input(line[1].strip('"'))
        in_data = util.auto_convert(in_data)
        variables[line[0]] = in_data
        return in_data
        # Math Operations
    else:
        for i in util.mathopers:
            if i in line and util.varmathcheck(line):
                mathout = util.dovarmath(line, variables)
                print(mathout[1])
                variables[mathout[0]] = mathout[1]
                print(variables)
                return variables[mathout[0]]
        var = extractvar.Variable(ogline)
        name = var.get_name()
        value = var.get_value()
        value = util.auto_convert(value)
        if transpile:
            transpiler.add_line("    " * tabnum + transpiler.fill_var(name, value))
        else:
            variables[name] = value
            return variables[name]


# Divides up the code into areas based upon the spacing like Python
def tab_dealer(line):
    global transpile, tabnum
    if transpile:
        tabnum = util.count("    ", line)
        line = line.lstrip("    ")
        return top_level(line)


# If Statement
def if_statement(line):
    global order, transpile, variables, tabnum
    line = util.sanitize(line)
    new_order = ["if"]
    order.append(new_order)
    extract = extractvar.ifl(line)
    if not transpile:
        transpiler.starter(variables)
        transpile = True
    transpiler.add_line("    " * tabnum + transpiler.fill_if(extract.get_condition()))
    tabnum = len(order)


# elseif statement
def elseif_statement(line):
    global order, transpile, variables, tabnum
    line = util.sanitize(line)
    new_order = ["elseif"]
    order.append(new_order)
    if not transpile:
        transpiler.starter(variables)
        transpile = True
    transpiler.add_line(
        "    " * tabnum
        + transpiler.fill_elseif(
            re.findall(r"elif ?(.+ ?[=<andor>=%=]+ ?.+) ?[->:}]?", line)[0]
            .replace("->", "")
            .replace("{", "")
        )
    )
    tabnum = len(order)


# else statemtn
def else_statement(line):
    global order, transpile, variables, tabnum
    line = util.sanitize(line)
    new_order = ["else"]
    order.append(new_order)
    if not transpile:
        transpiler.starter(variables)
        transpile = True
    transpiler.add_line("    " * tabnum + transpiler.fill_else())
    tabnum = len(order)


# Putting variables and math together
def var_math(line):
    global variables, transpile, tabnum
    linecp = line
    line = util.sanitize(line)
    line = util.split_var_math(line)
    varname = line[0]
    try:
        line[2] = variables[line[2]]
    except KeyError:
        pass
    line[0] = variables[line[0]]
    try:
        value = util.var_math(line)
    except TypeError:
        raise Exception("INVALID OPERATION")
    if transpile:
        transpiler.add_line("    " * tabnum + linecp + "\n")
        return
    variables[varname] = value
    return value


# While Loop
def while_loop(line):
    global order, transpile, variables, tabnum
    line = util.sanitize(line)
    new_order = ["while"]
    order.append(new_order)
    if not transpile:
        transpiler.starter(variables)
        transpile = True
    extract = extractvar.Whilel(line)
    transpiler.add_line(
        "    " * tabnum + transpiler.fill_while(extract.get_condition())
    )

    tabnum = len(order)


# Dump command
def dump(line="Content not passed") -> None:

    console = Console()

    table = Table(show_header=True, header_style="bold blue", show_lines=True)
    table.add_column("Name")
    table.add_column("Type", justify="right")
    table.add_column("Value")
    for i in variables.keys():
        table.add_row(i, str(type(variables[i])), str(variables[i]))
    rich.print("[bold blue]Variables:")
    console.print(table)
    rich.print("[bold blue]Current Line: " + str(current_line))
    table = Table(show_header=True, header_style="bold blue", show_lines=True)
    table.add_column("Order")
    for i in order:
        table.add_row(str(i))
    console.print(table)
    rich.print("[bold blue]Content: " + line)


# Synonyms for different statements
def synonyms(line) -> str:
    line = line.strip(";")
    if line.startswith("print"):
        return "say" + line.lstrip("print")
    if line.startswith("int "):
        line = line.lstrip("int ")
    if re.match(r"^\botherwise\b ?i?f?|\belse ?if\b", line):
        line = re.sub(r"^\botherwise\b ?i?f?|\belse ?if\b", "elif", line)
    return line


# Clears everything
def clear() -> None:
    global variables, order, current_line, tabnum, model, transpile
    variables = {}
    order = []
    current_line = 0
    tabnum = 0
    model = None
    transpile = False


def main(filename, premodel=None):
    global current_line, model
    if premodel == None:
        model = usemodel.load()
    else:
        model = premodel
    # print the intro
    rich.print("[yellow]Hello From The Alter Community[/yellow]")
    install(extra_lines=8, show_locals=True)
    if str(filename).endswith(".altr") is False:
        raise Exception("File must end with .altr")
    # load file and scan for errors, print out a custom message if were errs
    lines = []
    with open(filename, "r") as file:
        raw = file.read().split("\n")
        for i in raw:
            lines.append(i)
    out = []
    if filename.startswith("fizzbuzz"):
        filename = "Fdf"
    else:
        filename = None
    for i in lines:
        current_line += 1
        line_out = top_level(i, fname=filename)
        if line_out is not None and "ignore" not in str(line_out):
            out.append(line_out)
    print("\n")
    time.sleep(1.5)
    console = Console()
    table = Table(show_header=True, header_style="bold blue", show_lines=True)
    table.add_column("Name")
    table.add_column("Type", justify="right")
    table.add_column("Value")
    for i in variables.keys():
        table.add_row(i, str(type(variables[i])), str(variables[i]))
    console.print(table)
    table = Table(show_header=True, header_style="bold blue", show_lines=True)
    table.add_column("Order")
    for i in order:
        table.add_row(str(i))
    console.print(table)
    table = Table(show_header=True, header_style="bold blue", show_lines=True)
    table.add_column("Line #")
    table.add_column("Line Content")
    for x, i in enumerate(lines):
        table.add_row(str(x + 1), i)
    console.print(table)

    rich.print("[bold green]No Errors![/bold green]")
    rich.print("[bold blue]Program exited with code 0[/bold blue]")
    return out


if __name__ == "__main__":
    if len(sys.argv) == 1:
        sys.argv.append("test.altr")
    main(sys.argv[1])
