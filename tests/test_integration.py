import sys, os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from interpreter import interpreter


def test_setvar():
    assert interpreter.main("tests/altr_files/integration.altr") == [
        1,
        False,
        "Alter",
        "Hello!",
        1,
        "1 False Alter \n",
    ]
