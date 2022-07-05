import numpy_financial as npf

# Monthly savings 
res = npf.pmt(rate=0.10/12, nper=5*12, pv=0, fv=50000)
print(res)