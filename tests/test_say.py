import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from interpreter import interpreter


def test_hello():
    assert interpreter.main("tests/altr_files/hello.altr") == ["Hello World"]


def test_say_var():
    assert interpreter.main("tests/altr_files/say_var.altr") == ["hello", "hello"]


def test_say_multivar():
    assert interpreter.main("tests/altr_files/say_multivar.altr") == [
        1,
        2,
        "hello",
        "1 2 hello \n",
    ]


def test_say_groups():
    assert interpreter.main("tests/altr_files/say_groups.altr") == [
        4,
        "Alter",
        "hello, Alter, goodbye 4",
    ]


def test_input_string(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "Alter")
    assert interpreter.main("tests/altr_files/say_input.altr") == ["Alter", "Alter"]
