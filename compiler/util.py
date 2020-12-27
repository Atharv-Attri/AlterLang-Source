comparables = ["==", "=>", "<=", ">=", "=<", ">", "<", "True", "true", "False", "false"]

variable_math_operators = ["+=", "-=", "=+", "=-", "/=", "=/", "*=", "=*"]


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
    item = item.strip("'")
    item = item.strip('"')
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
    elif text.startswith("while"):
        text = text.lstrip("while")
    text = text.rstrip("->")
    text = text.replace(" ", "")
    comp = find_comparable(text)
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


def find_comparable(text: str) -> str:
    global comparables
    for i in comparables:
        if i in text:
            return str(i)
    return "Nah"


def sanitize(line: str):
    line = line.rstrip("\n")
    line = line.rstrip("\r")
    return line


def var_math_check(line):
    for i in variable_math_operators:
        if i in line:
            return True


def split_var_math(line):
    operator = find_var_math_oper(line)
    line = line.split(operator)
    for x, i in enumerate(line):
        i = i.strip(" ")
        line[x] = auto_convert(i)
    line.insert(1, operator)
    return line


def count(item, group) -> int:
    count = 0
    for i in group:
        if i == item:
            count += 1
    return count


def position(item, group) -> list:
    positions = []
    for x, i in enumerate(group):
        if i == item:
            positions.append(x)
    return positions


def groups(text, grouper, seperator: str) -> str:
    """
    Parameters:
        :param text, grouper, seperator: strings
    Return:
        type - string
    """
    # Not too sure what it does
    started = False
    groups = []
    tmp = ""
    for i in text:
        if i == grouper:
            if started is False:
                started = True
            else:
                started = False
            tmp += i
        elif i == seperator and started is False:
            groups.append(tmp)
            tmp = ""
        else:
            tmp += i
    groups.append(tmp)
    return groups


def remove_tabs(item):
    if item[0] == ("\t"):
        item = item.lstrip("\t")
    elif item[0] == (" "):
        item = item.lstrip(" ")
    return item


def find_var_math_oper(text: str) -> str:
    global variable_math_operators
    for i in variable_math_operators:
        if i in text:
            return str(i)
    return "Nah"


def var_math(values: list):
    if values[1] in ["+=", "=+"]:
        return values[0] + values[2]
    if values[1] in ["-=", "=-"]:
        return values[0] - values[2]
    if values[1] in ["*=", "=*"]:
        return values[0] * values[2]
    if values[1] in ["/=", "=/"]:
        return values[0] / values[2]


def remove_num(text, item, num):
    for _ in range(num):
        if text.startswith(item):
            text = list(text)
            textc = ""
            for i in range(len(item)):
                text.pop(i)
            for i in text:
                textc += i
    return textc
