import json
import random


def var(outlines, outfile):
    with open("data.json", "r") as f:
        names = json.load(f)
    names = names["var"]["name"]
    for _ in range(400):
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
    with open("./variables/names.txt", "a") as f:
        for i in names:
            f.write(i + "\t 1\n")


var("f", "f")
