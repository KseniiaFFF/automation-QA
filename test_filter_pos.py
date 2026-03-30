import pytest
from functions_for_tests import filter_positive_even_numbers

def test_positive():
    assert filter_positive_even_numbers([8,5,6, -66]) == [8,6]
    assert filter_positive_even_numbers([]) == []
    assert filter_positive_even_numbers([0,-5,6,-88]) == [6]
    assert filter_positive_even_numbers([1,2.3,6]) == [6]

def test_negative_list():
    with pytest.raises(TypeError):
        filter_positive_even_numbers("TypeError") 

    with pytest.raises(TypeError):
        filter_positive_even_numbers(345) 

    with pytest.raises(TypeError):
        filter_positive_even_numbers(None)         

def test_negative_nums():
    with pytest.raises(ValueError):
        filter_positive_even_numbers([1,2,'3'])   

    with pytest.raises(ValueError):
        filter_positive_even_numbers([1,True,6])      

    