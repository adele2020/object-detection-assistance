# TODO(everyone): 더하기, 빼기, 곱하기, 나누기 함수 정의하기
import math

def plus(arg1, arg2):
    return float(arg1) + float(arg2)

def minus(arg1, arg2):
    return round(float(arg1) - float(arg2), 3)

def multiply(arg1, arg2):
    return round(float(arg1) * float(arg2), 3)

def division(arg1, arg2):
    return round(float(arg1)/float(arg2), 3)

def fn_sqrt(arg1):
    return round(math.sqrt(float(arg1)), 3)
