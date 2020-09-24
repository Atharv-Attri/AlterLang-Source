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
        return bool(item)

def canConvert(item, type):
    if type == "list":    
        try:
            list(item)
            return True
        except ValueError:
            return False
    if 

        