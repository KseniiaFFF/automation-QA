import pytest
from functions_for_tests import merge_and_count

def test_positive():
    assert merge_and_count({}, {}) == {}
    assert merge_and_count({"f":0},{}) == {"f":0}
    assert merge_and_count({},{"v":3}) == {"v":3}

    assert merge_and_count({"a":4, "t": 9, "c":5}, {"a":2,"b":7}) == {"a":6, "t": 9, "c":5,"b":7}

def test_negative_dict():
    with pytest.raises(TypeError):
        merge_and_count(["TypeError"], {"c":5}) 

    with pytest.raises(TypeError):
        merge_and_count(890, {"k":7}) 

    with pytest.raises(TypeError):
        merge_and_count("TypeError", {"c":5})         


def test_negative_int():
    with pytest.raises(ValueError):
        merge_and_count({"u":8},{"r":"6"}) 

    with pytest.raises(ValueError):
        merge_and_count({"u":8},{"r":4.4})     

    with pytest.raises(ValueError):
        merge_and_count({5:"6"},{"c":5})       
  

    