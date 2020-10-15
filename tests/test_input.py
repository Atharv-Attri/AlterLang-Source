import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from compiler import compiler

def test_input_string(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "Alter")
    assert compiler.main("tests/altr_files/8input.altr") == ["Alter"]