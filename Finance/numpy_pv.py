import numpy_financial as npf

res = npf.pv(rate=0.10, nper=8, pmt=0, fv=1000)
print(res)