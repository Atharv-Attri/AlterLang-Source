import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from interpreter import interpreter


def test_input_string(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "Alter")
    assert interpreter.main("tests/altr_files/input.altr") == ["Alter"]

