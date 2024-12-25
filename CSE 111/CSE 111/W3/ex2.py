# from pytest import approx
# import pytest

# def div_by_3(number):
#     return number / 3.0

# def test_div_by_3():
#     assert div_by_3(23) == approx(7.66, abs=0.01)
    
#  assert div_by_3(23) == approx(7.66, rel=0.01)


from weather import cels_from_fahr
from pytest import approx
import pytest

def test_cels_from_fahr():
    assert cels_from_fahr(-25) == approx(-31.66667)
    assert cels_from_fahr(0) == approx(-17.77778)
    assert cels_from_fahr(32) == approx(0)
    assert cels_from_fahr(70) == approx(21.11111)

pytest.main(['-v', '--tb=line', '-rN', _file_ ])


# from file_name import function_1, function_2, function_N

# if _name_== '_main_':
#     main()

