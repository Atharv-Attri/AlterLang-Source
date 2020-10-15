def datatype(item):
    if "'" in item or '"' in item:
        return "str"
    elif item.lower() in ["false", "true"]:
        return "bool"
    elif item.isdigit():
        return "int"

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
        else: return None
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
        except:
            pass
        try:
            item = float(item)
            return item
        except:
            pass
    return item
