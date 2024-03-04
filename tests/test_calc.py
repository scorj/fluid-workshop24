
import functions.calc as fc
import pytest
def test_negatives():
    assert fc.adivb(-10,-5) == 2, "Two negative should return a positive "

def test_pos_neg():

     assert fc.adivb(-9,3) == -3, "One positive one negative should return a negative "

def test_positive():

    assert fc.adivb(35,7) > 0, "Two pos should be pos"


def test_type():
    assert isinstance(fc.adivb(5,10), float), "minor by larger should be float"


def test_float():

    assert fc.adivb(5,2) == 2.5, "5/2 should be 2.5"



def test_rational(): 
    assert fc.adivb(10,3) == pytest.approx(3.33, 0.01), "10/3 should be 3.333"