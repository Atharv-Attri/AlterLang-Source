import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from compiler import compiler


def test_hello():
    assert compiler.main("tests/altr_files/if_statement.altr") == [
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
