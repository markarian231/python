from math import gcd

def add_frac(frac1, frac2):
    numerator = frac1[0] * frac2[1] + frac2[0] * frac1[1]
    denominator = frac1[1] * frac2[1]
    common_divisor = gcd(numerator, denominator)
    return [numerator // common_divisor, denominator // common_divisor]

def sub_frac(frac1, frac2):
    numerator = frac1[0] * frac2[1] - frac2[0] * frac1[1]
    denominator = frac1[1] * frac2[1]
    common_divisor = gcd(numerator, denominator)
    return [numerator // common_divisor, denominator // common_divisor]

def mul_frac(frac1, frac2):
    numerator = frac1[0] * frac2[0]
    denominator = frac1[1] * frac2[1]
    common_divisor = gcd(numerator, denominator)
    return [numerator // common_divisor, denominator // common_divisor]

def div_frac(frac1, frac2):
    numerator = frac1[0] * frac2[1]
    denominator = frac1[1] * frac2[0]
    common_divisor = gcd(numerator, denominator)
    return [numerator // common_divisor, denominator // common_divisor]

def is_positive(frac):
    return frac[0] / frac[1] > 0

def is_zero(frac):
    return frac[0] == 0

def cmp_frac(frac1, frac2):
    reduced_frac1 = [frac1[0] * frac2[1], frac1[1] * frac2[1]]
    reduced_frac2 = [frac2[0] * frac1[1], frac2[1] * frac1[1]]
    if reduced_frac1[0] > reduced_frac2[0]:
        return 1
    elif reduced_frac1[0] < reduced_frac2[0]:
        return -1
    else:
        return 0

def frac2float(frac):
    return frac[0] / frac[1]
