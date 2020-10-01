import sys
import rich

import stringHelp
import helper

current_line = 0
variables = {}

def top_level(line):
    if line.startswith("#"):
        return
    elif line.startswith("say"):
        say(line)
    elif stringHelp.count("=", line) == 1 and stringHelp.position("=", line)[0] != 0:
        set_variable(line)


def say(line):
    listed = list(line)
    out = ""
    start = None
    quotes = ["'", '"']
    quote_used = ""

    if stringHelp.count("'", line) == 0 and stringHelp.count('"', line) == 0 and "," in line:
        line = line.rstrip("\n")
        line = line.lstrip("say")
        line = line.replace(" ", "")
        line = line.split(',')
        for i in line:
            try: print(variables[i], end = " ")
            except KeyError: raise Exception("Variable not found")
        print("\n", end = "")
        return

    if stringHelp.count("'", line) == 0 and stringHelp.count('"', line) == 0:
        line = line.rstrip("\n")
        line = line.lstrip("say")
        line = line.lstrip(" ")
        try: print(variables[line])
        except KeyError: raise Exception("Variable not found")
        return

    #kavish's code goes here
    
    
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


def set_variable(line):
    line = line.replace("\n", "")
    name = ""
    value = ""
    equal = False
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
    value = helper.convert(value,helper.datatype(value))
    variables[name] = value

        

if __name__ == "__main__":
    #print the intro
    rich.print("[yellow]Hello From The Alter Community[/yellow]")
    #load file and scan for errors, print out a custom message if there were errors
    lines = []
    with open(sys.argv[1], "r") as file:
        raw = file.readlines()
        for i in raw:
            lines.append(i)
            current_line += 1
    for i in lines:
        top_level(i)
    print(lines, variables, sep="\n")
    rich.print("[bold green]No Errors![/bold green]")
    rich.print("[bold blue]Program exited with code 0[/bold blue]")
