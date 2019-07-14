from decimal import *

deci1 = round(Decimal('0.7') * Decimal('1.05'), 2)

print(deci1)
deci2 = round(.70 * 1.05,2)

print(deci2)

dec3 = Decimal('1.00') %Decimal('.10')
print(dec3)

mod = 1.00%0.10
print(mod)

tot = sum([Decimal('0.1')]*10) == Decimal('1.0')
print(tot)

tot3 = sum([0.1]*10) == 1.0

print(tot3)
what = getcontext().prec = 36

print(what)

WHAT = Decimal(1)/Decimal(7)
print(WHAT)