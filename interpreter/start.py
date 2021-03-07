import re
import time
import rich
from textblob import TextBlob
from rich.console import Console

try:
    from . import interpreter, usemodel

except ImportError:
    import interpreter
    import usemodel

rich.print("[blue]Alter Command Line Interface v.ALPHA")

console = Console()
tasks = ["Loaded Machine Learning Model", "Re-Processed model", "Verified model speed", "Verified model accuracy"]
with console.status("[bold green]Starting...") as status:
    model = usemodel.load()
    task = tasks.pop(0)
    console.log(f"{task}")
    blob = TextBlob("the value of x is 5", classifier=model)
    blob.classify()
    task = tasks.pop(0)
    console.log(f"{task}")
    ct = time.time()
    blob = TextBlob("the value of x is 4", classifier=model)
    blob.classify()
    if time.time() - ct < 1.5:
        pass
    else:
        print("[bold red]Model May Run Slow")
    task = tasks.pop(0)
    console.log(f"{task}")
    blob = TextBlob("let x equal 4", classifier=model)
    if blob.classify() == "pos":
        pass
    else:
        print("[bold red]Model may not be accurate")
        print(blob.classify())

    task = tasks.pop(0)
    console.log(f"{task}")

while True:
    argin = input(">")
    if argin.startswith("run"):
        if "." in argin:
            fname = re.findall(r"run *(\w+).altr")
        else:
            fname = "test"
        
        interpreter.main(fname+".altr", model)
        print("\n\n")
        interpreter.clear()

    elif argin.startswith("exit"):
        exit()
    else:
        rich.print("[bold red]Command Not Understood")
