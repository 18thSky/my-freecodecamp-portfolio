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
    
    
    
    
    