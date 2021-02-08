import json
import random
import util


def varname():
    names = []
    for _ in range(5000):
        num = random.randint(0, 3)
        name = ""
        if num == 0:
            for _ in range(random.randint(2, 15)):
                name += chr(random.randint(65, 90))
        if num == 1:
            for _ in range(random.randint(2, 15)):
                name += chr(random.randint(97, 122))
        if num == 2:
            for _ in range(random.randint(2, 15)):
                tmp = random.randint(0, 1)
                if tmp == 0:
                    name += chr(random.randint(97, 122))
                else:
                    name += chr(random.randint(65, 90))
        if num == 3:
            for _ in range(random.randint(2, 15)):
                tmp = random.randint(0, 1)
                if tmp == 0:
                    name += chr(random.randint(97, 122))
                else:
                    name += chr(random.randint(65, 90))
            name = list(name)
            tmp = random.randint(0, 1)
            if tmp == 1:
                name.insert(random.randint(0, len(name)), "-")
            else:
                name.insert(random.randint(0, len(name)), "_")
            name = "".join(name)
        names.append(name)
    with open("names.txt", "a") as f:
        for i in names:
            f.write(i + "\n")


def varvalue() -> None:
    names = []
    for _ in range(5000):
        num = random.randint(0, 5)
        name = ""
        if num == 0:
            for _ in range(random.randint(2, 15)):
                name += chr(random.randint(65, 90))
        if num == 1:
            for _ in range(random.randint(2, 15)):
                name += chr(random.randint(97, 122))
        if num == 2:
            for _ in range(random.randint(2, 15)):
                tmp = random.randint(0, 1)
                if tmp == 0:
                    name += chr(random.randint(97, 122))
                else:
                    name += chr(random.randint(65, 90))
        if num == 3:
            name = str(random.randint(2, 100000000))
        if num == 4:
            name = random.choice(["False", "false", "true", "True"])
        if num == 5:
            name = str(random.uniform(2, 100000000))
            name = truncate(name, random.randint(1, 7))
        if num in [0, 1, 2]:
            tmp = random.randint(0, 1)
            if tmp == 0:
                name = "'" + name + "'"
            else:
                name = '"' + name + '"'
        names.append(name)
    with open("values.txt", "a") as f:
        for i in names:
            f.write(i + "\n")


def fit_var_template(template: str, name: str, value: str) -> str:
    template = template.replace("{var}", name)
    template = template.replace("{value}", value)
    return template


def truncate(f: float, n: int) -> float:
    """Truncates/pads a float f to n decimal places without rounding"""
    s = "{}".format(f)
    if "e" in s or "E" in s:
        return "{0:.{1}f}".format(f, n)
    i, p, d = s.partition(".")
    return ".".join([i, (d + "0" * n)[:n]])


def fit_ifwhile_template(template: str, cond: str) -> str:
    return template.replace("{cond}", cond)


def make_condition() -> str:
    names = util.get_names()

    condition = random.choice(util.cond_temp)
    comp = random.choice(util.comparables)
    vals = []
    for _ in range(2):
        tmp = random.randint(0, 1)
        if tmp == 0:
            vals.append(random.choice(names))
        else:
            dec = random.randint(0, 1)
            if dec == 0:
                vals.append(str(random.randint(0, 10000000)))
            else:
                vals.append(str(random.uniform(0, 10000000)))
    condition = (
        condition.replace("{oper}", comp)
        .replace("{val1}", vals[0])
        .replace("{val2}", vals[1])
    )
    return condition


def make_while_files() -> None:
    with open("data.json", "r") as f:
        data = json.load(f)
    templates = data["while"]["templates"]

    for i in range(5000, 9000):
        template = random.choice(templates)
        cond = make_condition()
        fname = str(i).zfill(6)
        with open(f"./Alter/Alter-train/while/{fname}", "w") as f:
            f.write(template.replace("{cond}", cond))
    for i in range(9000, 10000):
        template = random.choice(templates)
        cond = make_condition()
        fname = str(i).zfill(6)
        with open(f"./Alter/Alter-test/while/{fname}", "w") as f:
            f.write(template.replace("{cond}", cond))


# varname()
# varvalue()
# make_var_files()
def make_if_files() -> None:
    with open("data.json", "r") as f:
        data = json.load(f)
    templates = data["if"]["templates"]

    for i in range(10000, 14000):
        template = random.choice(templates)
        cond = make_condition()
        fname = str(i).zfill(6)
        with open(f"./Alter/Alter-train/if/{fname}", "w") as f:
            f.write(template.replace("{cond}", cond))
    for i in range(14000, 15000):
        template = random.choice(templates)
        cond = make_condition()
        fname = str(i).zfill(6)
        with open(f"./Alter/Alter-test/if/{fname}", "w") as f:
            f.write(template.replace("{cond}", cond))


def var_tsv() -> None:
    with open("data.json", "r") as f:
        data = json.load(f)
    templates = data["var"]["templates"]
    with open("names.txt", "r") as f:
        names = f.read().split("\n")
    with open("values.txt", "r") as f:
        values = f.read().split("\n")
    for n in range(2000):
        fname = str(n).zfill(6)
        ctemp = random.choice(templates)
        cname = random.choice(names)
        cvalue = random.choice(values)
        with open(f"./tsvs/var.tsv", "a") as f:
            f.write(fit_var_template(ctemp, cname, cvalue) + "\tpos\n")
    with open("data.json", "r") as f:
        data = json.load(f)
    templates = data["if"]["templates"]

    for i in range(500):
        template = random.choice(templates)
        cond = make_condition()
        fname = str(i).zfill(6)
        with open(f"./tsvs/var.tsv", "a") as f:
            f.write(template.replace("{cond}", cond) + "\tneg\n")

    with open("data.json", "r") as f:
        data = json.load(f)
    templates = data["while"]["templates"]

    for i in range(500):
        template = random.choice(templates)
        cond = make_condition()
        fname = str(i).zfill(6)
        with open(f"./tsvs/var.tsv", "a") as f:
            f.write(template.replace("{cond}", cond) + "\tneg\n")


def shuffle():
    with open("./tsvs/var.tsv", "r") as f:
        lines = f.read().split("\n")
    with open("./tsvs/var.tsv", "w") as f:
        f.write("")
    random.shuffle(lines)
    with open("./tsvs/var.tsv", "a") as f:
        for i in lines:
            f.write(i + "\n")


def make_json(filename: str) -> None:
    with open(filename, "r") as f:
        lines = f.read().split("\n")
    al = []
    for i in lines:
        i = i.split("\t")
        if len(i) != 2:
            continue
        cur = {"text": None, "label": None}
        cur["text"] = i[0]
        cur["label"] = i[1]
        al.append(cur)
    with open("model.json", "w") as f:
        json.dump(al, f, indent=4)


varname()
varvalue()
var_tsv()
make_json("./tsvs/var.tsv")
