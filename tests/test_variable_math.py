import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from compiler import compiler


def test_math():
    assert compiler.main("tests/altr_files/varmath.altr") == [5, 0.546797, "foo", True, 6, 18, 1.0, 5.756797, 1.43919925, 'foofoofoofoofoo', 1.43919925, 1.43919925, 0, 'foofoofoofoofoobar', 'foofoofoofoofoobarbaz', 1, 56.43919925, ]
