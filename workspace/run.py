import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from compiler import compiler

try:
    sys.argv[1]
except:
    sys.argv.insert(1, "main.altr")

compiler.main(sys.argv[1])
