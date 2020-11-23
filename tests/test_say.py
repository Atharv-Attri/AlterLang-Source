import sys 
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from compiler import compiler


def test_hello():
    assert compiler.main("tests/altr_files/hello.altr") == ["Hello World"]


def test_say_var():
    assert compiler.main("tests/altr_files/say_var.altr") == ["hello", "hello"]


def test_say_multivar():
    assert compiler.main("tests/altr_files/say_multivar.altr") == [1,2, "hello", "1 2 hello \n"]


def test_say_groups():
    assert compiler.main("tests/altr_files/say_groups.altr") == [4, "Alter", "hello, Alter, goodbye 4"]


def test_input_string(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "Alter")
    assert compiler.main("tests/altr_files/say_input.altr") == ["Alter", "Alter"]