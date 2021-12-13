# tests/test_lib.py
from project_part1.lib  import try_my


def test_try_my():
    assert len(try_my()) != 0
