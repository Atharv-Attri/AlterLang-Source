import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from compiler import util


def test_greater():
    assert util.condition("if a > 100 ->", {"a": 5}) is False
    assert util.condition("if a > 100 ->", {"a": 500}) is True
    assert util.condition("if 100 > a ->", {"a": 500}) is False


def test_lesser():
    assert util.condition("if a < 100 ->", {"a": 5}) is True
    assert util.condition("if a < 100 ->", {"a": 500}) is False
    assert util.condition("if 100 < a ->", {"a": 5}) is False


def test_equal():
    assert util.condition("if 100 <= a ->", {"a": 5}) is False
    assert util.condition("if 100 =< a ->", {"a": 5}) is False
    assert util.condition("if 100 <= a ->", {"a": 500}) is True
    assert util.condition("if 100 =< a ->", {"a": 500}) is True
    assert util.condition("if 100 >= a ->", {"a": 5}) is True
    assert util.condition("if 100 =< a ->", {"a": 5}) is False
    assert util.condition("if 100 <= a ->", {"a": 500}) is True
    assert util.condition("if a <= 100 ->", {"a": 500}) is False
    assert util.condition("if a == 500 ->", {"a": 500}) is True
