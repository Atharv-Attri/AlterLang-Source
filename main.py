import pkg_resources
import os
installed = {"ply" : False, "rich": False}
installed_packages = pkg_resources.working_set
installed_packages_list = sorted(["%s==%s" % (i.key, i.version)
   for i in installed_packages])
for i in installed_packages:
    if str(i).startswith("ply"):
        installed["ply"] = True
    if str(i).startswith("rich"):
        installed["rich"] = True
if installed["ply"] == False:
    os.system("pip install ply")
if installed["rich"] == False:
    os.system("pip install rich")

file = input("What file would You like to run? Leave Empty for all: ")

os.system("python -m complier tests/" + file)