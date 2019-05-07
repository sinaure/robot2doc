#!/env/python

import robot2doc

def test_keyword_to_line():
    assert keyword_to_line("a", "b", "c") == "a b c" 