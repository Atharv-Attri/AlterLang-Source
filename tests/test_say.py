import sys
import os
import lid.util

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from interpreter import interpreter


def test_hello(model):
    assert interpreter.main("tests/altr_files/hello.altr") == ["Hello World"]


def test_say_var(model):
    assert interpreter.main("tests/altr_files/say_var.altr") == ["hello", "hello"]


def test_say_multivar(model):
    assert interpreter.main("tests/altr_files/say_multivar.altr") == [
        1,
        2,
        "hello",
        "1 2 hello \n",
    ]


def test_say_groups(model):
    assert interpreter.main("tests/altr_files/say_groups.altr") == [
        4,
        "Alter",
        "hello, Alter, goodbye 4",
    ]


# def test_input_string(monkeypatch, model):
# monkeypatch.setattr("builtins.input", lambda _: "Alter")
# assert interpreter.main("tests/altr_files/say_input.altr") == ["Alter", "Alter"]


def main(model) -> None:
    test_say_groups(model)
    test_say_multivar(model)
    test_say_var(model)
    test_hello(model)
