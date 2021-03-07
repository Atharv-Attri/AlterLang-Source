comparables = ["==", "=>", "<=", ">=", "=<", ">", "<"]

with open("names.txt", "r") as f:
    names = f.read().split("\n")


def get_names() -> list:
    global names
    return names


cond_temp = [
    "{val1} {oper} {val2}",
    "{val1} {oper}{val2}",
    "{val1}{oper} {val2}",
    "{val1}{oper}{val2}",
]
