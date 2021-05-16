# TODO(everyone): 더하기, 빼기, 곱하기, 나누기 함수 테스트 케이스 작성
import pytest
from oda_app.functions import plus, minus, multiply, division

def test_plus():
    assert plus(1,2) == 3

def test_plus_none():
    assert plus(None, 2) == 2

def test_minus():
    assert minus(1,2) == -1.0

def test_multiply():
    assert multiply(1,2) == 2.0

def test_division():
    assert division(1,2) == 0.5

pytest.main()

