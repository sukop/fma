from decimal import Decimal, getcontext
from xmath import fma

def horner_double(polynomial, x):
    s = 0.0
    for c in polynomial:
        s = s*x + c
    return s

def horner_fma(polynomial, x):
    s = 0.0
    for c in polynomial:
        s = fma(s, x, c)
    return s

def _two_sum(a, b):
    x = a + b
    t = x - a
    y = (a - (x - t)) + (b - t)
    return x, y

def _two_product_fma(a, b):
    x = a*b
    y = fma(a, b, -x)
    return x, y

def horner_compensated(polynomial, x):
    # Based on "Compensated Horner Scheme"
    # by S. Graillat, Ph. Langlois, N. Louvet, 2005
    s = error = 0.0
    for c in polynomial:
        p, pi = _two_product_fma(s, x)
        s, sigma = _two_sum(p, c)
        error = error*x + (pi + sigma)
    return s + error

def horner_decimal(polynomial, x):
    polynomial, x = map(Decimal, polynomial), Decimal(x)
    s = Decimal(0.0)
    for c in polynomial:
        s = s*x + c
    return float(s)

getcontext().prec = 100

polynomial, x = (1.0, -78.0, 2717.0, -55770.0, 749463.0, -6926634.0,
    44990231.0, -206070150.0, 657206836.0, -1414014888.0, 1931559552.0,
    -1486442880.0, 479001600.0), 12.001 # Wilkinson's polynomial

for f in (horner_double, horner_fma, horner_compensated, horner_decimal):
    print(repr(f(polynomial, x)), '\t', f.__name__)
