import sys
import rich

try:
    from . import stringUtil, util
except ImportError:
    import stringUtil, util

current_line = 0
variables = {}

# ! clean up code, maintainablity is like D- or something
# TODO: Make tests
# ? add type purification
# ? think about using layer levels
# ? reduce code reuse
def top_level(line):
    if line.startswith("#"):
        return
    elif line.startswith("say"):
        return say(line)
    elif stringUtil.count("=", line) == 1 and stringUtil.position("=", line)[0] != 0:
        return set_variable(line)


def say(line):
    listed = list(line)
    out = ""
    start = None
    quotes = ["'", '"']
    quote_used = ""

    if len(stringUtil.groups(line, '"', "+")) > 1:
        groups = stringUtil.groups(line, '"', "+")
        out = ""
        for i in groups:
            i = i.strip(" ")
            if i.startswith('say'):
                i = i.lstrip('say "')
                i = i.rstrip('"')
                print(i, end = "")
                out += str(i)
            elif i.startswith('"'):
                i = i.strip('"')
                print(i, end = "")
                out += str(i)
            else:
                try: 
                    print(variables[i], end = "")
                    out += str(variables[i])
                except KeyError: raise Exception("Variable not found")
        print("")
        return out
    elif stringUtil.count("'", line) == 0 and stringUtil.count('"', line) == 0 and "," in line:
        line = line.rstrip("\n")
        line = line.lstrip("say")
        line = line.replace(" ", "")
        line = line.split(',')
        full_out = ""
        for i in line:
            try: 
                print(variables[i], end = " ")
                full_out += str(variables[i]) + " "
            except KeyError: raise Exception("Variable not found")
        print("\n", end = "")
        full_out += "\n"
        return full_out

    elif stringUtil.count("'", line) == 0 and stringUtil.count('"', line) == 0:
        line = line.rstrip("\n")
        line = line.lstrip("say")
        line = line.lstrip(" ")
        try: print(variables[line])
        except KeyError: raise Exception("Variable not found")
        return variables[line]

    #kavish's code goes here
    else:
        if listed[3] == " " and listed[4] in quotes:
            start = 5
            quote_used = listed[4]
        elif listed[3] in quotes:
            quote_used = listed[3]
            start = 4        
        if start == None:
            raise Exception(f"Error on line: {line}\nInvalid syntax for say statement. Did you add too many spaces or forget quotes?")
        for i in listed[start:]:
            if i in quote_used:
                break
            out += i
        print(out)
        return out


def set_variable(line):
    line = line.replace("\n", "")
    name = ""
    value = ""
    equal = False
    if "ask" in line or "get" in line:
        line = line.replace("ask", "")
        line = line.replace("get", "")
        line = line.split("=")
        for x,i in enumerate(line):
            line[x] = i.strip(" ")
        in_data = input(line[1].strip('"'))
        in_data = util.auto_convert(in_data)
        variables[line[0]] = in_data
        return in_data
    else:
        for i in line:
            if i == "=":
                equal = True
                continue
            if equal == False:
                name += i
            else:
                value += i
        name = name.strip(" ")
        value = value.lstrip((" "))
        value = util.convert(value,util.datatype(value))
        variables[name] = value
        return variables[name]

def main(filename):
    global current_line
    #print the intro
    rich.print("[yellow]Hello From The Alter Community[/yellow]")
    #load file and scan for errors, print out a custom message if there were errors
    lines = []
    with open(filename, "r") as file:
        raw = file.readlines()
        for i in raw:
            lines.append(i)
            current_line += 1
    out = []
    for i in lines:
        line_out = top_level(i)
        if line_out != None:
            out.append(line_out)
    print(lines, variables, sep="\n")
    rich.print("[bold green]No Errors![/bold green]")
    rich.print("[bold blue]Program exited with code 0[/bold blue]")
    return out

if __name__ == "__main__":
    main(sys.argv[1])
