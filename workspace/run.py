import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from interpreter import interpreter

try:
    sys.argv[1]
except:
    sys.argv.insert(1, "main.altr")

interpreter.main(sys.argv[1])
