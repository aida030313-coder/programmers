import math

def solution(numer1, denom1, numer2, denom2)
    n = 0; d = 0; x = 0
    n = (numer1 * denom2 + numer2 * denom1)
    d = (denom1 * denom2)
    x = math.gcd(n, d)   # 최대 공약수 구하기

    return [n//x, d//x]


# 파이썬 분수 계산
from fractions import Fraction

def solution(numer1, denom1, numer2, denom2):
    result = Fraction(numer1, denom1) + Fraction(numer2, denom2)
    
    return [result.numerator, result.denominator]