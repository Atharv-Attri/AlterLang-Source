import sys
import re
import rich

try:
    from . import util
except ImportError:
    import util

current_line = 0
variables = {}
order = []
tabnum = -1
count_tabs = False
# ! clean up code, maintainablity is like D- or something
# TODO: Make tests
# ? add type purification
# ? think about using layer levels
# ? reduce code reuse


def top_level(line: str, stripped=False):
    """
    Choses what to send the line to
    """
    global count_tabs, tabnum, order
    if count_tabs is True and stripped is False:
        order = []
        count_tabs = False
    # print(order)
    if line.startswith("#"):
        return "#ignore"
    if line.startswith("dump"):
        dump()
    elif line.startswith("say"):
        return say(line)
    elif line.startswith("if"):
        if_statement(line)
    elif line.startswith("while"):
        while_loop(line)
    elif line.startswith("<-"):
        end_arrow()
    elif line.startswith("\t") or line.startswith(" "):
        if order[-1][0] != "while":
            count_tabs = True
        tor = tab_dealer(line)
        return tor
    elif util.var_math_check(line) is True:
        return var_math(line)
    elif util.count("=", line) == 1 and util.position("=", line)[0] != 0:
        return set_variable(line)


def end_arrow():
    global order, variables
    index = -1
    current = order[index]
    while current[0] != "while":
        index -= 1
        current = order[index]
    tabs = str(current[1]).count("    ")
    while util.condition(current[1], variables) is not False:
        remove = 0
        for i in current[2]:
            i = str(i).lstrip("    ")
            # print(i)
            top_level(i)
            if i.startswith("if"):
                remove += 1
        for i in range(remove):
            order.pop(-1)
        count_tabs = True
        return tab_dealer(line)

def say(line: str) -> str:
    """
    Parameters:
        :param line: string of line that needs to be processed
    Return:
        str - text that was printed
    """
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
            print(variables[line])
        except KeyError:
            raise Exception("Variable not found")
        return variables[line]

    # kavish's code goes here
    else:
        to_say = list(re.findall(r"say[ ]*?['\"](.+)['\"]", line))
        if len(to_say) > 0:
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
    # The code for making variables
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
        for i in line:
            if i == "=":
                equal = True
                continue
            if equal is False:
                name += i
            else:
                value += i
        name = name.strip(" ")
        value = value.lstrip((" "))
        value = util.auto_convert(value)
        variables[name] = value
        return variables[name]
    
         

def tab_dealer(line):
    global order, tabnum, variables
    # print(order, line)
    try:
        current = order[line.count("    ") - 1]
    except IndexError:
        current = order[-1]
    if current[0] == "if":
        if current[1] is True:
            line = util.remove_tabs(line)
            return top_level(line, stripped=True)
    if current[0] == "while":
        try:
            order[line.count("    ") - 1][2].append(line)
        except IndexError:
            order[-1][2].append(line)


def if_statement(line):
    global variables, tabnum
    line = util.sanitize(line)
    condition = util.condition(line, variables)
    order.append(["if", condition])
    tabnum += 1


def var_math(line):
    global variables
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
    variables[varname] = value
    return value


def while_loop(line):
    global variables, order
    line = util.sanitize(line)
    new_order = ["while", line, []]
    order.append(new_order)
def dump(line="Content not passed") -> None:
    print("==================DUMP=======================","Variables: "+str(variables),"Line: "+str(current_line),"Order: "+str(order), "Content: "+line,"==================DUMP=======================",sep="\n")

def synonyms(line) -> str:
    if line.startswith("print"):
        return "say"+line.lstrip("print")
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
