import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from compiler import compiler

def test_hello():
    assert compiler.main("tests/altr_files/1hello.altr") == ["Hello World"]

def test_say_var():
    assert compiler.main("tests/altr_files/5say_var.altr") == ["hello", "hello"]
def test_say_multivar():
    assert compiler.main("tests/altr_files/6say_multivar.altr") == [1,2, "hello", "1 2 hello \n"]