import re
import time
import rich
import sys
import os
from textblob import TextBlob
from rich.console import Console
import importlib.util
import traceback
try:
    from . import interpreter, usemodel

except ImportError:
    import interpreter
    import usemodel

rich.print("[blue]Alter Command Line Interface v.ALPHA")
# Progress Info when running code
console = Console()
tasks = [
    "Loaded Machine Learning Model",
    "Re-Processed model",
    "Verified model speed",
    "Verified model accuracy",
]
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
    if blob.classify() == "var":
        pass
    else:
        print("[bold red]Model may not be accurate")
        print(blob.classify())

    task = tasks.pop(0)
    console.log(f"{task}")


def run_tests():
    sys.path.append(os.path.join(os.path.dirname(__file__), "../tests"))
    print(os.listdir())
    test_file_names = [i for i in os.listdir() if i.startswith("test_")]
    print(test_file_names)
    return
    for i,x in enumerate(test_file_names):
        spec = importlib.util.spec_from_file_location("Fdf", i)
        testfunc = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(foo)
        testfunc.MyClass()

while True:
    importlib.reload(interpreter)
    argin = input(">")
    if argin.startswith("run"):
        if "." in argin:
            fname = re.findall(r"run (\w+)\.altr", argin)
            while len(fname) ==0:
                argin = input("> ")
                fname = re.findall(r"run (\w+)\.altr", argin)
            fname = fname[0]
        else:
            fname = "test"
        try:
            interpreter.main(fname + ".altr", model)
            print("\n\n")
            interpreter.clear()
        except Exception:
            traceback.print_exc()
            pass
        


    elif argin.startswith("exit"):
        exit()
    elif argin.startswith("test"):
        run_tests()
    else:
        rich.print("[bold red]Command Not Understood")
