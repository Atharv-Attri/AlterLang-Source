import sys
import re
import rich

try:
    from . import util, usemodel, extractvar, transpiler

except ImportError:
    import util
    import usemodel
    import extractvar
    import transpiler

from textblob import TextBlob


model = usemodel.load()
current_line = 0
variables = {}
order = []
tabnum = None
count_tabs = False
transpile = False
# ! clean up code, maintainablity is like D- or something
# TODO: Make tests
# ? add type purification
# ? think about using layer levels
# ? reduce code reuse


def top_level(line: str, stripped=False):
    """
    Choses what to send the line to
    """
    global count_tabs, tabnum, order, model, transpile, variables
    tabnum = len(order)
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
    if line.startswith("#"):
        return "#ignore"
    elif list(line) == []:
        return None
    if line.startswith("dump"):
        dump()
    elif line.startswith("say"):
        return say(line)
    elif line.startswith("if"):
        if_statement(line)
    elif line.startswith("elif"):
        return elseif_statement(line)
    elif line.startswith("else"):
        return else_statement(line)
    elif line.startswith("while"):
        while_loop(line)
    elif line.startswith("<-"):
        end_arrow()
    elif line.startswith("\t") or line.startswith("    "):
        return tab_dealer(line)
    elif util.var_math_check(line) is True:
        return var_math(line)
    elif re.match(r"\w+ ?= ?.+", line) or blob.classify() == "pos":
        return set_variable(line)


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


def say(line: str) -> str:
    """
    Parameters:
        :param line: string of line that needs to be processed
    Return:
        str - text that was printed
    """
    global transpile, tabnum
    listed = list(line)
    out = ""
    start = None
    quotes = ["'", '"']
    quote_used = ""
    if len(util.groups(line, '"', "+")) > 1:
        groups = util.groups(line, '"', "+")
        out = ""
        for i in groups:
            i = i.strip(" ")
            if i.startswith("say"):
                i = i.lstrip('say "')
                i = i.rstrip('"')
                print(i, end="")
                out += str(i)
            elif i.startswith('"'):
                i = i.strip('"')
                print(i, end="")
                out += str(i)
            else:
                try:
                    print(variables[i], end="")
                    out += str(variables[i])
                except KeyError:
                    raise Exception("Variable not found")
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
                print(line)
                transpiler.add_line("    "*tabnum + transpiler.fill_print_plain_var(line))
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


def set_variable(line: str) -> str:
    """
    Parameters:
        :param line: string
    Return:
        string - variable
    """
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


def tab_dealer(line):
    global transpile, tabnum
    if transpile:
        tabnum = util.count("    ", line)
        line = line.lstrip("    ")
        return top_level(line)


def if_statement(line):
    global order, transpile, variables, tabnum
    line = util.sanitize(line)
    new_order = ["if"]
    order.append(new_order)
    if not transpile:
        transpiler.starter(variables)
        transpile = True
    transpiler.add_line(
        "    " * tabnum
        + transpiler.fill_if(re.findall(r"if ?(.+ ?[=<>=andor%=]+ ?.+) ?->", line)[0])
    )
    tabnum = len(order)


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
            re.findall(r"elif ?(.+ ?[=<andor>=%=]+ ?.+) ?->", line)[0]
        )
    )
    tabnum = len(order)


def else_statement(line):
    global order, transpile, variables, tabnum
    line = util.sanitize(line)
    new_order = ["else"]
    order.append(new_order)
    if not transpile:
        transpiler.starter(variables)
        transpile = True
    transpiler.add_line(
        "    " * tabnum
        + transpiler.fill_else()
    )
    tabnum = len(order)


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


def while_loop(line):
    global order, transpile, variables, tabnum
    line = util.sanitize(line)
    new_order = ["while"]
    order.append(new_order)
    if not transpile:
        transpiler.starter(variables)
        transpile = True
    transpiler.add_line(
        "    " * tabnum
        + transpiler.fill_while(re.findall(r"while ?(.+ ?[=%<andor>==]+ ?.+) ?->", line)[0])
    )
    tabnum = len(order)


def dump(line="Content not passed") -> None:
    print(
        "==================DUMP=======================",
        "Variables: " + str(variables),
        "Line: " + str(current_line),
        "Order: " + str(order),
        "Content: " + line,
        "==================DUMP=======================",
        sep="\n",
    )


def synonyms(line) -> str:
    if line.startswith("print"):
        return "say" + line.lstrip("print")
    re.sub(r"^\botherwise\b|\belse ?if\b", "elif", line)
    return line


def main(filename):
    global current_line
    # print the intro
    rich.print("[yellow]Hello From The Alter Community[/yellow]")
    if str(filename).endswith(".altr") is False:
        raise Exception("File must end with .altr")
    # load file and scan for errors, print out a custom message if were errs
    lines = []
    with open(filename, "r") as file:
        raw = file.read().split("\n")
        for i in raw:
            lines.append(i)
    out = []
    for i in lines:
        current_line += 1
        line_out = top_level(i)
        if line_out is not None and "ignore" not in str(line_out):
            out.append(line_out)
    print(lines, variables, order, sep="\n")
    rich.print("[bold green]No Errors![/bold green]")
    rich.print("[bold blue]Program exited with code 0[/bold blue]")
    return out


if __name__ == "__main__":
    if len(sys.argv) == 1:
        sys.argv.append("test.altr")
    main(sys.argv[1])
