import pkg_resources
import os
import time

installed = {"ply": False, "rich": False}
installed_packages = pkg_resources.working_set
installed_packages_list = sorted(
    ["%s==%s" % (i.key, i.version) for i in installed_packages]
)
for i in installed_packages:
    if str(i).startswith("ply"):
        installed["ply"] = True
    if str(i).startswith("rich"):
        installed["rich"] = True
if installed["ply"] == False:
    os.system("pip install ply")
if installed["rich"] == False:
    os.system("pip install rich")
import rich

file = input("What file would You like to run? Leave Empty for all: ")
if len(file) != 0:
    os.system("python -m complier tests/" + file)
else:
    rich.print(
        "\n[bold italic turquoise4]===================================[/bold italic turquoise4]\n"
    )
    rich.print(
        "[bold italic turquoise4]Running 1.altr, Topic: Hello World[/bold italic turquoise4]"
    )
    rich.print(
        "\n[bold italic turquoise4]===================================[/bold italic turquoise4]\n"
    )
    time.sleep(0.5)
    os.system("python -m complier tests/1.altr")
    rich.print(
        "\n[bold italic turquoise4]==========================================[/bold italic turquoise4]\n"
    )
    rich.print(
        "[bold italic turquoise4]Running 2.altr, Topic: If Else Statements[/bold italic turquoise4]"
    )
    rich.print(
        "\n[bold italic turquoise4]==========================================[/bold italic turquoise4]\n"
    )
    time.sleep(0.5)
    os.system("python -m complier tests/2.altr")
    rich.print(
        "\n[bold italic turquoise4]=============================[/bold italic turquoise4]\n"
    )
    rich.print(
        "[bold italic turquoise4]Running 3.altr, Topic: Input[/bold italic turquoise4]"
    )
    rich.print(
        "\n[bold italic turquoise4]=============================[/bold italic turquoise4]\n"
    )
    time.sleep(0.5)
    os.system("python -m complier tests/3.altr")
    rich.print(
        "\n[bold italic turquoise4]===================================[/bold italic turquoise4]\n"
    )
    rich.print(
        "[bold italic turquoise4]running 4.altr, Topic: While Loops[/bold italic turquoise4]"
    )
    rich.print(
        "\n[bold italic turquoise4]===================================[/bold italic turquoise4]\n"
    )
    time.sleep(0.5)
    os.system("python -m complier tests/4.altr")
    rich.print(
        "\n[bold italic turquoise4]=====================================[/bold italic turquoise4]\n"
    )
    rich.print(
        "[bold italic turquoise4]running 5.altr, Topic: Guessing Game[/bold italic turquoise4]"
    )
    rich.print(
        "\n[bold italic turquoise4]=====================================[/bold italic turquoise4]\n"
    )
    time.sleep(0.5)
    os.system("python -m complier tests/5.altr")
