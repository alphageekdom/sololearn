import numpy_financial as npf

# Monthly mortgage payments
res = npf.pmt(rate=0.07/12, nper=5*12, pv=100000, fv=0)
print(res)