import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from compiler import compiler


def test_setvar():
    assert compiler.main("tests/altr_files/2setvar.altr") == [1]


def test_multivar():
    assert compiler.main("tests/altr_files/3multi_var.altr") == [1, 3]

def test_multi_letter_var():
    assert compiler.main("tests/altr_files/4multi_letter_var.altr") == ["Hello"]