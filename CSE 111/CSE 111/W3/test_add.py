from add import add_me
from pytest import approx, main

def test_add_me():
    
    assert  add_me(1, 2) ==3
    assert  add_me(1.5, 1.5) == approx(3.0)
    
main(['-v', '--tb=line', '-rN', _file_ ])
    
    