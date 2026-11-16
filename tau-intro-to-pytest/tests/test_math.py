import pytest

def test_one_plus_one():
    assert 1 + 1 == 2

#assertion introspection a + b == 1(error)
def test_one_plus_two():
    a = 1
    b = 2
    c = 3
    assert a + b == c 
    
def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError) as e: #pytest.raises
        num = 1 /0 
        #expected exception

    assert 'division by zero' in str(e.value)
    
#Equivalence classes
"""
Multiplication ideas:
2 positive integers
identity: multiply by 1
zero: multiply by 0
positive by negative
negative by negative
floats
"""
# def test_multiply_two_positive_ints():
#     assert 2 * 3 == 6
# def test_multiply_identity():
#     assert 1 * 99 == 99
# def test_multiply_zero():
#     assert 0 * 100 == 100

#pytest.mark.parametrize

products = [
    (2,3,6),
    (1,99,99),
    (0,99,0),
    (3,-4,-12),
    (-5,-5,25),
    (2.5,6.7,16.75)
]

@pytest.mark.parametrize('a, b, product', products)
def test_multiplication(a, b, product):
    assert a * b == product
