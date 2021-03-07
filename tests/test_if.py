import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from interpreter import interpreter


def test_hello():
    assert interpreter.main("tests/altr_files/if_statement.altr") == [
        5,
        44,
        0,
        -9,
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
    ]
