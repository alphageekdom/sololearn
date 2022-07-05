import numpy_financial as npf

cashflow = [-5000, 500, 700, 1000, 3000]

print(npf.irr(cashflow))