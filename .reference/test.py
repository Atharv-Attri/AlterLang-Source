import subprocess
from time import sleep
from csv import DictReader
import rich
from rich.progress import track
from rich.panel import Panel
from os import system
from pyautogui import click, typewrite, hotkey


def main():
    r_file = open("tests.csv", "r")
    filed = DictReader(r_file)
    passed = 0
    total = 0
    failed = []
    for i in filed:
        if i["live"] == "0":
            total += 1
            out = subprocess.Popen(
                f"python -m compiler tests/{i['file']}", stdout=subprocess.PIPE
            )
            data = str(out.communicate())
            print(data)
            data = data.split(r"\r\n")
            outputs = i["output"].rstrip("]")
            outputs = outputs.lstrip("[")
            outputs = outputs.split("~")
            a = int(i["startline"])
            error = False
            rich.print(Panel(f"[bold blue]Running {i['file']}...[/bold blue]"))

            for step in track(range(100)):
                pass
            for j in outputs:
                if data[a] == j:
                    pass
                else:
                    rich.print(
                        f"[bold red]\nTest Failed. Output line {a} did not match expected {j}. Actual Output: {data[a]}[/bold red]"
                    )
                    error = True
                a += 1
            if not error:
                rich.print(
                    f"[bold green]Tests for {i['file']} were a success![/bold green]"
                )
                passed += 1
            if error:
                rich.print(f"[bold red]\nTests for {i['file']} FAILED![/bold red]")
                failed.append(i["file"])
        if i["live"] == "1":
            rich.print(f"[bold blue]\nRunning {i['file']}...[/bold blue]")
            send_input(i["file"])
            system(f"python -m complier tests/{i['file']}")
    outp = ""
    r_file.close()
    outp += f"[bold blue]{passed} out of {total} automated tests passed!\n[/bold blue]"
    if len(failed) == 0:
        outp += f"[bold green]No auotmated tests failed![/bold green]"
    else:
        outp += f"[bold red]{len(failed)} auotmated tests failed![/bold red]"
        for i in failed:
            outp += f"\n[bold red]{i} failed"
    rich.print(Panel(outp, title="Summary"))


def send_input(filename) -> None:
    print(filename)
    sleep(2)
    click(1208, 955)
    if filename == "3.altr":
        typewrite("Alter", interval=0.3)
        hotkey("enter")
        return None


if __name__ == "__main__":
    main()
