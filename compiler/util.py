comparables = ["==", "=>", "<=", ">=", "=<",  ">", "<", "True", "true", "False",
               "false"]


def datatype(item):
    if "'" in item or '"' in item:
        return "str"
    elif item.lower() in ["false", "true"]:
        return "bool"
    else:
        try:
            int(item)
            return "int"
        except ValueError:
            return None


def convert(item, type):
    if type == "str":
        if item[1] == "'":
            item = item.strip("'")
        else:
            item = item.strip('"')
        return str(item)
    elif type == "int":
        return int(item)
    elif type == "bool":
        if item.lower() == "false":
            return False
        elif item.lower() == "true":
            return True
        else:
            return None
    elif type == "list":
        return list(item)


def canConvert(item, type):
    if type == "list":    
        try:
            list(item)
            return True
        except ValueError:
            return False
    if type == "int":
        try:
            int(item)
            return True
        except ValueError:
            return False
    if type == "bool":    
        try:
            bool(item)
            return True
        except ValueError:
            return False


def auto_convert(item):
    if item.lower() == "true":
        return True
    elif item.lower() == "false":
        return False
    else:
        try:
            item = int(item)
            return item
        except ValueError:
            pass
        try:
            item = float(item)
            return item
        except ValueError:
            pass
    return item


def condition(conditional, varlist):
    # v = True/False
    # v [<,>,=,<=,>=]
    condition = get_condition(conditional, varlist)
    # print(condition)
    if condition[1] == "<":
        return condition[0] < condition[2]
    elif condition[1] == ">":
        return condition[0] > condition[2]
    elif condition[1] == "==":
        return condition[0] == condition[2]
    elif condition[1] == ">=":
        return condition[0] >= condition[2]
    elif condition[1] == "<=":
        return condition[0] <= condition[2]
    elif condition[1] == "=<":
        return condition[0] <= condition[2]
    elif condition[1] == "=>":
        return condition[0] >= condition[2]
    elif condition[1] in ["True", "true"]:
        return True
    elif condition[1] in ["False", "false"]:
        return False


def get_condition(text, varlist):
    global comparables
    if text.startswith("if"):
        text = text.lstrip("if")
        text = text.rstrip("->")
        text = text.replace(" ", "")
        comp = find_comprable(text)
        text = text.split(comp)
        for x, i in enumerate(text):
            try:
                i = varlist[i]
                text[x] = i
            except KeyError:
                pass
            text[x] = auto_convert(str(i))
        text.insert(1, comp)
        return text


def find_comprable(text: str) -> str:
    global comparables
    for i in comparables:
        if i in text:
            return str(i)
    return "Nah"


def sanitize(line: str):
    line = line.rstrip("\n")
    line = line.rstrip("\r")
    return line
