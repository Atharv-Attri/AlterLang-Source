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
  '''
  Parameters:
    :param text, grouper, seperator: strings
  Return:
    type - string
  '''
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
